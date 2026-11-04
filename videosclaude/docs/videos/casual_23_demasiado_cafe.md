# Claude, ¿cuántos cafés son demasiados?

**Archivo de guion:** `guiones/casual_23_demasiado_cafe.json` · **Ambiente:** `dia_casa` · **Duración:** 36 s (216 frames de animación a 6 fps)

La pregunta que nadie quiere responder: ya vas por el sexto café.

**Gancho (primera frase):** «Claude, ¿cuántos cafés son demasiados?»

## Cómo se genera el vídeo
```bash
python3 -I motor/montar_video.py guiones/casual_23_demasiado_cafe.json salidas/casual_23_demasiado_cafe.mp4
```
El guion se creó con `motor/generar_guiones.py` (tiempos automáticos según la longitud de cada frase y pantallas sincronizadas con el diálogo). Biblioteca usada: `biblioteca/dia_casa/`.

## Guion plano a plano

| # | Tiempo | Quién | Texto | Plano | Emoción / pose / estado | Pantalla del monitor |
|---|---|---|---|---|---|---|
| 1 | 0.0–4.3 | Humano | Claude, ¿cuántos cafés / son demasiados? | `humano` | confundido | recordatorios (26.13 s) |
| 2 | 4.3–6.9 | Claude | ¿Cuántos llevas hoy? | `monitor` | mira_izq |  |
| 3 | 6.9–9.2 | Humano | Seis. | `dos` | bobo |  |
| 4 | 9.2–11.5 | Claude | Pues ya lo sabes. | `claude_ojos` | feliz |  |
| 5 | 11.5–14.1 | Humano | Pero no tengo sueño. | `humano` | ilusionado |  |
| 6 | 14.1–18.6 | Claude | Tampoco tienes calma. / Te tiembla la mano. | `cenital` | mira_der |  |
| 7 | 18.6–20.9 | Humano | Es la emoción. | `dos` | preocupado |  |
| 8 | 20.9–24.8 | Claude | Es el café. Bebe agua. / Y siéntate. | `pantalla_completa` | idle |  |
| 9 | 24.8–27.1 | Humano | ¿Un descafeinado? | `humano` | bobo |  |
| 10 | 27.1–30.1 | Claude | Eso. Con mucha dignidad. | `monitor` | feliz |  |
| 11 | 30.1–32.4 | Humano | Gracias, Claude. | `dos` | feliz |  |
| 12 | 32.4–36.0 | Claude | De nada. / En fin... eres humano. | `general` | feliz |  |

## Datos reales que aparecen o se mencionan

- Vídeo de humor, sin datos reales.

## Notas de producción

- **Humor:** Claude es sarcástico y pícaro («como el que le salva el culo»); el humano es ingenuo y algo tonto (expresiones `bobo`, `ilusionado`, `confundido`).
- **Voces:** son «blips» sintéticos (no hay voz real). Para voz real: ElevenLabs o grabarla y sustituir el audio.
- **Cifras y leyes:** los datos reales están citados arriba; las cuentas de ejemplo (márgenes, 214 tiendas, etc.) son ilustrativas. No es asesoramiento financiero ni legal.
