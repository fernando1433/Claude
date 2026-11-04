#!/bin/bash
# Cola de render de TODAS las bibliotecas (ambientes). Reanudable: no repite capas que ya existen.
# Uso: bash motor/cola_render.sh [logdir]
cd "$(dirname "$0")/.."
LOG=${1:-/tmp}
LITE_PLANOS="humano dos general monitor monitor_espalda monitor_lateral claude_ojos cenital"
etapa() {   # nombre ambiente decorado lite planos...
  local nombre=$1 amb=$2 dec=$3 lite=$4; shift 4
  echo "== $nombre (inicio $(date +%H:%M:%S))" >> $LOG/cola.log
  VC_AMBIENTE=$amb VC_DECOR=$dec VC_LITE=$lite python3 -I motor/render_biblioteca.py "$PWD/biblioteca/$nombre" "$@" > $LOG/render_$nombre.log 2>&1
  python3 -I motor/indice_biblioteca.py "$nombre" >> $LOG/cola.log 2>&1
  touch $LOG/LISTO_$nombre
  echo "== $nombre LISTO ($(date +%H:%M:%S))" >> $LOG/cola.log
}
rm -f biblioteca/noche_trading/*/claude_*.png     # Clawd sin brillos en los ojos: se re-renderiza
etapa noche_trading noche trading 0
etapa dia_trading dia trading 1 $LITE_PLANOS
etapa dia_tienda dia tienda 1 $LITE_PLANOS
etapa atardecer_tienda atardecer tienda 1 $LITE_PLANOS
touch $LOG/COLA_TERMINADA
