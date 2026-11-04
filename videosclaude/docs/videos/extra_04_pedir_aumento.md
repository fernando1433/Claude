# Claude, ¿me pido un aumento?

**Archivo de guion:** `guiones/extra_04_pedir_aumento.json` · **Ambiente:** `atardecer_tienda` · **Duración:** 40 s (240 frames de animación a 6 fps)

Preparar la petición de un aumento de sueldo: argumentos buenos (logros, datos de mercado, una cifra real) y malos («mi gato lo merece»).

**Gancho (primera frase):** «Claude, ¿me pido un aumento?»

## Cómo se genera el vídeo
```bash
python3 -I motor/montar_video.py guiones/extra_04_pedir_aumento.json salidas/extra_04_pedir_aumento.mp4
```
El guion se creó con `motor/generar_guiones.py` (tiempos automáticos según la longitud de cada frase y pantallas sincronizadas con el diálogo). Biblioteca usada: `biblioteca/atardecer_tienda/`.

## Guion plano a plano

| # | Tiempo | Quién | Texto | Plano | Emoción / pose / estado | Pantalla del monitor |
|---|---|---|---|---|---|---|
| 1 | 0.0–2.8 | Humano | Claude, ¿me pido un aumento? | `humano` | ilusionado | tareas (30.26 s) |
| 2 | 2.8–4.9 | Claude | ¿Con qué argumentos? | `monitor` | mira_izq |  |
| 3 | 4.9–6.8 | Humano | Llevo tres años. | `dos` | bobo |  |
| 4 | 6.8–9.4 | Claude | Bien. ¿Y qué has logrado? | `claude_ojos` | idle |  |
| 5 | 9.4–11.8 | Humano | Asistir a las reuniones. | `humano` | confundido |  |
| 6 | 11.8–15.9 | Claude | Más bien sobrevivir. / Necesitamos resultados. | `cenital` | mira_der |  |
| 7 | 15.9–17.8 | Humano | Mi gato lo merece. | `dos` | ilusionado |  |
| 8 | 17.8–21.3 | Claude | Tu gato no negocia. / Tú, un poco peor. | `monitor` | feliz |  |
| 9 | 21.3–23.2 | Humano | ¿Y qué hago? | `humano` | preocupado |  |
| 10 | 23.2–28.8 | Claude | Lista de logros con datos, / referencias del mercado y una cifra. | `pantalla_completa` | idle |  |
| 11 | 28.8–30.7 | Humano | ¿Una cifra? ¿Cuál? | `dos` | confundido |  |
| 12 | 30.7–35.0 | Claude | Una real. Ni 3 millones / ni «lo que usted crea». | `claude_ojos` | mira_izq, empuje de cámara |  |
| 13 | 35.0–36.9 | Humano | ¡Voy a por ello! | `humano` | ilusionado |  |
| 14 | 36.9–40.0 | Claude | Y respira. / En fin... eres humano. | `general` | feliz |  |

## Datos reales que aparecen o se mencionan

- Vídeo de humor con consejos generales de negociación (logros medibles, referencias de mercado y una cifra concreta). No es asesoramiento laboral.

## Notas de producción

- **Humor:** Claude es sarcástico y pícaro («como el que le salva el culo»); el humano es ingenuo y algo tonto (expresiones `bobo`, `ilusionado`, `confundido`).
- **Voces:** son «blips» sintéticos (no hay voz real). Para voz real: ElevenLabs o grabarla y sustituir el audio.
- **Cifras y leyes:** los datos reales están citados arriba; las cuentas de ejemplo (márgenes, 214 tiendas, etc.) son ilustrativas. No es asesoramiento financiero ni legal.
