# videosclaude — LÉEME PRIMERO (para cualquier sesión futura)

Proyecto de vídeos cortos verticales (TikTok/Reels, 9:16) con **Clawd** (la mascota pixel naranja de Claude Code: pequeña, sin boca, ojos cuadrados)
y un **humano low-poly** (gorro rojo, auriculares, sudadera verde) sentado tras un escritorio, visto de cintura arriba. Estilo 3D low-poly.
Usuario: **"Jefe"**, español informal y directo; prefiere ver resultados y ajustar después (no preguntar de más).
Tono de los vídeos: **Claude = sarcástico, pícaro, el que le salva el culo al humano; el humano = ingenuo, medio tonto.** Siempre con humor, y a veces con datos reales citados.

## REGLA DE ORO: no se renderiza nada nuevo por vídeo
Todo lo visual ya está renderizado en `biblioteca/<ambiente>/` como **capas PNG con transparencia**. Un vídeo nuevo = escribir un guion + ejecutar el montador (PIL + ffmpeg, ~5 min, sin Blender):

```bash
python3 -I motor/montar_video.py guiones/trading_01_curso_milagro.json salidas/trading_01_curso_milagro.mp4
python3 -I motor/montar_video.py guiones/ALGO.json salidas/prueba.mp4 --solo-frames 12     # prueba rápida
```
Dependencias del montador: `pillow numpy` + `ffmpeg`. (`pip install bpy` solo hace falta para REGENERAR la biblioteca.)

## Vídeos hechos (cada uno tiene su documentación en `docs/videos/<id>.md`)
| id | tema | ambiente |
|----|------|----------|
| `trading_01_curso_milagro` | el curso «millonario en 7 días»; Claude bloquea el pago | `noche_trading` |
| `trading_02_senales_vip` | grupo VIP de señales = pump & dump; Claude le salva 380 € | `dia_trading` |
| `trading_03_apalancamiento_x100` | x100 → liquidado; límites UE y gestión de riesgo | `dia_trading` |
| `drop_01_que_es_dropshipping` | cómo funciona y por qué de 29,90 € quedan 3,44 € | `dia_tienda` |
| `drop_02_producto_ganador` | «lámpara de cactus»: competencia, moda, marcado CE | `dia_tienda` |
| `drop_03_primer_pedido` | envío de 25 días, cliente enfadado, 14 días de desistimiento, IVA | `atardecer_tienda` |
| (anteriores) `trading_30s_sarcastico`, `ejemplo_*` | pruebas / ejemplos | `noche_trading` |

Los 6 guiones grandes se generan con `python3 -I motor/generar_guiones.py` (tiempos automáticos según la longitud de cada frase, pantallas sincronizadas con el diálogo y **docs por vídeo** con tabla de planos y fuentes). **Edita el generador y vuelve a ejecutarlo** en vez de tocar los JSON a mano.

## Ambientes (carpetas de `biblioteca/`)
Cada ambiente es una sala completa renderizada: `noche_trading` (noche, neón TRADE, póster BUY THE DIP), `dia_trading` (de día, mismo decorado de trading),
`dia_tienda` y `atardecer_tienda` (decorado de **tienda online**: neón OPEN, póster de envío, cajas; **sin nada de trading**). Se elige con `"ambiente"` en el guion.
Cada una tiene `INDICE.md` y `_contacto.png` por plano. Las de día/atardecer son versiones «lite» (menos poses/emociones); `noche_trading` es la completa.

## Planos (cámaras fijas) y capas
`humano` (primer plano), `dos` (humano + Clawd), `general` (sala entera), `monitor` (monitor centrado y de frente, Clawd al pie), `monitor_espalda`, `monitor_lateral` (3/4),
`cenital` (desde arriba), `claude_ojos` (primerísimo plano de Clawd), `claude` y `espalda` (solo noche), y `pantalla_completa` (2D: la pantalla ocupa el vídeo; zoom automático).
- **Humano**: emociones `neutral feliz preocupado burlon` + «de tonto»: `bobo`, `ilusionado`, `confundido`. Poses con cinemática inversa: `type` (por defecto), `pensar`, `senalar`, `hombros`, `mira`.
  Bocas `cerrada media abierta`. Si el plano no tiene una pose/emoción, el montador usa la más cercana.
- **Clawd**: `idle`, `feliz` (ojos ^ ^ de listillo), `mira_izq`, `mira_der`, `mira_arriba` (reojo sarcástico). **Siempre neutro, sin boca, sin brillos en los ojos**; al hablar da botecitos.
- Orden de apilado: fondo → pantalla del monitor → sombras fijas → humano → Clawd. Las **sombras son capas aparte y fijas** (el escenario no se mueve con los botecitos).

## Pantallas del monitor (`motor/pantallas.py`, se dibujan al montar, no hay que renderizar)
`{"tipo":"dashboard","datos":{...},"duracion":4}` en el campo `pantalla` de una línea. Se animan solas durante `duracion` segundos (cifras que suben, texto que se teclea…).
- Negocio/vida: `chat` `dashboard` `tienda` `calendario` `email` `analitica` `tareas` `hoja`
- Trading: `trading` `cartera` `orden` `resultado` `curso` (curso milagro + banderas rojas de Claude) `checkout` (pago bloqueado) `telegram` (modo `chat`|`pump`) `apalanc` `verdad` (tipo `esma`|`brasil`|`apalanc`)
- Dropshipping: `catalogo` `proveedor` `margen` (calculadora real: precio − coste − anuncio − comisión − IVA, ROAS mínimo) `producto` `pedido` `tracking` `cliente` `ley`
- Opciones comunes: `datos.desde` (empieza la animación ya avanzada), `zoom` en la línea (`pantalla_completa`), `ZOOM_AUTO`. Imágenes de producto: iconos dibujados con PIL (sin imágenes externas).
- Nueva pantalla: función `p_xxx(p, datos)` en pantallas.py + registrarla en `PANTALLAS`.

## Campos de una línea del guion
`inicio fin quien texto plano` · humano: `emocion pose` · Claude: `claude_estado empuje` (zoom lento) · `tono` (`sarcastico` por defecto en Claude, `dudoso`, `seguro`) · `pantalla`. Ver el docstring de `motor/montar_video.py`.
Animación a **6 fps** duplicada a 24: pocos frames distintos y movimientos mínimos (boca que alterna, botecitos, parpadeo). 45 s = solo 270 frames de animación.

## Limitaciones conocidas (decirlas al Jefe, no inventar)
- Las **voces son «blips»** sintéticos (no voz real). Para voz real: ElevenLabs con la cuenta del Jefe o su voz grabada.
- `pantalla_completa` aprovecha poco alto en vertical (el monitor es 16:9); mejora pendiente: pantallas en formato vertical.
- Cámara o pose NUEVA = re-render con Blender (~14 s/capa). Evitarlo salvo que haga falta.
- Poses probadas y **borradas por quedar mal**: facepalm, celebrar, sorpresa (Clawd), sentado/dormido (Clawd). No reintroducir sin rehacer bien el rig.
- Los datos reales de cada vídeo están citados en su `docs/videos/*.md`; las cuentas de ejemplo (márgenes, nº de tiendas…) son ilustrativas. No es asesoramiento financiero ni legal.

## Regenerar o ampliar bibliotecas
```bash
pip install bpy                                   # Blender como módulo (Python 3.13 ok)
python3 -I motor/texturas.py tex                  # pantallas base, ventanas (noche/día/atardecer), neón y póster (trading/tienda)
bash motor/cola_render.sh /tmp                    # cola completa: noche_trading, dia_trading, dia_tienda, atardecer_tienda (~2 h en 4 CPU; reanudable)
VC_AMBIENTE=dia VC_DECOR=tienda VC_LITE=1 python3 -I motor/render_biblioteca.py $PWD/biblioteca/dia_tienda humano dos   # un ambiente/planos concretos
python3 -I motor/indice_biblioteca.py             # INDICE.md + hojas de contacto de todos los ambientes
bash motor/cola_montaje.sh /tmp                   # monta los 6 vídeos cuando cada biblioteca esté lista
```
`motor/escena.py` = escena Blender (personajes, props, luces por `VC_AMBIENTE`=`noche|dia|atardecer`, decorado por `VC_DECOR`=`trading|tienda`, `BASES` = cámaras, `set_human`, `set_clawd`, IK de brazos).

## Estructura
```
motor/       código (escena, texturas, pantallas, render_biblioteca, montar_video, generar_guiones, indice_biblioteca, colas .sh)
biblioteca/  <ambiente>/<plano>/ capas PNG + manifest.json + INDICE.md + _contacto.png ; pantallas/ (compartidas)   <-- REUTILIZAR
guiones/     JSON de los vídeos (los 6 grandes los escribe generar_guiones.py)
docs/videos/ documentación por vídeo (guion plano a plano, pantallas, datos reales con fuentes)
salidas/     vídeos finales (mp4)
tex/         texturas (regenerables)
```
