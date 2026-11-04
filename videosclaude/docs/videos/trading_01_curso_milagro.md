# El curso milagro

**Archivo de guion:** `guiones/trading_01_curso_milagro.json` · **Ambiente:** `noche_trading` · **Duración:** 45 s (270 frames de animación a 6 fps)

El trader quiere ser millonario en 7 días con un curso de 997 €. Claude le va desmontando el anuncio (contador falso, testimonios de stock, «garantizado») y, cuando el tonto va a pagar, le bloquea el pago.

## Cómo se genera el vídeo
```bash
python3 -I motor/montar_video.py guiones/trading_01_curso_milagro.json salidas/trading_01_curso_milagro.mp4
```
El guion se creó con `motor/generar_guiones.py` (tiempos automáticos según la longitud de cada frase y pantallas sincronizadas con el diálogo). Biblioteca usada: `biblioteca/noche_trading/`.

## Guion plano a plano

| # | Tiempo | Quién | Texto | Plano | Emoción / pose / estado | Pantalla del monitor |
|---|---|---|---|---|---|---|
| 1 | 0.0–3.1 | Humano | ¡Voy a ser millonario! / Me apunté a un curso. | `general` | ilusionado | curso (36.47 s) |
| 2 | 3.1–4.8 | Claude | Ah, ¿sí? Enséñamelo. | `monitor` | mira_izq |  |
| 3 | 4.8–7.5 | Humano | «Millonario en 7 días». / ¡Solo 997 €! | `dos` | feliz, pose senalar |  |
| 4 | 7.5–11.4 | Claude | Si funcionara, no lo vendería: / estaría contando billetes. | `monitor` | feliz |  |
| 5 | 11.4–13.1 | Humano | Pero tiene un Lambo. | `humano` | bobo |  |
| 6 | 13.1–16.4 | Claude | Alquilado. Y el contador / se reinicia cada vez. | `monitor` | idle |  |
| 7 | 16.4–18.0 | Humano | ¿Y los testimonios? | `dos` | confundido |  |
| 8 | 18.0–22.0 | Claude | Fotos de stock. «Carlos, 24» / es dentista en otro anuncio. | `claude_ojos` | feliz, empuje de cámara |  |
| 9 | 22.0–25.9 | Claude | Dato real: 74–89 % de cuentas / minoristas de CFD pierde. | `pantalla_completa` | idle | verdad (3.86 s) |
| 10 | 25.9–27.6 | Humano | Pero yo soy del 11 %. | `humano` | bobo |  |
| 11 | 27.6–30.6 | Claude | Todos creen ser del 11 %. / El 89 % también. | `cenital` | mira_arriba |  |
| 12 | 30.6–32.4 | Humano | Pues lo compro igual. | `dos` | ilusionado | checkout (3.26 s) |
| 13 | 32.4–34.2 | Claude | Pago bloqueado. / De nada. | `pantalla_completa` | idle |  |
| 14 | 34.2–35.7 | Humano | ¡Era mi dinero! | `humano` | preocupado, pose hombros |  |
| 15 | 35.7–39.0 | Claude | Y lo sigue siendo. / A eso se le llama ahorrar. | `monitor` | feliz |  |
| 16 | 39.0–41.6 | Humano | ¡Mira, otro! ¡Millonario en 3 días! | `humano` | ilusionado | curso (3.5 s) |
| 17 | 41.6–45.0 | Claude | Mismo PDF, menos páginas. / En fin... eres humano. | `general` | feliz |  |

## Datos reales que aparecen o se mencionan

- 74–89 % de las cuentas minoristas de CFD pierden dinero (cifra de las advertencias de riesgo obligatorias que fijó ESMA en 2018; porcentaje de cuentas, no probabilidad individual).
  - Fuente: [ESMA (2018): prohíbe las opciones binarias y restringe los CFD a minoristas](https://www.esma.europa.eu/node/84933)
  - Fuente: [ESMA: renovación de las restricciones a los CFD](https://www.esma.europa.eu/press-news/esma-news/esma-renew-restriction-cfds-further-three-months)

## Notas de producción

- **Humor:** Claude es sarcástico y pícaro («como el que le salva el culo»); el humano es ingenuo y algo tonto (expresiones `bobo`, `ilusionado`, `confundido`).
- **Voces:** son «blips» sintéticos (no hay voz real). Para voz real: ElevenLabs o grabarla y sustituir el audio.
- **Cifras y leyes:** los datos reales están citados arriba; las cuentas de ejemplo (márgenes, 214 tiendas, etc.) son ilustrativas. No es asesoramiento financiero ni legal.
