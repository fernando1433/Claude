#!/bin/bash
# Monta cada video en cuanto su biblioteca (ambiente) esta lista. Uso: bash motor/cola_montaje.sh [logdir]
cd "$(dirname "$0")/.."
LOG=${1:-/tmp}
montar() {   # ambiente id...
  local amb=$1; shift
  while [ ! -f $LOG/LISTO_$amb ]; do sleep 15; done
  for id in "$@"; do
    echo "montando $id ($(date +%H:%M:%S))" >> $LOG/montaje.log
    python3 -I motor/montar_video.py guiones/$id.json salidas/$id.mp4 >> $LOG/montaje.log 2>&1
    echo "listo $id ($(date +%H:%M:%S))" >> $LOG/montaje.log; touch $LOG/VIDEO_$id
  done
}
montar noche_trading trading_01_curso_milagro
montar dia_trading trading_02_senales_vip trading_03_apalancamiento_x100
montar dia_tienda drop_01_que_es_dropshipping drop_02_producto_ganador
montar atardecer_tienda drop_03_primer_pedido
touch $LOG/MONTAJE_TERMINADO
