# Claude, ¿he apagado el horno?

![vista previa](img/micro_01_el_horno.jpg)

**Archivo de guion:** `guiones/micro_01_el_horno.json` · **Ambiente:** `noche_casa` · **Duración:** 20 s (120 frames de animación a 6 fps)

Micro-vídeo de humor de ~20 s, sin datos reales.

**Gancho (primera frase):** «Claude, ¿he apagado el horno?»

## Cómo se genera el vídeo
```bash
python3 -I motor/montar_video.py guiones/micro_01_el_horno.json salidas/micro_01_el_horno.mp4
```
El guion se creó con `motor/generar_guiones.py` (tiempos automáticos según la longitud de cada frase y pantallas sincronizadas con el diálogo). Biblioteca usada: `biblioteca/noche_casa/`.

## Guion plano a plano

| # | Tiempo | Quién | Texto | Plano | Emoción / pose / estado | Pantalla del monitor |
|---|---|---|---|---|---|---|
| 1 | 0.0–3.4 | Humano | Claude, ¿he apagado el horno? | `humano` | preocupado | mensajes (20.0 s) |
| 2 | 3.4–6.5 | Claude | No tengo ojos en tu cocina. | `monitor` | mira_izq |  |
| 3 | 6.5–9.2 | Humano | Pero tú lo sabes todo. | `dos` | bobo |  |
| 4 | 9.2–13.2 | Claude | Sé muchas cosas. / El horno no es una. | `claude_ojos` | feliz |  |
| 5 | 13.2–15.4 | Humano | Voy a mirar. | `humano` | preocupado |  |
| 6 | 15.4–20.0 | Claude | Y de paso, relájate. / En fin... eres humano. | `general` | feliz |  |

## Datos reales que aparecen o se mencionan

- Vídeo de humor, sin datos reales.

## Notas de producción

- **Humor:** Claude es sarcástico y pícaro («como el que le salva el culo»); el humano es ingenuo y algo tonto (expresiones `bobo`, `ilusionado`, `confundido`).
- **Voces:** son «blips» sintéticos (no hay voz real). Para voz real: ElevenLabs o grabarla y sustituir el audio.
- **Cifras y leyes:** los datos reales están citados arriba; las cuentas de ejemplo (márgenes, 214 tiendas, etc.) son ilustrativas. No es asesoramiento financiero ni legal.
