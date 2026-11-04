# Claude, ¿cinco minutos más?

**Archivo de guion:** `guiones/casual_08_cinco_minutos.json` · **Ambiente:** `dia_casa` · **Duración:** 36 s (216 frames de animación a 6 fps)

El despertador y el «cinco minutos más»: Claude lleva la cuenta de las veces que se ha pospuesto.

**Gancho (primera frase):** «Claude... ¿cinco minutos más?»

## Cómo se genera el vídeo
```bash
python3 -I motor/montar_video.py guiones/casual_08_cinco_minutos.json salidas/casual_08_cinco_minutos.mp4
```
El guion se creó con `motor/generar_guiones.py` (tiempos automáticos según la longitud de cada frase y pantallas sincronizadas con el diálogo). Biblioteca usada: `biblioteca/dia_casa/`.

## Guion plano a plano

| # | Tiempo | Quién | Texto | Plano | Emoción / pose / estado | Pantalla del monitor |
|---|---|---|---|---|---|---|
| 1 | 0.0–2.9 | Humano | Claude... ¿cinco minutos más? | `humano` | bobo | recordatorios (21.4 s) |
| 2 | 2.9–6.0 | Claude | Es la cuarta vez que / me lo pides. | `monitor` | mira_izq |  |
| 3 | 6.0–8.5 | Humano | Es que hoy es distinto. | `dos` | confundido |  |
| 4 | 8.5–11.7 | Claude | Dijiste lo mismo ayer. / Y el lunes. | `claude_ojos` | idle |  |
| 5 | 11.7–13.7 | Humano | Mi cama me quiere. | `humano` | ilusionado |  |
| 6 | 13.7–17.7 | Claude | Tu cama no tiene opinión. / La tiene tu jefe. | `cenital` | mira_der |  |
| 7 | 17.7–20.3 | Humano | Cinco minutos. Solo cinco. | `dos` | bobo |  |
| 8 | 20.3–23.6 | Claude | Cinco minutos de verdad. / Yo cuento. | `pantalla_completa` | idle |  |
| 9 | 23.6–25.8 | Humano | ...Qué rápido pasan. | `humano` | preocupado |  |
| 10 | 25.8–28.8 | Claude | Ya te lo dije. / Levántate, anda. | `claude_ojos` | feliz |  |
| 11 | 28.8–31.5 | Humano | Vale. Pero primero un café. | `dos` | feliz |  |
| 12 | 31.5–36.0 | Claude | Primero los pies al suelo. / En fin... eres humano. | `general` | feliz |  |

## Datos reales que aparecen o se mencionan

- Vídeo de humor, sin datos reales.

## Notas de producción

- **Humor:** Claude es sarcástico y pícaro («como el que le salva el culo»); el humano es ingenuo y algo tonto (expresiones `bobo`, `ilusionado`, `confundido`).
- **Voces:** son «blips» sintéticos (no hay voz real). Para voz real: ElevenLabs o grabarla y sustituir el audio.
- **Cifras y leyes:** los datos reales están citados arriba; las cuentas de ejemplo (márgenes, 214 tiendas, etc.) son ilustrativas. No es asesoramiento financiero ni legal.
