# Mi cuñado dice que compre esta moneda

**Archivo de guion:** `guiones/trading_04_el_cunado.json` · **Ambiente:** `dia_trading` · **Duración:** 44 s (264 frames de animación a 6 fps)

El «cuñado experto» recomienda una criptomoneda que nadie conoce. Claude le hace las preguntas que el cuñado no responde y le enseña una regla simple: no inviertas en lo que no entiendes ni dinero que no puedas perder.

**Gancho (primera frase):** «Claude, mi cuñado dice que compre esta moneda.»

## Cómo se genera el vídeo
```bash
python3 -I motor/montar_video.py guiones/trading_04_el_cunado.json salidas/trading_04_el_cunado.mp4
```
El guion se creó con `motor/generar_guiones.py` (tiempos automáticos según la longitud de cada frase y pantallas sincronizadas con el diálogo). Biblioteca usada: `biblioteca/dia_trading/`.

## Guion plano a plano

| # | Tiempo | Quién | Texto | Plano | Emoción / pose / estado | Pantalla del monitor |
|---|---|---|---|---|---|---|
| 1 | 0.0–3.3 | Humano | Claude, mi cuñado dice que / compre esta moneda. | `humano` | ilusionado | telegram (10.25 s) |
| 2 | 3.3–5.3 | Claude | ¿Tu cuñado es financiero? | `monitor` | mira_izq |  |
| 3 | 5.3–7.8 | Humano | Trabaja en el taller de su primo. | `dos` | bobo |  |
| 4 | 7.8–10.2 | Claude | Ya. ¿Y la moneda cómo se llama? | `claude_ojos` | idle |  |
| 5 | 10.2–12.0 | Humano | «Perrolambo Inu Max». | `humano` | ilusionado | cartera (14.69 s) |
| 6 | 12.0–14.7 | Claude | Suena a estornudo con / logo de perro. | `monitor` | feliz |  |
| 7 | 14.7–16.4 | Humano | Él ya ganó con ella. | `dos` | ilusionado |  |
| 8 | 16.4–19.8 | Claude | Según él. Y en la cena / las ganancias se hinchan. | `cenital` | mira_der |  |
| 9 | 19.8–21.3 | Humano | ¿Y si sube? | `humano` | bobo |  |
| 10 | 21.3–24.2 | Claude | Y si cae, tú pierdes / y él «ya te avisó». | `pantalla_completa` | idle |  |
| 11 | 24.2–26.1 | Humano | ¿Qué pregunto entonces? | `dos` | confundido |  |
| 12 | 26.1–30.3 | Claude | Quién la creó, qué problema / resuelve y cuánto puedes perder. | `claude_ojos` | idle, empuje de cámara |  |
| 13 | 30.3–32.1 | Humano | Ese no lo sabe nadie. | `humano` | preocupado |  |
| 14 | 32.1–34.3 | Claude | Pues ya tienes tu respuesta. | `monitor` | mira_arriba |  |
| 15 | 34.3–35.8 | Humano | ¿Y mi dinero? | `dos` | confundido |  |
| 16 | 35.8–39.3 | Claude | En lo que entiendas. / Y solo el que puedas perder. | `pantalla_completa` | idle | verdad (3.5 s) |
| 17 | 39.3–41.1 | Humano | Se lo diré a mi cuñado. | `humano` | feliz |  |
| 18 | 41.1–44.0 | Claude | No te hará caso. / En fin... eres humano. | `general` | feliz |  |

## Datos reales que aparecen o se mencionan

- Aviso de riesgo general: las inversiones pueden perder valor, y los productos complejos (CFD, criptoactivos apalancados) tienen restricciones para minoristas en la UE. Recomendación de sentido común, no asesoramiento financiero.
  - Fuente: [ESMA (2018): prohíbe las opciones binarias y restringe los CFD a minoristas](https://www.esma.europa.eu/node/84933)
- Dato citado: 74–89 % de cuentas minoristas de CFD pierde dinero (ESMA, 2018).
  - Fuente: [ESMA (2018): prohíbe las opciones binarias y restringe los CFD a minoristas](https://www.esma.europa.eu/node/84933)
  - Fuente: [ESMA: renovación de las restricciones a los CFD](https://www.esma.europa.eu/press-news/esma-news/esma-renew-restriction-cfds-further-three-months)

## Notas de producción

- **Humor:** Claude es sarcástico y pícaro («como el que le salva el culo»); el humano es ingenuo y algo tonto (expresiones `bobo`, `ilusionado`, `confundido`).
- **Voces:** son «blips» sintéticos (no hay voz real). Para voz real: ElevenLabs o grabarla y sustituir el audio.
- **Cifras y leyes:** los datos reales están citados arriba; las cuentas de ejemplo (márgenes, 214 tiendas, etc.) son ilustrativas. No es asesoramiento financiero ni legal.
