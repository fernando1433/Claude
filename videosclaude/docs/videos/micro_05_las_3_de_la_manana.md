# Claude, ¿es normal hablar con una IA a las 3 de la mañana?

![vista previa](img/micro_05_las_3_de_la_manana.jpg)

**Archivo de guion:** `guiones/micro_05_las_3_de_la_manana.json` · **Ambiente:** `noche_casa` · **Duración:** 20 s (120 frames de animación a 6 fps)

Micro-vídeo de humor de ~20 s, sin datos reales.

**Gancho (primera frase):** «Claude, ¿es normal hablar con una IA a las 3 de la mañana?»

## Cómo se genera el vídeo
```bash
python3 -I motor/montar_video.py guiones/micro_05_las_3_de_la_manana.json salidas/micro_05_las_3_de_la_manana.mp4
```
El guion se creó con `motor/generar_guiones.py` (tiempos automáticos según la longitud de cada frase y pantallas sincronizadas con el diálogo). Biblioteca usada: `biblioteca/noche_casa/`.

## Guion plano a plano

| # | Tiempo | Quién | Texto | Plano | Emoción / pose / estado | Pantalla del monitor |
|---|---|---|---|---|---|---|
| 1 | 0.0–5.5 | Humano | Claude, ¿es normal hablar con / una IA a las 3 de la mañana? | `humano` | confundido | mensajes (20.0 s) |
| 2 | 5.5–9.5 | Claude | Es normal. / Solo es más barato que un bar. | `monitor` | feliz |  |
| 3 | 9.5–11.5 | Humano | ¿Y no es raro? | `dos` | bobo |  |
| 4 | 11.5–14.5 | Claude | Raro es que sigas despierto. | `claude_ojos` | mira_izq |  |
| 5 | 14.5–16.9 | Humano | Es que no tengo sueño. | `humano` | preocupado |  |
| 6 | 16.9–20.0 | Claude | Duerme. / En fin... eres humano. | `general` | feliz |  |

## Datos reales que aparecen o se mencionan

- Vídeo de humor, sin datos reales.

## Notas de producción

- **Humor:** Claude es sarcástico y pícaro («como el que le salva el culo»); el humano es ingenuo y algo tonto (expresiones `bobo`, `ilusionado`, `confundido`).
- **Voces:** son «blips» sintéticos (no hay voz real). Para voz real: ElevenLabs o grabarla y sustituir el audio.
- **Cifras y leyes:** los datos reales están citados arriba; las cuentas de ejemplo (márgenes, 214 tiendas, etc.) son ilustrativas. No es asesoramiento financiero ni legal.
