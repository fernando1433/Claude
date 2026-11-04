# Claude, no tengo nada que ponerme

**Archivo de guion:** `guiones/casual_24_nada_que_ponerme.json` · **Ambiente:** `noche_casa` · **Duración:** 36 s (216 frames de animación a 6 fps)

El armario lleno y la ropa que «no combina con pereza».

**Gancho (primera frase):** «Claude, no tengo nada que ponerme.»

## Cómo se genera el vídeo
```bash
python3 -I motor/montar_video.py guiones/casual_24_nada_que_ponerme.json salidas/casual_24_nada_que_ponerme.mp4
```
El guion se creó con `motor/generar_guiones.py` (tiempos automáticos según la longitud de cada frase y pantallas sincronizadas con el diálogo). Biblioteca usada: `biblioteca/noche_casa/`.

## Guion plano a plano

| # | Tiempo | Quién | Texto | Plano | Emoción / pose / estado | Pantalla del monitor |
|---|---|---|---|---|---|---|
| 1 | 0.0–3.6 | Humano | Claude, no tengo nada / que ponerme. | `humano` | preocupado | mensajes (36.0 s) |
| 2 | 3.6–6.7 | Claude | Tu armario tiene 83 prendas. | `monitor` | mira_izq |  |
| 3 | 6.7–8.8 | Humano | Ninguna combina. | `dos` | bobo |  |
| 4 | 8.8–10.9 | Claude | ¿Con qué? | `claude_ojos` | idle |  |
| 5 | 10.9–13.2 | Humano | Con «me da pereza». | `humano` | confundido |  |
| 6 | 13.2–18.0 | Claude | Pues ponte la sudadera verde. / Combina con todo. | `cenital` | mira_der |  |
| 7 | 18.0–20.8 | Humano | Es la que llevo siempre. | `dos` | ilusionado |  |
| 8 | 20.8–23.4 | Claude | Y por eso te sale bien. | `monitor` | feliz |  |
| 9 | 23.4–25.5 | Humano | ¿Y si hace calor? | `humano` | preocupado |  |
| 10 | 25.5–29.8 | Claude | Entonces sudadera, pero / con más dignidad. | `claude_ojos` | mira_arriba, empuje de cámara |  |
| 11 | 29.8–31.9 | Humano | Vale. La verde. | `dos` | feliz |  |
| 12 | 31.9–36.0 | Claude | Siempre la verde. / En fin... eres humano. | `general` | feliz |  |

## Datos reales que aparecen o se mencionan

- Vídeo de humor, sin datos reales.

## Notas de producción

- **Humor:** Claude es sarcástico y pícaro («como el que le salva el culo»); el humano es ingenuo y algo tonto (expresiones `bobo`, `ilusionado`, `confundido`).
- **Voces:** son «blips» sintéticos (no hay voz real). Para voz real: ElevenLabs o grabarla y sustituir el audio.
- **Cifras y leyes:** los datos reales están citados arriba; las cuentas de ejemplo (márgenes, 214 tiendas, etc.) son ilustrativas. No es asesoramiento financiero ni legal.
