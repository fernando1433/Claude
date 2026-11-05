# videosclaude — GUÍA COMPLETA (para continuar desde otra sesión)

## 0. Qué es esto
Fábrica de vídeos cortos verticales (9:16, 1080x1920, 24 fps, H.264+AAC) para TikTok/Reels/Shorts.
Personajes: **Clawd** (mascota pixel naranja de Claude Code: sin boca, ojos cuadrados, sin brillos, da botecitos al hablar; sarcástico, pícaro, el que le salva el culo al humano) y un **humano low-poly** (gorro rojo, auriculares, sudadera verde; ingenuo, medio tonto), sentado tras un escritorio, cintura arriba.
Todos los vídeos empiezan con un gancho y acaban con el subtítulo «En fin... eres humano» (nunca «palomitas»).
Usuario: "Jefe", español informal y directo, quiere ver resultados y ajustar luego.

## 1. Dónde está todo
- **Repo:** https://github.com/fernando1433/Claude — rama `claude/cool-knuth-ye0cyp`, carpeta `videosclaude/`. (Pesa ~1,1 GB: biblioteca 419 MB + salidas 572 MB.)
- Para retomar en otra sesión: clonar el repo, `git checkout claude/cool-knuth-ye0cyp`, leer `videosclaude/README_SESION.md` y este archivo.
```
videosclaude/
  README_SESION.md   léeme corto
  motor/             TODO el código (ver §3)
  biblioteca/        capas PNG ya renderizadas, por ambiente y plano (419 MB)  <-- REUTILIZAR, no re-renderizar
  guiones/           JSON de cada vídeo (los genera motor/generar_guiones.py; NO editar a mano)
  salidas/           mp4 finales (108), portadas/ (jpg 1080x1920), voz/ (9 muestras eSpeak experimentales)
  docs/              CATALOGO.md (con portadas y "Empieza por estos 10"), QA.md, videos/<id>.md (guion, pantallas y datos reales con fuentes), videos/img/ (tiras de fotogramas)
  tex/               texturas regenerables;  bases/  escenas base de referencia
```

## 2. Cómo se hace un vídeo (la regla de oro)
**No se renderiza nada por vídeo.** Blender ya generó las capas (fondo, humano, Clawd, sombras) por ambiente/plano. Un vídeo = guion + montador en 2D (PIL + numpy + ffmpeg), unos 5 min, sin Blender.
Dependencias del montaje: `pip install pillow numpy` + `ffmpeg`. (Regenerar biblioteca: `pip install bpy`, Blender 5.2.3 como módulo, Python 3.13.)
```bash
cd videosclaude
python3 -I motor/montar_video.py guiones/trading_01_curso_milagro.json salidas/trading_01_curso_milagro.mp4
python3 -I motor/montar_video.py guiones/ALGO.json salidas/prueba.mp4 --solo-frames 12   # prueba rápida
python3 -I motor/montar_video.py guiones/X.json salidas/X.mp4 --voz espeak               # voz robótica (experimental)
```
### Crear un vídeo NUEVO (el flujo normal)
1. Editar `motor/generar_guiones.py` (lista de vídeos; helpers `H` humano, `C` Claude, `S` pantalla, `casual(...)`, `micro(...)`, `CHAT(n)` con n ≤ nº de líneas del vídeo). Los tiempos se calculan solos por longitud del texto. Las pantallas se sincronizan con `sync=('ini'|'fin', n_línea_1-based, p, extra_s)`.
2. `python3 -I motor/generar_guiones.py` → escribe `guiones/*.json`, `docs/videos/*.md`, índice y catálogo.
3. `python3 -I motor/validar_guiones.py` → valida.
4. Montar: `python3 -I motor/montar_video.py ...` o dejar el demonio (§4).
5. `python3 -I motor/qa_videos.py` → revisa mp4 (duración, audio, fotogramas), genera `docs/QA.md`, tiras y portadas.
6. Commit + push.

### Campos de una línea del guion
`inicio fin quien texto plano` · humano: `emocion pose` · Claude: `claude_estado empuje` · `tono` (`sarcastico` por defecto en Claude, `dudoso`, `seguro`) · `pantalla` (`{"tipo":..., "datos":{...}, "duracion":s}`) · `sfx:false` en el guion desactiva efectos. Docstring completo en `motor/montar_video.py`.
Animación a **6 fps duplicada a 24** (pocos frames, movimientos mínimos: boca que alterna, botecitos, parpadeo) — petición expresa del Jefe.

## 3. El código (`motor/`)
| Archivo | Para qué |
|---|---|
| `escena.py` | Escena **Blender**: personajes, props, luces por `VC_AMBIENTE` (noche\|dia\|atardecer), decorado por `VC_DECOR` (trading\|tienda\|casa), cámaras `BASES`, `set_human`, `set_clawd`, IK de brazos (`ik_brazo`), expresiones (ojos, cejas, boca) |
| `render_biblioteca.py` | Renderiza las capas PNG RGBA (Cycles CPU, 24 muestras + denoise, 720x1280, `film_transparent`, holdout/shadow-catcher). Reanudable (salta capas existentes), `--forzar` |
| `texturas.py` | Pantallas base, ventanas (noche/día/atardecer), neón y póster por decorado |
| `montar_video.py` | Montador 2D: apila capas, warp de perspectiva de la pantalla del monitor, `pantalla_completa` con zoom, audio (blips + pad + SFX), `--solo-frames`, `--voz` |
| `pantallas.py` | Todas las pantallas animadas dibujadas con PIL (`p_xxx(p, datos)` + registro en `PANTALLAS`; `ZOOM_AUTO`; `datos.desde`) |
| `generar_guiones.py` | Fuente de verdad de los ~105 vídeos y sus fuentes citadas; genera JSON + docs + catálogo |
| `cola_pendientes.py` | Demonio de montaje: monta guiones nuevos/modificados cuyo ambiente ya esté renderizado. `PARTE=0/3 python3 -I motor/cola_pendientes.py <logs>` (1/3, 2/3 para paralelo) |
| `autosubir.sh` | commit+push a GitHub cada 7 min |
| `cola_render.sh / 2 / 3` | Colas de render de bibliotecas (reanudables) |
| `qa_videos.py`, `validar_guiones.py`, `indice_biblioteca.py` | QA, validación, INDICE.md + `_contacto.png` por ambiente |
| `voz_espeak.py`, `muestras_voz.sh` | Voz eSpeak NG offline (experimental) |
| `cola_montaje.sh` | OBSOLETO (re-montaba todo) |

## 4. Blender: cuándo y cómo
Solo hace falta para **cámara/pose/ambiente NUEVOS** (~14 s por capa).
```bash
pip install bpy
python3 -I motor/texturas.py tex                               # texturas
VC_AMBIENTE=dia VC_DECOR=tienda VC_LITE=1 python3 -I motor/render_biblioteca.py $PWD/biblioteca/dia_tienda humano dos
bash motor/cola_render.sh /tmp                                 # cola completa (~2 h en 4 CPU)
python3 -I motor/indice_biblioteca.py                          # INDICE.md + contactos
```
Variables: `VC_AMBIENTE`, `VC_DECOR`, `VC_LITE=1`, `VC_SAMPLES`, `VC_TEX`.
Poses probadas y **borradas por quedar mal**: facepalm, celebrar, sorpresa y sentado/dormido de Clawd. No reintroducir sin rehacer el rig. Detalle clave: `EYE_BASE` se restaura en cada `set_human` (si no, los ojos del humano "se separan" de la cara).

## 5. Biblioteca (capas)
`biblioteca/<ambiente>/<plano>/`: `fondo.png`, `sombra_humano.png`, `sombra_claude.png`, `humano_<emo>_<boca>.png`, `humano_<pose>_<emo>_<boca>.png`, `claude_<estado>.png`, `manifest.json` (con `pantalla_quad`). Apilado: fondo → pantalla → sombras (fijas) → humano → Clawd. Las sombras son capas fijas aparte (el escenario no se mueve cuando Clawd bota).
- **Ambientes:** `noche_trading` (completa), `dia_trading`, `dia_tienda`, `atardecer_tienda`, `noche_tienda`, `noche_casa`, `dia_casa`, `atardecer_casa` (los de día/atardecer son "lite"). Cada uno tiene `INDICE.md` y `_contacto.png`. Trading = neón TRADE/póster BUY THE DIP; tienda = neón OPEN, cajas, sin nada de trading; casa = neón home, montañas, gato dormido.
- **Planos:** humano, dos, general, monitor, monitor_espalda, monitor_lateral, cenital, claude_ojos, claude y espalda (solo noche_trading), pantalla_completa (2D).
- **Humano:** emociones neutral/feliz/preocupado/burlon + bobo/ilusionado/confundido; poses type/pensar/senalar/hombros/mira; bocas cerrada/media/abierta. **Clawd:** idle, feliz, mira_izq, mira_der, mira_arriba. Si falta una pose/emoción en un plano, el montador usa la más cercana.

## 6. Pantallas disponibles (`motor/pantallas.py`)
Negocio/vida: chat dashboard tienda calendario email analitica tareas hoja · Útiles: mensajes(auto) menu recordatorios contrasenas phishing wifi bizum presupuesto interes anuncios tienda_falsa llamada inflacion etf comisiones martingala · Trading: trading cartera orden resultado curso checkout telegram apalanc verdad(esma|brasil|brasil2|apalanc) · Dropshipping: catalogo proveedor margen producto pedido tracking cliente ley(garantia).

## 7. Vídeos hechos (108 mp4; catálogo con portadas en `docs/CATALOGO.md`)
trading_* (curso milagro, señales VIP, apalancamiento x100, cuñado, gurú del yate, doblar apuesta…, + trading_30s_sarcastico) · drop_* (qué es, producto ganador, primer pedido, devoluciones, proveedor barato) · extra_* (presupuesto, un día con Claude, anuncios, aumento, entrevista) · fin_* (finanzas: comisiones, interés…) · casual_* (~50, día a día con gancho: «¿tú me quieres?», «¿qué ceno?»…) · util_* (contraseñas, phishing, WiFi pública, Bizum, WhatsApp, actualizaciones, copias…). Cada uno tiene `docs/videos/<id>.md` con guion plano a plano, pantallas y **datos reales con fuente** (ESMA 74–89 % CFD pierden; estudio Brasil 97 % day traders; ESMA 30:1; desistimiento 14 días; IVA importaciones 2021; garantía 3 años; INCIBE; NordPass; BCE; CNMV). Las cuentas de ejemplo son ilustrativas. No es asesoramiento financiero.
QA: 105 revisados, 0 problemas (`docs/QA.md`).

## 8. Si el contenedor se reinicia
Se pierden los procesos, no el repo. Relanzar: `PARTE=0/3 python3 -I motor/cola_pendientes.py <logs>` ×3 (1/3, 2/3), `bash motor/autosubir.sh`, y las colas de render si faltan capas (son reanudables). Marcadores `LISTO_*` en el scratchpad de la sesión (no están en el repo; no pasa nada si faltan, se salta lo ya existente).

## 9. Limitaciones y pendientes (honesto)
- **Voces:** blips sintéticos (estilo Animal Crossing). `--voz espeak` da voz robótica inteligible, pero **nadie la ha escuchado** aún. Voz real = ElevenLabs con la cuenta del Jefe o voz grabada por él (en la sesión solo había acceso a PyPI).
- `pantalla_completa` aprovecha poco alto en vertical (monitor 16:9): mejora pendiente = pantallas en formato vertical.
- Cámara/pose nueva = re-render Blender.
- Repo pesado (~1,1 GB); si molesta, mover mp4 a releases o a otro almacenamiento.
- Los enlaces cortos de TikTok no se pudieron abrir (proxy); la referencia de estilo fue base.learn (se investigó con vidIQ). Nada de "Roco" (el Jefe pidió olvidarlo).

## 10. Ideas siguientes
Voz real; subtítulos grandes estilo TikTok; pantallas verticales; más ambientes (cocina, oficina); series con personajes recurrentes; tandas de `util_*` con datos reales; publicar con descripción + fuentes del `.md` de cada vídeo.
