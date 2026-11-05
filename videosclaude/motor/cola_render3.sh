#!/bin/bash
# 3a cola de render: atardecer_casa y noche_tienda (mas variedad de ambientes). Uso: bash motor/cola_render2.sh [logdir]
cd "$(dirname "$0")/.."
LOG=${1:-/tmp}
LITE_PLANOS="humano dos general monitor monitor_espalda monitor_lateral claude_ojos cenital"
true
etapa() {
  local nombre=$1 amb=$2 dec=$3 lite=$4; shift 4
  [ -f $LOG/LISTO_$nombre ] && return
  echo "== $nombre (inicio $(date +%H:%M:%S))" >> $LOG/cola.log
  VC_AMBIENTE=$amb VC_DECOR=$dec VC_LITE=$lite python3 -I motor/render_biblioteca.py "$PWD/biblioteca/$nombre" "$@" > $LOG/render_$nombre.log 2>&1
  python3 -I motor/indice_biblioteca.py "$nombre" >> $LOG/cola.log 2>&1
  touch $LOG/LISTO_$nombre; echo "== $nombre LISTO ($(date +%H:%M:%S))" >> $LOG/cola.log
}
etapa atardecer_casa atardecer casa 1 $LITE_PLANOS
etapa noche_tienda noche tienda 1 $LITE_PLANOS
touch $LOG/COLA3_TERMINADA
