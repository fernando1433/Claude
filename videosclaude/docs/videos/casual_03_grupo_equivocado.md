# He mandado un audio al grupo equivocado

**Archivo de guion:** `guiones/casual_03_grupo_equivocado.json` · **Ambiente:** `dia_casa` · **Duración:** 40 s (240 frames de animación a 6 fps)

Desastre cotidiano: un audio sobre el jefe enviado al grupo del trabajo. Claude hace control de daños con dignidad.

**Gancho (primera frase):** «¡Claude! He mandado un audio al grupo equivocado.»

## Cómo se genera el vídeo
```bash
python3 -I motor/montar_video.py guiones/casual_03_grupo_equivocado.json salidas/casual_03_grupo_equivocado.mp4
```
El guion se creó con `motor/generar_guiones.py` (tiempos automáticos según la longitud de cada frase y pantallas sincronizadas con el diálogo). Biblioteca usada: `biblioteca/dia_casa/`.

## Guion plano a plano

| # | Tiempo | Quién | Texto | Plano | Emoción / pose / estado | Pantalla del monitor |
|---|---|---|---|---|---|---|
| 1 | 0.0–4.1 | Humano | ¡Claude! He mandado un audio / al grupo equivocado. | `humano` | preocupado | mensajes (19.88 s) |
| 2 | 4.1–6.0 | Claude | ¿Qué decía el audio? | `monitor` | mira_izq |  |
| 3 | 6.0–9.6 | Humano | Que mi jefe es un ser de luz / con poca luz. | `dos` | bobo |  |
| 4 | 9.6–12.3 | Claude | Qué poético. / ¿Quién lo ha visto? | `claude_ojos` | feliz, empuje de cámara |  |
| 5 | 12.3–14.2 | Humano | Catorce. Y el jefe. | `humano` | preocupado |  |
| 6 | 14.2–17.3 | Claude | Vale. Respira. / Borra para todos. Ya. | `monitor` | idle |  |
| 7 | 17.3–19.9 | Humano | Ya lo escucharon tres veces. | `dos` | preocupado, pose hombros |  |
| 8 | 19.9–23.3 | Claude | Entonces la única salida / es la dignidad. | `cenital` | mira_der |  |
| 9 | 23.3–25.0 | Humano | ¿Qué hago? | `humano` | confundido |  |
| 10 | 25.0–29.7 | Claude | Escribe: «Era un ensayo de teatro». / Y no añadas nada más. | `monitor` | feliz |  |
| 11 | 29.7–31.4 | Humano | ¿Y cuela? | `dos` | bobo |  |
| 12 | 31.4–34.3 | Claude | No. Pero queda digno. / Tú aguanta. | `claude_ojos` | mira_izq |  |
| 13 | 34.3–36.0 | Humano | Gracias, Claude. | `humano` | feliz |  |
| 14 | 36.0–40.0 | Claude | A ti, y a ese ser de luz. / En fin... eres humano. | `general` | feliz |  |

## Datos reales que aparecen o se mencionan

- Vídeo de humor, sin datos reales.

## Notas de producción

- **Humor:** Claude es sarcástico y pícaro («como el que le salva el culo»); el humano es ingenuo y algo tonto (expresiones `bobo`, `ilusionado`, `confundido`).
- **Voces:** son «blips» sintéticos (no hay voz real). Para voz real: ElevenLabs o grabarla y sustituir el audio.
- **Cifras y leyes:** los datos reales están citados arriba; las cuentas de ejemplo (márgenes, 214 tiendas, etc.) son ilustrativas. No es asesoramiento financiero ni legal.
