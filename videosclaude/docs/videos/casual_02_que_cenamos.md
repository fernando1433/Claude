# Claude, ¿qué ceno hoy?

**Archivo de guion:** `guiones/casual_02_que_cenamos.json` · **Ambiente:** `noche_casa` · **Duración:** 38 s (228 frames de animación a 6 fps)

El bucle eterno de «¿qué ceno?»: Claude propone, el humano rechaza todo, y acaba pidiendo la pizza de siempre 43 minutos después.

**Gancho (primera frase):** «Claude, ¿qué ceno hoy?»

## Cómo se genera el vídeo
```bash
python3 -I motor/montar_video.py guiones/casual_02_que_cenamos.json salidas/casual_02_que_cenamos.mp4
```
El guion se creó con `motor/generar_guiones.py` (tiempos automáticos según la longitud de cada frase y pantallas sincronizadas con el diálogo). Biblioteca usada: `biblioteca/noche_casa/`.

## Guion plano a plano

| # | Tiempo | Quién | Texto | Plano | Emoción / pose / estado | Pantalla del monitor |
|---|---|---|---|---|---|---|
| 1 | 0.0–2.5 | Humano | Claude, ¿qué ceno hoy? | `humano` | confundido | menu (32.85 s) |
| 2 | 2.5–4.6 | Claude | Ensalada. | `monitor` | idle |  |
| 3 | 4.6–6.7 | Humano | Ya... pero no. | `dos` | preocupado |  |
| 4 | 6.7–8.8 | Claude | Pasta. | `claude_ojos` | mira_izq |  |
| 5 | 8.8–10.9 | Humano | Comí pasta ayer. | `humano` | bobo |  |
| 6 | 10.9–13.0 | Claude | Sushi. | `cenital` | mira_der |  |
| 7 | 13.0–15.1 | Humano | Es caro. | `dos` | confundido |  |
| 8 | 15.1–17.2 | Claude | Tortilla. | `monitor` | feliz |  |
| 9 | 17.2–19.3 | Humano | Me da pereza. | `humano` | preocupado |  |
| 10 | 19.3–23.9 | Claude | Llevamos 43 minutos. / ¿Qué tienes en la nevera? | `claude_ojos` | mira_arriba |  |
| 11 | 23.9–26.8 | Humano | Una cebolla y medio limón. | `dos` | bobo |  |
| 12 | 26.8–31.2 | Claude | Pide una pizza. / La elegiste hace 43 minutos. | `pantalla_completa` | idle |  |
| 13 | 31.2–33.4 | Humano | ¡Pizza! ¡Qué idea! | `humano` | ilusionado |  |
| 14 | 33.4–38.0 | Claude | Mía no fue, por cierto. / En fin... eres humano. | `general` | feliz |  |

## Datos reales que aparecen o se mencionan

- Vídeo de humor, sin datos reales.

## Notas de producción

- **Humor:** Claude es sarcástico y pícaro («como el que le salva el culo»); el humano es ingenuo y algo tonto (expresiones `bobo`, `ilusionado`, `confundido`).
- **Voces:** son «blips» sintéticos (no hay voz real). Para voz real: ElevenLabs o grabarla y sustituir el audio.
- **Cifras y leyes:** los datos reales están citados arriba; las cuentas de ejemplo (márgenes, 214 tiendas, etc.) son ilustrativas. No es asesoramiento financiero ni legal.
