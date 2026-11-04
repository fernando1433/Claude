#!/bin/bash
# 2a cola de render (tras la primera): ambientes de CASA para los videos del dia a dia. Uso: bash motor/cola_render2.sh [logdir]
cd "$(dirname "$0")/.."
LOG=${1:-/tmp}
LITE_PLANOS="humano dos general monitor monitor_espalda monitor_lateral claude_ojos cenital"
while [ ! -f $LOG/COLA_TERMINADA ]; do sleep 20; done
etapa() {
  local nombre=$1 amb=$2 dec=$3 lite=$4; shift 4
  [ -f $LOG/LISTO_$nombre ] && return
  echo "== $nombre (inicio $(date +%H:%M:%S))" >> $LOG/cola.log
  VC_AMBIENTE=$amb VC_DECOR=$dec VC_LITE=$lite python3 -I motor/render_biblioteca.py "$PWD/biblioteca/$nombre" "$@" > $LOG/render_$nombre.log 2>&1
  python3 -I motor/indice_biblioteca.py "$nombre" >> $LOG/cola.log 2>&1
  touch $LOG/LISTO_$nombre; echo "== $nombre LISTO ($(date +%H:%M:%S))" >> $LOG/cola.log
}
etapa noche_casa noche casa 1 $LITE_PLANOS
etapa dia_casa dia casa 1 $LITE_PLANOS
touch $LOG/COLA2_TERMINADA
