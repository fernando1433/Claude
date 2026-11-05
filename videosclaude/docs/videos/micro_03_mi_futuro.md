# Claude, ¿cómo será mi futuro?

![vista previa](img/micro_03_mi_futuro.jpg)

**Archivo de guion:** `guiones/micro_03_mi_futuro.json` · **Ambiente:** `atardecer_casa` · **Duración:** 20 s (120 frames de animación a 6 fps)

Micro-vídeo de humor de ~20 s, sin datos reales.

**Gancho (primera frase):** «Claude, ¿cómo será mi futuro?»

## Cómo se genera el vídeo
```bash
python3 -I motor/montar_video.py guiones/micro_03_mi_futuro.json salidas/micro_03_mi_futuro.mp4
```
El guion se creó con `motor/generar_guiones.py` (tiempos automáticos según la longitud de cada frase y pantallas sincronizadas con el diálogo). Biblioteca usada: `biblioteca/atardecer_casa/`.

## Guion plano a plano

| # | Tiempo | Quién | Texto | Plano | Emoción / pose / estado | Pantalla del monitor |
|---|---|---|---|---|---|---|
| 1 | 0.0–3.4 | Humano | Claude, ¿cómo será mi futuro? | `humano` | confundido | mensajes (20.0 s) |
| 2 | 3.4–6.7 | Claude | Depende de lo que hagas hoy. | `monitor` | mira_izq |  |
| 3 | 6.7–9.6 | Humano | ¿Y qué voy a hacer hoy? | `dos` | bobo |  |
| 4 | 9.6–12.7 | Claude | El sofá. Lo veo clarísimo. | `claude_ojos` | feliz |  |
| 5 | 12.7–16.2 | Humano | Entonces mi futuro es el sofá. | `humano` | preocupado |  |
| 6 | 16.2–20.0 | Claude | Con extras. / En fin... eres humano. | `general` | feliz |  |

## Datos reales que aparecen o se mencionan

- Vídeo de humor, sin datos reales.

## Notas de producción

- **Humor:** Claude es sarcástico y pícaro («como el que le salva el culo»); el humano es ingenuo y algo tonto (expresiones `bobo`, `ilusionado`, `confundido`).
- **Voces:** son «blips» sintéticos (no hay voz real). Para voz real: ElevenLabs o grabarla y sustituir el audio.
- **Cifras y leyes:** los datos reales están citados arriba; las cuentas de ejemplo (márgenes, 214 tiendas, etc.) son ilustrativas. No es asesoramiento financiero ni legal.
