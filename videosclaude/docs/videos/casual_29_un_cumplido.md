# Claude, me han hecho un cumplido y no sé qué contestar

**Archivo de guion:** `guiones/casual_29_un_cumplido.json` · **Ambiente:** `dia_casa` · **Duración:** 36 s (216 frames de animación a 6 fps)

El pánico de recibir un cumplido. Claude resume la respuesta correcta en dos palabras.

**Gancho (primera frase):** «Claude, me han hecho un cumplido y no sé qué contestar.»

## Cómo se genera el vídeo
```bash
python3 -I motor/montar_video.py guiones/casual_29_un_cumplido.json salidas/casual_29_un_cumplido.mp4
```
El guion se creó con `motor/generar_guiones.py` (tiempos automáticos según la longitud de cada frase y pantallas sincronizadas con el diálogo). Biblioteca usada: `biblioteca/dia_casa/`.

## Guion plano a plano

| # | Tiempo | Quién | Texto | Plano | Emoción / pose / estado | Pantalla del monitor |
|---|---|---|---|---|---|---|
| 1 | 0.0–5.2 | Humano | Claude, me han hecho un cumplido / y no sé qué contestar. | `humano` | confundido | mensajes (36.0 s) |
| 2 | 5.2–7.4 | Claude | ¿Qué te han dicho? | `monitor` | mira_izq |  |
| 3 | 7.4–10.6 | Humano | «Qué bien te queda ese jersey.» | `dos` | bobo |  |
| 4 | 10.6–13.1 | Claude | Qué cosa más terrible. | `claude_ojos` | feliz |  |
| 5 | 13.1–15.9 | Humano | Yo dije «es de hace años». | `humano` | preocupado |  |
| 6 | 15.9–19.3 | Claude | Ya. Y luego / «no es nada especial». | `cenital` | mira_der |  |
| 7 | 19.3–22.2 | Humano | Y luego, «gracias... creo». | `dos` | confundido |  |
| 8 | 22.2–25.6 | Claude | Hay una respuesta / mejor. Es corta. | `monitor` | feliz |  |
| 9 | 25.6–27.6 | Humano | ¿Cuál? | `humano` | ilusionado |  |
| 10 | 27.6–29.7 | Claude | «Gracias.» | `claude_ojos` | idle, empuje de cámara |  |
| 11 | 29.7–31.7 | Humano | ¿Solo eso? | `dos` | bobo |  |
| 12 | 31.7–36.0 | Claude | Solo eso. Es difícil. / En fin... eres humano. | `general` | feliz |  |

## Datos reales que aparecen o se mencionan

- Vídeo de humor, sin datos reales.

## Notas de producción

- **Humor:** Claude es sarcástico y pícaro («como el que le salva el culo»); el humano es ingenuo y algo tonto (expresiones `bobo`, `ilusionado`, `confundido`).
- **Voces:** son «blips» sintéticos (no hay voz real). Para voz real: ElevenLabs o grabarla y sustituir el audio.
- **Cifras y leyes:** los datos reales están citados arriba; las cuentas de ejemplo (márgenes, 214 tiendas, etc.) son ilustrativas. No es asesoramiento financiero ni legal.
