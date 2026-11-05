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

## Vídeos hechos (índice completo en `docs/videos/README.md`; cada uno tiene su `docs/videos/<id>.md` con guion, pantallas y datos reales con fuentes)
Familias (todos terminan con **«En fin... eres humano»** y empiezan con un **gancho** en la primera frase):
- `trading_*` (5, ~45 s): curso milagro, señales VIP, apalancamiento x100, el cuñado, el gurú del yate (+ `trading_30s_sarcastico`).
- `drop_*` (5, ~45 s): qué es el dropshipping, producto ganador, primer pedido, devoluciones, proveedor barato.
- `extra_*` (5): presupuesto, un día con Claude, anuncios que no venden, pedir un aumento, entrevista de trabajo.
- `casual_*` (~30, 28-40 s): conversaciones del día a día con gancho («Claude, ¿tú me quieres?», «¿qué ceno hoy?», «no me contesta»…).
- `util_*` (4, ~40 s, con datos reales y fuentes): contraseñas, estafa del banco (phishing), WiFi pública, Bizum inverso.
Los guiones se generan con `python3 -I motor/generar_guiones.py` (editar ese archivo, no los JSON) y se validan con `python3 -I motor/validar_guiones.py`.
El demonio `motor/cola_pendientes.py` monta solo cualquier guion nuevo/modificado cuyo ambiente ya esté renderizado; `motor/autosubir.sh` sube a GitHub cada 7 min. `motor/qa_videos.py` revisa todos los mp4 (duración, audio, fotogramas) y genera `docs/QA.md`, las tiras de `docs/videos/img/` y las **portadas** 1080x1920 de `salidas/portadas/`.
El montaje admite varios trabajadores en paralelo: `PARTE=0/3 python3 -I motor/cola_pendientes.py <logs>` (y 1/3, 2/3). Los videos incluyen efectos de sonido suaves (whoosh en cada corte, pop al cambiar la pantalla; `"sfx": false` en el guion lo desactiva).

## Ambientes (carpetas de `biblioteca/`)
Cada ambiente es una sala completa renderizada: `noche_trading` (noche, neón TRADE, póster BUY THE DIP), `dia_trading` (de día, mismo decorado de trading),
`dia_tienda` y `atardecer_tienda` (decorado de **tienda online**: neón OPEN, póster de envío, cajas; **sin nada de trading**), `noche_casa`, `dia_casa` y `atardecer_casa` (decorado de **casa** para el día a día: neón «home», póster de montañas, un gato dormido en el escritorio) y `noche_tienda` (tienda online de noche). Se elige con `"ambiente"` en el guion.
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
- Día a día / útiles: `mensajes` (chat estilo móvil; `auto:true` lo escribe con el propio diálogo) `menu` `recordatorios` `contrasenas` `phishing` `wifi` `bizum` `presupuesto` `interes` `anuncios`
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
