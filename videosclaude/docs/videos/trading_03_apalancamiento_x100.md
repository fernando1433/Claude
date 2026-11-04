# Apalancamiento x100

**Archivo de guion:** `guiones/trading_03_apalancamiento_x100.json` · **Ambiente:** `dia_trading` · **Duración:** 45 s (270 frames de animación a 6 fps)

El trader quiere meter 500 € a x100 «porque si sube un 1 % gana 500 €». Claude le enseña la otra cara: si baja un 1 %, liquidado. Y le explica los límites de la UE y la regla de arriesgar poco por operación.

**Gancho (primera frase):** «¡Pongo mis 500 € a x100!»

## Cómo se genera el vídeo
```bash
python3 -I motor/montar_video.py guiones/trading_03_apalancamiento_x100.json salidas/trading_03_apalancamiento_x100.mp4
```
El guion se creó con `motor/generar_guiones.py` (tiempos automáticos según la longitud de cada frase y pantallas sincronizadas con el diálogo). Biblioteca usada: `biblioteca/dia_trading/`.

## Guion plano a plano

| # | Tiempo | Quién | Texto | Plano | Emoción / pose / estado | Pantalla del monitor |
|---|---|---|---|---|---|---|
| 1 | 0.0–1.7 | Humano | ¡Pongo mis 500 € a x100! | `dos` | feliz, pose senalar | apalanc (13.26 s) |
| 2 | 1.7–3.1 | Claude | Define «x100». | `monitor` | mira_izq |  |
| 3 | 3.1–4.8 | Humano | Si sube 1 %, ¡gano 500 €! | `humano` | ilusionado |  |
| 4 | 4.8–7.4 | Claude | Y si baja 1 %, / esa parte no la cuentas. | `monitor_lateral` | idle |  |
| 5 | 7.4–8.7 | Humano | ¿Pierdo 5 €? | `humano` | bobo |  |
| 6 | 8.7–11.2 | Claude | 500 €. Todos. Liquidado. / Adiós, 500 €. | `pantalla_completa` | idle |  |
| 7 | 11.2–12.5 | Humano | ¿¡Con un 1 %!? | `dos` | preocupado, pose hombros |  |
| 8 | 12.5–15.4 | Claude | Un 1 % es lo que se mueve / mientras parpadeas. | `claude_ojos` | feliz, empuje de cámara |  |
| 9 | 15.4–17.1 | Humano | ¿Y quién gana entonces? | `humano` | confundido |  |
| 10 | 17.1–19.7 | Claude | El broker. Cobra comisión / gane o pierdas. | `cenital` | mira_der |  |
| 11 | 19.7–21.5 | Humano | Pues pongo x50, entonces. | `dos` | bobo |  |
| 12 | 21.5–25.2 | Claude | En la UE el máximo para minoristas / es 30:1. En cripto, 2:1. | `pantalla_completa` | idle | verdad (3.68 s) |
| 13 | 25.2–27.1 | Humano | ¡Pues me voy fuera de la UE! | `humano` | ilusionado |  |
| 14 | 27.1–30.7 | Claude | Donde no hay normas, tampoco / hay quien te devuelva nada. | `monitor` | mira_arriba |  |
| 15 | 30.7–32.2 | Humano | Vale... ¿y qué hago? | `dos` | preocupado |  |
| 16 | 32.2–36.0 | Claude | Poco apalancamiento, stop loss / y arriesga 1-2 % por operación. | `pantalla_completa` | idle | orden (3.0 s) |
| 17 | 36.0–37.5 | Humano | Eso es... aburrido. | `humano` | feliz |  |
| 18 | 37.5–41.0 | Claude | Aburrido es lo que funciona. / Lo emocionante es perderlo. | `monitor_lateral` | feliz |  |
| 19 | 41.0–42.5 | Humano | ¡Pues x100 con stop! | `dos` | ilusionado |  |
| 20 | 42.5–45.0 | Claude | Saltará al -1 %. / En fin... eres humano. | `general` | feliz |  |

## Datos reales que aparecen o se mencionan

- Límites de apalancamiento para minoristas en la UE (CFD): 30:1 divisas principales, 20:1 divisas no principales/oro/índices principales, 10:1 otras materias primas, 5:1 acciones y 2:1 criptomonedas. Fijados por ESMA en 2018; comprobar el estado actual en la web de ESMA o del regulador nacional.
  - Fuente: [ESMA (2018): prohíbe las opciones binarias y restringe los CFD a minoristas](https://www.esma.europa.eu/node/84933)
  - Fuente: [Resumen de los límites de apalancamiento de ESMA (FinanceFeeds)](https://financefeeds.com/esma-bans-offering-binary-options-retail-investors-introduces-restrictions-cfds/)
- Regla popular de gestión del riesgo: no arriesgar más del 1-2 % del capital por operación (orientación general, no asesoramiento financiero).

## Notas de producción

- **Humor:** Claude es sarcástico y pícaro («como el que le salva el culo»); el humano es ingenuo y algo tonto (expresiones `bobo`, `ilusionado`, `confundido`).
- **Voces:** son «blips» sintéticos (no hay voz real). Para voz real: ElevenLabs o grabarla y sustituir el audio.
- **Cifras y leyes:** los datos reales están citados arriba; las cuentas de ejemplo (márgenes, 214 tiendas, etc.) son ilustrativas. No es asesoramiento financiero ni legal.
