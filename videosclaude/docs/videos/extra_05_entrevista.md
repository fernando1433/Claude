# Claude, mañana tengo una entrevista de trabajo

**Archivo de guion:** `guiones/extra_05_entrevista.json` · **Ambiente:** `dia_casa` · **Duración:** 38 s (228 frames de animación a 6 fps)

Simulacro de entrevista: «háblame de ti», el defecto «perfeccionista» y el logro de llegar a tiempo cuatro días seguidos.

**Gancho (primera frase):** «Claude, mañana tengo una entrevista de trabajo.»

## Cómo se genera el vídeo
```bash
python3 -I motor/montar_video.py guiones/extra_05_entrevista.json salidas/extra_05_entrevista.mp4
```
El guion se creó con `motor/generar_guiones.py` (tiempos automáticos según la longitud de cada frase y pantallas sincronizadas con el diálogo). Biblioteca usada: `biblioteca/dia_casa/`.

## Guion plano a plano

| # | Tiempo | Quién | Texto | Plano | Emoción / pose / estado | Pantalla del monitor |
|---|---|---|---|---|---|---|
| 1 | 0.0–3.9 | Humano | Claude, mañana tengo una / entrevista de trabajo. | `humano` | preocupado | mensajes (38.0 s) |
| 2 | 3.9–6.4 | Claude | Empecemos. / «Háblame de ti». | `monitor` | idle |  |
| 3 | 6.4–8.2 | Humano | Soy muy... humano. | `dos` | bobo |  |
| 4 | 8.2–9.9 | Claude | No. Eso no. | `claude_ojos` | mira_izq |  |
| 5 | 9.9–11.8 | Humano | ¿Mi mayor defecto? | `humano` | confundido |  |
| 6 | 11.8–16.0 | Claude | No digas «soy demasiado / perfeccionista». Lo huelen. | `cenital` | mira_der |  |
| 7 | 16.0–18.2 | Humano | Que me cuesta madrugar. | `dos` | preocupado |  |
| 8 | 18.2–22.6 | Claude | Honesto, pero peligroso. / Di algo real que ya mejoras. | `monitor` | feliz |  |
| 9 | 22.6–24.4 | Humano | ¿Mi mayor logro? | `humano` | ilusionado |  |
| 10 | 24.4–26.9 | Claude | Uno medible. Con un número. | `claude_ojos` | idle, empuje de cámara |  |
| 11 | 26.9–29.7 | Humano | Llegué a tiempo 4 días seguidos. | `dos` | bobo |  |
| 12 | 29.7–32.3 | Claude | Eso... guárdalo / para el café. | `pantalla_completa` | idle |  |
| 13 | 32.3–34.1 | Humano | ¡Voy a arrasar! | `humano` | feliz |  |
| 14 | 34.1–38.0 | Claude | Con calma. Y con camisa. / En fin... eres humano. | `general` | feliz |  |

## Datos reales que aparecen o se mencionan

- Vídeo de humor con consejos generales de entrevista (respuestas concretas y honestas con ejemplos medibles). No es asesoramiento laboral.

## Notas de producción

- **Humor:** Claude es sarcástico y pícaro («como el que le salva el culo»); el humano es ingenuo y algo tonto (expresiones `bobo`, `ilusionado`, `confundido`).
- **Voces:** son «blips» sintéticos (no hay voz real). Para voz real: ElevenLabs o grabarla y sustituir el audio.
- **Cifras y leyes:** los datos reales están citados arriba; las cuentas de ejemplo (márgenes, 214 tiendas, etc.) son ilustrativas. No es asesoramiento financiero ni legal.
