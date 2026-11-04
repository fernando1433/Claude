# Claude, ¿por qué existen los lunes?

**Archivo de guion:** `guiones/casual_09_los_lunes.json` · **Ambiente:** `dia_casa` · **Duración:** 36 s (216 frames de animación a 6 fps)

Queja filosófica del lunes por la mañana, con respuestas secas de Claude.

**Gancho (primera frase):** «Claude, ¿por qué existen los lunes?»

## Cómo se genera el vídeo
```bash
python3 -I motor/montar_video.py guiones/casual_09_los_lunes.json salidas/casual_09_los_lunes.mp4
```
El guion se creó con `motor/generar_guiones.py` (tiempos automáticos según la longitud de cada frase y pantallas sincronizadas con el diálogo). Biblioteca usada: `biblioteca/dia_casa/`.

## Guion plano a plano

| # | Tiempo | Quién | Texto | Plano | Emoción / pose / estado | Pantalla del monitor |
|---|---|---|---|---|---|---|
| 1 | 0.0–3.1 | Humano | Claude, ¿por qué existen / los lunes? | `humano` | preocupado | calendario (20.11 s) |
| 2 | 3.1–5.7 | Claude | Porque antes hay un domingo. | `monitor` | idle |  |
| 3 | 5.7–7.8 | Humano | ¿Y no se puede quitar? | `dos` | bobo |  |
| 4 | 7.8–11.8 | Claude | Quitamos el lunes y / el martes pasa a ser lunes. | `claude_ojos` | mira_izq |  |
| 5 | 11.8–14.4 | Humano | Entonces quitamos los martes. | `humano` | ilusionado |  |
| 6 | 14.4–19.1 | Claude | Y el miércoles. Ya tienes / el mismo problema, más barato. | `pantalla_completa` | idle |  |
| 7 | 19.1–21.8 | Humano | Odio las reuniones del lunes. | `dos` | preocupado |  |
| 8 | 21.8–25.1 | Claude | Esa reunión podía ser / un correo. Lo sé. | `cenital` | mira_der |  |
| 9 | 25.1–27.1 | Humano | ¿Entonces qué hago? | `humano` | confundido |  |
| 10 | 27.1–30.2 | Claude | Café, paciencia y / una reunión menos. | `monitor` | feliz |  |
| 11 | 30.2–31.9 | Humano | Eres un sabio. | `dos` | ilusionado |  |
| 12 | 31.9–36.0 | Claude | Soy un lunes con teclado. / En fin... eres humano. | `general` | feliz |  |

## Datos reales que aparecen o se mencionan

- Vídeo de humor, sin datos reales.

## Notas de producción

- **Humor:** Claude es sarcástico y pícaro («como el que le salva el culo»); el humano es ingenuo y algo tonto (expresiones `bobo`, `ilusionado`, `confundido`).
- **Voces:** son «blips» sintéticos (no hay voz real). Para voz real: ElevenLabs o grabarla y sustituir el audio.
- **Cifras y leyes:** los datos reales están citados arriba; las cuentas de ejemplo (márgenes, 214 tiendas, etc.) son ilustrativas. No es asesoramiento financiero ni legal.
