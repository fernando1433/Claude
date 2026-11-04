# Este tío tiene un yate y dice que me hace rico

**Archivo de guion:** `guiones/trading_05_el_guru_del_yate.json` · **Ambiente:** `noche_trading` · **Duración:** 44 s (264 frames de animación a 6 fps)

El gurú de Instagram con yate, coches y seguidores comprados. Claude le baja los humos con sarcasmo y el dato de ESMA.

**Gancho (primera frase):** «Claude, este tío tiene un yate y dice que me hace rico.»

## Cómo se genera el vídeo
```bash
python3 -I motor/montar_video.py guiones/trading_05_el_guru_del_yate.json salidas/trading_05_el_guru_del_yate.mp4
```
El guion se creó con `motor/generar_guiones.py` (tiempos automáticos según la longitud de cada frase y pantallas sincronizadas con el diálogo). Biblioteca usada: `biblioteca/noche_trading/`.

## Guion plano a plano

| # | Tiempo | Quién | Texto | Plano | Emoción / pose / estado | Pantalla del monitor |
|---|---|---|---|---|---|---|
| 1 | 0.0–4.3 | Humano | Claude, este tío tiene un yate / y dice que me hace rico. | `humano` | ilusionado | analitica (24.24 s) |
| 2 | 4.3–6.0 | Claude | ¿Ese yate es suyo? | `monitor` | mira_izq |  |
| 3 | 6.0–8.2 | Humano | Sale en todas las fotos. | `dos` | bobo |  |
| 4 | 8.2–12.1 | Claude | Se puede alquilar por horas. / Tiene tarifa y todo. | `claude_ojos` | idle |  |
| 5 | 12.1–13.8 | Humano | ¿Y los seguidores? | `humano` | confundido |  |
| 6 | 13.8–17.1 | Claude | Se pueden comprar. Por / miles. A céntimos. | `cenital` | mira_der |  |
| 7 | 17.1–18.8 | Humano | ¿Todo es falso? | `dos` | preocupado |  |
| 8 | 18.8–21.8 | Claude | Todo no. Lo único real / es tu tarjeta. | `monitor` | feliz |  |
| 9 | 21.8–24.4 | Humano | Pero dice que gana en directo. | `humano` | bobo |  |
| 10 | 24.4–28.7 | Claude | Dato real: 74–89 % de cuentas / minoristas de CFD pierde. | `pantalla_completa` | idle | verdad (4.32 s) |
| 11 | 28.7–30.8 | Humano | Yo pensaba que ganaba. | `dos` | confundido |  |
| 12 | 30.8–33.7 | Claude | Él gana. Con los que / pagan su curso. | `claude_ojos` | mira_izq, empuje de cámara |  |
| 13 | 33.7–35.9 | Humano | ¿Entonces dónde invierto? | `humano` | preocupado |  |
| 14 | 35.9–39.5 | Claude | Donde entiendas, con poco / riesgo y sin gurús. | `monitor` | mira_arriba |  |
| 15 | 39.5–41.2 | Humano | ¡Pues sin gurú! | `dos` | ilusionado |  |
| 16 | 41.2–44.0 | Claude | Y sin yate. / En fin... eres humano. | `general` | feliz |  |

## Datos reales que aparecen o se mencionan

- 74–89 % de cuentas minoristas de CFD pierden dinero (ESMA, 2018).
  - Fuente: [ESMA (2018): prohíbe las opciones binarias y restringe los CFD a minoristas](https://www.esma.europa.eu/node/84933)
  - Fuente: [ESMA: renovación de las restricciones a los CFD](https://www.esma.europa.eu/press-news/esma-news/esma-renew-restriction-cfds-further-three-months)
- Los seguidores se pueden comprar y los yates y coches de lujo se pueden alquilar por horas: afirmaciones de carácter general, no de una persona concreta.

## Notas de producción

- **Humor:** Claude es sarcástico y pícaro («como el que le salva el culo»); el humano es ingenuo y algo tonto (expresiones `bobo`, `ilusionado`, `confundido`).
- **Voces:** son «blips» sintéticos (no hay voz real). Para voz real: ElevenLabs o grabarla y sustituir el audio.
- **Cifras y leyes:** los datos reales están citados arriba; las cuentas de ejemplo (márgenes, 214 tiendas, etc.) son ilustrativas. No es asesoramiento financiero ni legal.
