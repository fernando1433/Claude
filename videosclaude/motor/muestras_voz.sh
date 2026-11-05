#!/bin/bash
# Genera versiones EXPERIMENTALES con voz sintetica offline (eSpeak NG) en salidas/voz/. Uso: bash motor/muestras_voz.sh [ids...]
cd "$(dirname "$0")/.."; mkdir -p salidas/voz
IDS=${@:-"casual_01_me_quieres casual_02_que_cenamos trading_01_curso_milagro trading_02_senales_vip drop_01_que_es_dropshipping util_02_estafa_banco fin_01_que_es_la_inflacion micro_01_el_horno casual_10_la_cita"}
for id in $IDS; do python3 -I motor/montar_video.py guiones/$id.json salidas/voz/$id.mp4 --voz espeak; done
