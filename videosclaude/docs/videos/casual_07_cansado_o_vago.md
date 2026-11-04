# Claude, ¿estoy cansado o soy vago?

**Archivo de guion:** `guiones/casual_07_cansado_o_vago.json` · **Ambiente:** `dia_casa` · **Duración:** 36 s (216 frames de animación a 6 fps)

Domingo por la tarde: nueve horas dormidas, pijama a las tres y el sofá que le saluda. Claude dicta sentencia con cariño.

**Gancho (primera frase):** «Claude, ¿estoy cansado o soy vago?»

## Cómo se genera el vídeo
```bash
python3 -I motor/montar_video.py guiones/casual_07_cansado_o_vago.json salidas/casual_07_cansado_o_vago.mp4
```
El guion se creó con `motor/generar_guiones.py` (tiempos automáticos según la longitud de cada frase y pantallas sincronizadas con el diálogo). Biblioteca usada: `biblioteca/dia_casa/`.

## Guion plano a plano

| # | Tiempo | Quién | Texto | Plano | Emoción / pose / estado | Pantalla del monitor |
|---|---|---|---|---|---|---|
| 1 | 0.0–3.6 | Humano | Claude, ¿estoy cansado / o soy vago? | `humano` | confundido | recordatorios (24.19 s) |
| 2 | 3.6–5.8 | Claude | Datos, por favor. | `monitor` | idle |  |
| 3 | 5.8–8.2 | Humano | He dormido 9 horas. | `dos` | bobo |  |
| 4 | 8.2–10.3 | Claude | Ajá. | `claude_ojos` | mira_izq |  |
| 5 | 10.3–13.4 | Humano | Son las 3 y sigo en pijama. | `humano` | preocupado |  |
| 6 | 13.4–15.6 | Claude | Ajá. | `cenital` | mira_der |  |
| 7 | 15.6–19.1 | Humano | El sofá me saluda por mi nombre. | `dos` | confundido |  |
| 8 | 19.1–23.0 | Claude | Vago. Con mucha dignidad, / pero vago. | `pantalla_completa` | idle |  |
| 9 | 23.0–26.6 | Humano | ¡Qué alivio! Pensé que era grave. | `humano` | ilusionado |  |
| 10 | 26.6–30.5 | Claude | Grave sería no tener sofá. / Descansa. | `monitor` | feliz |  |
| 11 | 30.5–32.6 | Humano | Gracias. | `dos` | feliz |  |
| 12 | 32.6–36.0 | Claude | De nada. / En fin... eres humano. | `general` | feliz |  |

## Datos reales que aparecen o se mencionan

- Vídeo de humor, sin datos reales.

## Notas de producción

- **Humor:** Claude es sarcástico y pícaro («como el que le salva el culo»); el humano es ingenuo y algo tonto (expresiones `bobo`, `ilusionado`, `confundido`).
- **Voces:** son «blips» sintéticos (no hay voz real). Para voz real: ElevenLabs o grabarla y sustituir el audio.
- **Cifras y leyes:** los datos reales están citados arriba; las cuentas de ejemplo (márgenes, 214 tiendas, etc.) son ilustrativas. No es asesoramiento financiero ni legal.
