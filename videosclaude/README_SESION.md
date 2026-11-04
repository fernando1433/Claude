# videosclaude — LEEME PRIMERO (para cualquier sesion futura)

Proyecto de videos cortos verticales (TikTok/Reels, 9:16) con **Clawd** (la mascota pixel naranja de Claude Code, pequeña, sin boca)
y un **humano low-poly** sentado tras un escritorio (se ve de cintura arriba), estilo 3D low-poly nocturno.
Usuario: "Jefe", español informal y directo. Prefiere ver resultados y ajustar despues; no preguntar de mas.

## REGLA DE ORO: NO renderizar frames nuevos por video
Todo lo que se ve ya esta renderizado en **`biblioteca/`** como **capas PNG con transparencia**. Un video nuevo se crea SOLO
escribiendo un guion (`guiones/*.json`) y ejecutando el montador (PIL + ffmpeg, segundos, sin Blender):

```bash
python3 -I motor/montar_video.py guiones/ejemplo_dip.json salidas/ejemplo_dip.mp4
python3 -I motor/montar_video.py guiones/ejemplo_dip.json salidas/prueba.mp4 --solo-frames 12   # prueba rapida
```
Dependencias del montador: `pillow numpy` y `ffmpeg`. (Blender `pip install bpy` solo hace falta para REGENERAR la biblioteca.)

## Que hay en la biblioteca (ver `biblioteca/INDICE.md` y `biblioteca/<plano>/_contacto.png`)
4 planos (camaras fijas). Cada plano = `fondo.png` + capas de personajes (RGBA, mismo tamaño 720x1280):

| plano     | encuadre                                   | capas |
|-----------|--------------------------------------------|-------|
| `humano`  | primer plano del humano (cintura arriba)   | humano_<emocion>_<boca>.png |
| `claude`  | Clawd pequeño sobre una pila de libros     | claude_idle / parpadeo / feliz |
| `dos`     | humano + Clawd en el escritorio            | humano_* y claude_* |
| `espalda` | Clawd de espaldas mirando el monitor       | claude_idle |

- Emociones del humano: `neutral`, `feliz`, `preocupado`, `burlon`. Bocas: `cerrada`, `media`, `abierta` (+ `neutral_parpadeo`).
- Clawd SIEMPRE neutro (de pie, sin poses raras ni caras de sorpresa). Habla = **botecitos** (sube/baja), no tiene boca.
- Orden de apilado: **fondo -> pantalla del monitor -> sombras fijas -> humano -> claude**.
- **Sombras = capas aparte y FIJAS** (`sombra_humano.png`, `sombra_claude.png`). Los personajes NO llevan sombra pegada, asi al dar botecitos
  solo se mueve Clawd y el escenario queda quieto (verificado: entre frames solo cambia la zona de Clawd).
- La **pantalla del monitor es intercambiable**: el fondo trae pantalla `vacia` (neutra) y el montador pega cualquier imagen
  1280x720 con perspectiva (cuadrilatero guardado en `biblioteca/manifest.json`). Pantallas en `biblioteca/pantallas/`
  (`vacia` por defecto; `chart`, `chat`, `order` son EJEMPLOS de trading, no la identidad del proyecto). Para otro tema: crear PNG nuevo ahi.

## Como se hace un video
1. Escribir `guiones/<nombre>.json` (copiar `ejemplo_dip.json`). Campos por linea: `inicio`, `fin`, `quien` (humano|claude), `texto`,
   `plano`, `emocion` (humano), `pantalla` (cambia el monitor desde esa linea). Extra: `cambios_pantalla` [{"t":..,"pantalla":..}].
2. Ejecutar el montador. Salida en `salidas/`.
3. Animacion a **6 fps** (duplicada a 24 al exportar): pocos frames distintos, movimientos minimos (boca alterna, botecitos, parpadeo).
   13 s = solo 80 frames de animacion. Se pueden hacer videos mas largos sin coste de render.

## Limitaciones conocidas (decirlas al Jefe, no inventar)
- Las **voces son "blips"** sinteticos (estilo Animal Crossing), no voz real. Para voz real: ElevenLabs con la cuenta del Jefe o su voz grabada.
- Solo hay 4 camaras fijas. Una camara/pose NUEVA exige re-renderizar con Blender (ver abajo) — evitarlo salvo que haga falta de verdad.
- Solo hay UNA pose de brazos del humano ("tecleando") y Clawd solo "de pie" / "de espaldas". Las poses de pensar, facepalm, encoger hombros,
  celebrar, sorpresa, etc. se probaron y se BORRARON porque quedaban mal; si se quieren, hay que rehacer bien el rig de brazos primero.

## Regenerar o ampliar la biblioteca (solo si se pierde o se necesita un plano/estado nuevo)
```bash
pip install bpy                                   # Blender como modulo (Python 3.13 ok)
python3 -I motor/texturas.py tex                  # pantallas, ventana de ciudad, neon, poster
python3 -I motor/render_biblioteca.py biblioteca  # ~25 min en 4 CPU; admite plano concreto: ... biblioteca dos
python3 -I motor/indice_biblioteca.py             # INDICE.md + hojas de contacto
```
- `motor/escena.py`: escena Blender completa (personajes, escritorio, props, luces, `BASES` = camaras, `set_human`, `set_clawd`).
- Añadir un plano: nueva entrada en `BASES` (escena.py) y en `PLANOS` (render_biblioteca.py).
- Añadir estados (p.ej. otra emocion): ampliar `EMO`/`BOCA` en render_biblioteca.py y renderizar solo ese plano.

## Estructura
```
motor/      codigo (escena.py, texturas.py, render_biblioteca.py, montar_video.py, indice_biblioteca.py)
biblioteca/ capas ya renderizadas + manifest.json + INDICE.md + pantallas/   <-- REUTILIZAR, no regenerar
guiones/    guiones json de los videos
salidas/    videos finales (mp4)
tex/        texturas generadas (regenerables; no hace falta guardarlas)
```
