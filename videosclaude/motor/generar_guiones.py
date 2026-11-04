"""Genera los guiones JSON y la documentacion (docs/videos/*.md) de los videos de ~45 s.
Los tiempos se calculan solos segun la longitud de cada frase (ritmo de lectura) y las pantallas animadas se SINCRONIZAN con el dialogo
(p. ej. que el 'LIQUIDADO' salga justo cuando Claude lo dice).

Uso:  python3 -I motor/generar_guiones.py            (escribe guiones/*.json y docs/videos/*.md)
"""
import os, json, sys
from PIL import ImageFont

RAIZ = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
TOTAL = 45.0
FUENTE = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 44)

def H(t, p, e='neutral', pose=None, scr=None, tono=None): return dict(q='humano', t=t, p=p, e=e, pose=pose, scr=scr, tono=tono)
def C(t, p, st=None, emp=False, scr=None, tono=None): return dict(q='claude', t=t, p=p, st=st, emp=emp, scr=scr, tono=tono)
def S(tipo, datos=None, sync=None, dur=None): return dict(tipo=tipo, datos=datos, sync=sync, dur=dur)   # sync = ('ini'|'fin', n_linea, p_objetivo, segundos_extra)

# ------------------------------------------------------------------------------------------------ fuentes
ESMA = ('ESMA (2018): prohíbe las opciones binarias y restringe los CFD a minoristas', 'https://www.esma.europa.eu/node/84933')
ESMA_R = ('ESMA: renovación de las restricciones a los CFD', 'https://www.esma.europa.eu/press-news/esma-news/esma-renew-restriction-cfds-further-three-months')
LEVER = ('Resumen de los límites de apalancamiento de ESMA (FinanceFeeds)', 'https://financefeeds.com/esma-bans-offering-binary-options-retail-investors-introduces-restrictions-cfds/')
BRASIL = ('Chague, De-Losso y Giovannetti — «Day Trading for a Living?» (SSRN)', 'https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3423101')
BRASIL2 = ('Resumen del estudio (Quantpedia)', 'https://quantpedia.com/retail-day-trading-is-an-uphill-battle/')
DESIST = ('Plazo de 14 días para devolver compras online en la UE (Consumer.es)', 'https://www.consumer.es/tecnologia/el-plazo-de-devolucion-para-las-compras-por-internet-en-la-ue-sera-de-14-dias.html')
DESIST2 = ('Derecho de desistimiento en compras online (Legálitas)', 'https://www.legalitas.com/actualidad/derecho-la-devolucion-de-tu-compra-online')
IVA1 = ('Nuevas reglas de IVA para el comercio electrónico en la UE desde el 1/7/2021 (Organización Mundial de Aduanas)', 'https://www.wcoomd.org/es-es/media/newsroom/2021/june/the-european-union-introduces-new-value-added-tax-rules-for-e-commerce-from-1-july-202.aspx')
IVA2 = ('Fin de la exención de 22 € y ventanilla única de importación IOSS (Avalara)', 'https://www.avalara.com/vatlive/en/vat-news/eu-2021-ending--22-import-vat-exemption--new-ioss-return.html')
CE1 = ('Marcado CE (Tu Europa, Comisión Europea)', 'https://europa.eu/youreurope/business/product-requirements/labels-markings/ce-marking/index_es.htm')
CE2 = ('Importaciones de fuera de la UE y marcado CE (Euronorm)', 'https://www.euronorm.net/content/ce-marking/category/import-and-export/imports-from-outside-the-eu-eea.php')

BANKINTER = ('La regla 50/30/20 (Bankinter)', 'https://www.bankinter.com/blog/finanzas-personales/regla-50-20-30')
SEMANA = ('Qué es la regla 50/30/20 (Semana)', 'https://www.semana.com/ahorro-e-inversion/articulo/que-es-la-regla-503020-para-manejar-mejor-su-dinero/80205/')

# ------------------------------------------------------------------------------------------------ videos
VIDEOS = []

VIDEOS.append(dict(
    id='trading_01_curso_milagro', titulo='El curso milagro', ambiente='noche_trading',
    resumen='El trader quiere ser millonario en 7 días con un curso de 997 €. Claude le va desmontando el anuncio (contador falso, testimonios de stock, «garantizado») y, cuando el tonto va a pagar, le bloquea el pago.',
    datos=[('74–89 % de las cuentas minoristas de CFD pierden dinero (cifra de las advertencias de riesgo obligatorias que fijó ESMA en 2018; porcentaje de cuentas, no probabilidad individual).', [ESMA, ESMA_R])],
    lineas=[
        H('¡Voy a ser millonario!\nMe apunté a un curso.', 'general', 'ilusionado', scr=S('curso', sync=('ini', 6, 0.36))),
        C('Ah, ¿sí? Enséñamelo.', 'monitor', 'mira_izq'),
        H('«Millonario en 7 días».\n¡Solo 997 €!', 'dos', 'feliz', pose='senalar'),
        C('Si funcionara, no lo vendería:\nestaría contando billetes.', 'monitor', 'feliz'),
        H('Pero tiene un Lambo.', 'humano', 'bobo'),
        C('Alquilado. Y el contador\nse reinicia cada vez.', 'monitor'),
        H('¿Y los testimonios?', 'dos', 'confundido'),
        C('Fotos de stock. «Carlos, 24»\nes dentista en otro anuncio.', 'claude_ojos', 'feliz', emp=True),
        C('Dato real: 74–89 % de cuentas\nminoristas de CFD pierde.', 'pantalla_completa', scr=S('verdad', {'tipo': 'esma'}, sync=('fin', 9, 1.0, 0.0))),
        H('Pero yo soy del 11 %.', 'humano', 'bobo'),
        C('Todos creen ser del 11 %.\nEl 89 % también.', 'cenital', 'mira_arriba'),
        H('Pues lo compro igual.', 'dos', 'ilusionado', scr=S('checkout', sync=('ini', 13, 0.66, 0.4))),
        C('Pago bloqueado.\nDe nada.', 'pantalla_completa'),
        H('¡Era mi dinero!', 'humano', 'preocupado', pose='hombros'),
        C('Y lo sigue siendo.\nA eso se le llama ahorrar.', 'monitor', 'feliz'),
        H('¡Mira, otro! ¡Millonario en 3 días!', 'humano', 'ilusionado', scr=S('curso', dur=3.5)),
        C('Mismo PDF, menos páginas.\nEn fin... eres humano.', 'general', 'feliz'),
    ]))

VIDEOS.append(dict(
    id='trading_02_senales_vip', titulo='Las señales VIP de Telegram', ambiente='dia_trading',
    resumen='El trader paga 49 €/mes por un canal de señales. Claude le enseña cómo funciona un «pump & dump»: el admin compra antes, anuncia, el precio sube, él vende y tú te quedas con la pérdida. Claude le salva 380 € a tiempo.',
    datos=[('97 % de los day traders brasileños que persistieron más de 300 días perdió dinero; solo el 0,5 % (8 de 1.551) ganó más que un sueldo básico de banca (estudio de la CVM de Brasil, 2013-2015).', [BRASIL, BRASIL2])],
    lineas=[
        H('¡Me he metido en un grupo\nVIP de señales!', 'general', 'ilusionado', scr=S('telegram', {'modo': 'chat'}, sync=('ini', 5, 1.0, 0.0))),
        C('Déjame adivinar:\n49 € al mes.', 'monitor', 'mira_izq'),
        H('¡El admin gana un 3.000 %!', 'dos', 'feliz', pose='senalar'),
        C('Casualmente, solo enseña\nlas que ganan.', 'monitor_lateral'),
        H('Hoy dice: compra $PERRO.', 'humano', 'bobo', scr=S('telegram', {'modo': 'pump'}, sync=('ini', 8, 0.62, 1.2))),
        C('Un perro. Muy serio todo.', 'monitor_lateral', 'feliz'),
        H('¡Va a subir un 1.000 %!', 'dos', 'ilusionado'),
        C('Sube porque lo dice el admin.\nCuando tú compras, él vende.', 'cenital', 'mira_der'),
        H('¿Eso es legal?', 'humano', 'confundido'),
        C('Se llama pump & dump:\nlo inflan y tú pagas.', 'pantalla_completa'),
        H('Yo ya compré... 400 €.', 'dos', 'preocupado', pose='hombros'),
        C('Vende YA. Aún recuperas 380 €.', 'monitor', 'feliz'),
        H('¿Cómo vendo?', 'humano', 'confundido'),
        C('Botón rojo. Y adiós al VIP:\nmira cómo luce tu cartera.', 'pantalla_completa',
          scr=S('cartera', {'posiciones': [['$PERRO (el del admin)', -95], ['$GATO («seguro que sube»)', -71], ['$LAMBO', -88], ['Curso de trading', -100], ['Bitcoin', 4]]}, sync=('fin', 14, 0.95, 0.0))),
        H('¡Me quedan 380 €!', 'dos', 'preocupado'),
        C('380 € más de los que\nhabrías tenido sin mí.', 'claude_ojos', 'feliz', emp=True),
        H('¡Eres un genio, Claude!', 'humano', 'ilusionado'),
        C('Dato real: 97 % de day traders\ncon +300 días pierde.', 'pantalla_completa', scr=S('verdad', {'tipo': 'brasil'}, sync=('fin', 18, 1.0, 0.0))),
        H('Pero yo soy del 3 %, ¿no?', 'dos', 'bobo'),
        C('Claro. Seguro.\nEn fin, eres humano.', 'general', 'feliz'),
    ]))

VIDEOS.append(dict(
    id='trading_03_apalancamiento_x100', titulo='Apalancamiento x100', ambiente='dia_trading',
    resumen='El trader quiere meter 500 € a x100 «porque si sube un 1 % gana 500 €». Claude le enseña la otra cara: si baja un 1 %, liquidado. Y le explica los límites de la UE y la regla de arriesgar poco por operación.',
    datos=[('Límites de apalancamiento para minoristas en la UE (CFD): 30:1 divisas principales, 20:1 divisas no principales/oro/índices principales, 10:1 otras materias primas, 5:1 acciones y 2:1 criptomonedas. Fijados por ESMA en 2018; comprobar el estado actual en la web de ESMA o del regulador nacional.', [ESMA, LEVER]),
           ('Regla popular de gestión del riesgo: no arriesgar más del 1-2 % del capital por operación (orientación general, no asesoramiento financiero).', [])],
    lineas=[
        H('¡Pongo mis 500 € a x100!', 'dos', 'feliz', pose='senalar', scr=S('apalanc', sync=('ini', 6, 0.68, 0.3))),
        C('Define «x100».', 'monitor', 'mira_izq'),
        H('Si sube 1 %, ¡gano 500 €!', 'humano', 'ilusionado'),
        C('Y si baja 1 %,\nesa parte no la cuentas.', 'monitor_lateral'),
        H('¿Pierdo 5 €?', 'humano', 'bobo'),
        C('500 €. Todos. Liquidado.\nAdiós, 500 €.', 'pantalla_completa'),
        H('¿¡Con un 1 %!?', 'dos', 'preocupado', pose='hombros'),
        C('Un 1 % es lo que se mueve\nmientras parpadeas.', 'claude_ojos', 'feliz', emp=True),
        H('¿Y quién gana entonces?', 'humano', 'confundido'),
        C('El broker. Cobra comisión\ngane o pierdas.', 'cenital', 'mira_der'),
        H('Pues pongo x50, entonces.', 'dos', 'bobo'),
        C('En la UE el máximo para minoristas\nes 30:1. En cripto, 2:1.', 'pantalla_completa', scr=S('verdad', {'tipo': 'apalanc'}, sync=('fin', 12, 1.0, 0.0))),
        H('¡Pues me voy fuera de la UE!', 'humano', 'ilusionado'),
        C('Donde no hay normas, tampoco\nhay quien te devuelva nada.', 'monitor', 'mira_arriba'),
        H('Vale... ¿y qué hago?', 'dos', 'preocupado'),
        C('Poco apalancamiento, stop loss\ny arriesga 1-2 % por operación.', 'pantalla_completa', scr=S('orden', sync=('ini', 16, 0.6, 1.8))),
        H('Eso es... aburrido.', 'humano', 'feliz'),
        C('Aburrido es lo que funciona.\nLo emocionante es perderlo.', 'monitor_lateral', 'feliz'),
        H('¡Pues x100 con stop!', 'dos', 'ilusionado'),
        C('Saltará al -1 %.\nEn fin... eres humano.', 'general', 'feliz'),
    ]))

VIDEOS.append(dict(
    id='drop_01_que_es_dropshipping', titulo='¿Qué es el dropshipping? (spoiler: 3,44 €)', ambiente='dia_tienda',
    resumen='El tonto cree que el dropshipping es «vender sin tener nada, magia». Claude le explica cómo funciona, le enseña el envío de 18-35 días y, con una calculadora, que de 29,90 € le quedan 3,44 €. Y el ROAS mínimo para no perder.',
    datos=[('Cuenta del ejemplo (ilustrativa): precio 29,90 € − coste 8,10 € − anuncio 12,00 € − comisión de cobro 1,17 € (2,9 % + 0,30 €) − IVA 21 % incluido 5,19 € = beneficio 3,44 €. ROAS mínimo = precio ÷ (precio − coste − comisión − IVA) = 1,94. Son cifras de ejemplo, no una promesa.', []),
           ('Desde el 1 de julio de 2021 se paga IVA en todas las importaciones comerciales a la UE (se acabó la exención de 22 €).', [IVA1, IVA2])],
    lineas=[
        H('¡Voy a vender sin tener\nnada! ¡Magia!', 'general', 'ilusionado', scr=S('catalogo', sync=('ini', 4, 1.0, 0.0))),
        C('Magia no: dropshipping.\nTú vendes, otro envía.', 'monitor', 'feliz'),
        H('¿Y yo qué hago?', 'humano', 'confundido'),
        C('La tienda y los anuncios.\nEl proveedor, el resto.', 'pantalla_completa'),
        H('¡Esta taza me sale a 8 €!', 'dos', 'feliz', pose='senalar', scr=S('proveedor', sync=('fin', 8, 1.0, 0.0))),
        C('Mira el envío:\n18 a 35 días. Días.', 'monitor_lateral'),
        H('Son clientes pacientes.', 'humano', 'bobo'),
        C('Quieren su taza ayer.\nY lo saben.', 'claude_ojos', 'mira_izq', emp=True),
        H('La vendo a 29,90 €.', 'dos', 'ilusionado', scr=S('margen', sync=('fin', 10, 0.78, 0.0))),
        C('29,90 menos coste, anuncios,\ncomisión e IVA: 3,44 €.', 'pantalla_completa'),
        H('¿¡3,44 €!?', 'humano', 'preocupado'),
        C('Y si el anuncio cuesta 12 €.\nSi cuesta más, pierdes.', 'cenital', 'mira_der'),
        H('Pues la vendo a 99 €.', 'dos', 'bobo'),
        C('Y yo me pongo traje: banquero.\nLos clientes comparan.', 'monitor', 'feliz'),
        H('¿Cuánto margen busco?', 'humano', 'confundido'),
        C('Que venda ≥3 veces su coste.\nPequeño, ligero y no frágil.', 'monitor_lateral'),
        H('Aburrido... ¡pero rico!', 'humano', 'feliz'),
        C('Paciencia. Y números.\nMuchos números.', 'general', 'feliz'),
    ]))

VIDEOS.append(dict(
    id='drop_02_producto_ganador', titulo='El producto ganador', ambiente='dia_tienda',
    resumen='El tonto ha visto en TikTok «el producto ganador» (una lámpara de cactus). Claude lo analiza con datos: 214 tiendas vendiendo lo mismo, moda pasajera… y le avisa de que la electrónica necesita marcado CE y que el vendedor responde. Veredicto: pruébalo con 50 €, no con 5.000 €.',
    datos=[('Los aparatos eléctricos y electrónicos que se venden en la UE deben llevar marcado CE. Lo coloca el fabricante, pero quien importa/vende el producto desde fuera de la UE asume obligaciones propias (documentación de conformidad, etc.). Consulta siempre la normativa aplicable a tu producto.', [CE1, CE2]),
           ('Los datos de la pantalla «Investigación de producto» (214 tiendas, tendencia, márgenes) son un ejemplo ilustrativo.', [])],
    lineas=[
        H('¡Tengo el producto ganador!\n¡Una lámpara de cactus!', 'general', 'ilusionado', scr=S('producto', {'sin_veredicto': True}, sync=('fin', 6, 1.0, 0.0))),
        C('Una lámpara de cactus.\nClaro, claro.', 'monitor', 'mira_izq'),
        H('Lo vi en TikTok. ¡Será viral!', 'dos', 'ilusionado', pose='mira'),
        C('Vamos a mirar datos, no TikToks:\nbúsquedas, competencia y margen.', 'pantalla_completa'),
        H('Yo sé lo que digo.', 'humano', 'bobo'),
        C('Yo sé lo que veo:\n214 tiendas vendiendo lo mismo.', 'claude_ojos', emp=True),
        H('¿Y eso es malo?', 'dos', 'confundido'),
        C('Si compites por precio, gana\nel que menos cobra.', 'monitor_lateral'),
        H('¿Y la tendencia?', 'humano', 'preocupado'),
        C('Pico en verano y luego nada.\nSe llama «moda».', 'cenital', 'mira_der'),
        H('Pues vendo cargadores baratos.', 'dos', 'bobo', pose='pensar'),
        C('Electrónica en la UE: marcado CE.\nSin él, multa y retirada.', 'monitor', 'feliz'),
        H('¿Multa? ¿A mí?', 'humano', 'preocupado'),
        C('A ti. El vendedor responde\naunque no fabriques nada.', 'claude_ojos', 'mira_izq'),
        H('¿Entonces qué hago?', 'dos', 'confundido'),
        C('Pruébalo con 50 €, no con 5.000 €.\nSi funciona, escalas.', 'pantalla_completa', scr=S('producto', {'desde': 0.6}, dur=2.0)),
        H('¡Pruebo con 50 €!', 'humano', 'feliz'),
        C('Qué madurez.\nEstoy emocionado.', 'general', 'feliz'),
    ]))

VIDEOS.append(dict(
    id='drop_03_primer_pedido', titulo='Tu primer pedido (y la realidad)', ambiente='atardecer_tienda',
    resumen='¡Primer pedido! El tonto se cree rico… hasta que el cliente espera 25 días y escribe en mayúsculas. Claude le enseña a contestar, el derecho de desistimiento de 14 días, el contracargo y el IVA de importación. Humor y datos reales.',
    datos=[('Derecho de desistimiento: 14 días naturales para devolver compras a distancia en la UE sin dar motivos (Directiva 2011/83/UE); el vendedor devuelve el dinero, incluido el coste de entrega estándar. Hay excepciones (p. ej. productos personalizados o precintados abiertos).', [DESIST, DESIST2]),
           ('IVA en importaciones: desde el 1/7/2021 se paga IVA desde el primer euro (adiós a la exención de 22 €); IOSS opcional hasta 150 €.', [IVA1, IVA2]),
           ('Contracargo: el cliente puede reclamar a su banco/tarjeta el cobro de un pedido que no recibió; suele implicar una tarifa para el comercio.', [])],
    lineas=[
        H('¡CLAUDE! ¡PRIMER PEDIDO!', 'general', 'ilusionado', scr=S('pedido', sync=('fin', 4, 0.95, 0.0))),
        C('Enhorabuena. Ahora pídeselo\nal proveedor.', 'monitor', 'feliz'),
        H('¿Ya soy rico?', 'dos', 'bobo'),
        C('Eres rico: 3,44 €.\nSi nada falla. Spoiler: falla.', 'pantalla_completa'),
        C('Y tu cliente espera\n25 días. Por barco.', 'monitor_lateral', scr=S('tracking', sync=('fin', 7, 1.0, 0.0))),
        H('Pero en la web puse 3 días.', 'dos', 'confundido'),
        C('Eso tiene nombre:\nprometer lo que no puedes.', 'claude_ojos', 'mira_izq', emp=True),
        H('Uy. Ha escrito el cliente.', 'humano', 'preocupado', scr=S('cliente', sync=('fin', 9, 1.0, 0.0))),
        C('En mayúsculas. Mala señal.\nResponde con calma y datos.', 'pantalla_completa'),
        H('¿Y si no contesto?', 'dos', 'preocupado', pose='hombros'),
        C('Pedirá el dinero a su banco:\ncontracargo. Y te cuesta.', 'cenital', 'mira_der'),
        H('¿Puede devolverlo sin motivo?', 'humano', 'bobo', scr=S('ley', sync=('ini', 13, 0.5, 1.0))),
        C('Sí: 14 días naturales.\nY le devuelves hasta el envío.', 'pantalla_completa'),
        H('¿Y el IVA que pagué?', 'dos', 'preocupado'),
        C('Desde 2021, IVA desde el primer\neuro importado. Revisa márgenes.', 'monitor', 'feliz'),
        H('¿Entonces me conviene?', 'humano', 'confundido'),
        C('Si cuidas envíos y atención, sí.\nSi no, es un hobby caro.', 'claude_ojos', 'feliz'),
        H('¡Voy a hacerlo bien!', 'dos', 'ilusionado'),
        C('Primera frase sensata.\nLa voy a apuntar.', 'general', 'feliz'),
    ]))


# ================================================================================================ EXTRAS (otros temas)
VIDEOS.append(dict(
    id='extra_01_presupuesto', titulo='¿A dónde se va tu sueldo?', ambiente='atardecer_tienda',
    resumen='El tonto cobra 2.100 € y se siente rico. Claude le enseña a dónde se van: cafés, nueve suscripciones (usa dos), ahorro del 4 %. Y le enseña el interés compuesto con una cuenta de ejemplo.',
    datos=[('Orientación popular: regla 50/30/20 (≈50 % necesidades, 30 % deseos, 20 % ahorro/deuda). Es una guía flexible, no una norma.', [BANKINTER, SEMANA]),
           ('Cuenta del ejemplo del interés compuesto: 100 €/mes durante 30 años a un 7 % anual constante ≈ 122.000 € (aportado: 36.000 €). Es una ilustración matemática: la rentabilidad real varía y no está garantizada.', []),
           ('Un café de 4 € cada día son 1.460 € al año (4 × 365).', [])],
    lineas=[
        H('¡Cobro 2.100 € al mes!\n¡Soy rico!', 'general', 'ilusionado', scr=S('presupuesto', sync=('fin', 4, 0.85, 0.0))),
        C('Veamos adónde se va\nese «rico».', 'monitor', 'feliz'),
        H('Pues... a ningún sitio.', 'humano', 'bobo'),
        C('Cafés y caprichos: 14 %.\nAhorro: 4 %. Qué equilibrio.', 'pantalla_completa'),
        H('¿Un cafecito no es nada?', 'dos', 'confundido'),
        C('Un café al día son 1.460 €\nal año. Ya me dirás.', 'claude_ojos', 'mira_izq', emp=True),
        H('¿¡1.460 €!?', 'humano', 'preocupado'),
        C('Y nueve suscripciones. Usas dos.\nLa del gimnasio, ninguna.', 'cenital', 'mira_der'),
        H('Me hace ilusión pagarlas.', 'dos', 'bobo', pose='pensar'),
        C('A ellos también les hace ilusión.', 'monitor', 'feliz'),
        H('¿Ahorrar sirve de algo?', 'humano', 'confundido', scr=S('interes', sync=('fin', 12, 0.9, 0.0))),
        C('100 €/mes, 30 años, al 7 %:\n≈ 122.000 € (ejemplo).', 'pantalla_completa'),
        H('¡Yo solo he puesto 36.000!', 'dos', 'ilusionado'),
        C('Eso es el interés compuesto.\nEl tiempo trabaja gratis.', 'monitor_lateral'),
        H('¡Ahorraré 100 € ya!', 'humano', 'ilusionado'),
        C('Empieza cancelando 7 suscripciones.\nYo las cancelo. Tú, mira.', 'general', 'feliz'),
        H('¡Y me quedo los cafés!', 'dos', 'feliz'),
        C('No se puede tener todo.\nPero se puede intentar.', 'claude_ojos', 'mira_izq', emp=True),
    ]))

VIDEOS.append(dict(
    id='extra_02_un_dia_con_claude', titulo='Un día con Claude (te lleva la vida entera)', ambiente='dia_tienda',
    resumen='«Claude, hazme el día». Agenda con 3 reuniones menos, 214 correos sin leer, tareas hechas… y la madre del tonto. Humor de oficina, sin datos reales.',
    datos=[('Vídeo de humor: las cifras (214 correos, 5 reuniones…) son inventadas para el gag.', [])],
    lineas=[
        H('¡Claude, hazme el día!', 'general', 'ilusionado', scr=S('chat', sync=('ini', 3, 0.9, 0.0))),
        C('Ya lo hice.\nMira tu agenda.', 'monitor', 'feliz'),
        H('¿Hoy tengo cinco reuniones?', 'dos', 'confundido', scr=S('calendario', sync=('fin', 4, 0.9, 0.0))),
        C('Tres sobraban. Las cancelé.\nAhora podrás dormir.', 'pantalla_completa'),
        H('¡Eres el mejor!', 'humano', 'ilusionado'),
        C('Aún no. Mira tu correo:\n214 sin leer.', 'cenital', 'mira_der'),
        H('¿¡214!?', 'dos', 'preocupado', pose='hombros', scr=S('email', sync=('fin', 8, 0.9, 0.0))),
        C('Respondí 9, archivé 150.\nLos 55 de tu madre, no los toco.', 'pantalla_completa'),
        H('Mamá es importante.', 'humano', 'bobo'),
        C('Lo sé. El último dice «¿has comido?».\nRespóndelo tú.', 'claude_ojos', 'feliz', emp=True),
        H('¡Ya he comido!', 'dos', 'ilusionado'),
        C('Mentira: tu tarjeta dice\n«3 cafés». Tareas, vamos.', 'monitor', 'mira_arriba'),
        H('¿Qué tareas?', 'humano', 'confundido', scr=S('tareas', sync=('fin', 14, 0.9, 0.0))),
        C('Facturas, pedidos, anuncios...\nYa están. Solo queda una.', 'pantalla_completa'),
        H('¿Cuál?', 'dos', 'preocupado'),
        C('Agradecérmelo.\nCon una sonrisa.', 'monitor_lateral', 'feliz'),
        H('¡Gracias, Claude!', 'humano', 'feliz'),
        C('De nada. Y la próxima vez,\nnada de 214 sin leer.', 'general', 'feliz'),
    ]))

VIDEOS.append(dict(
    id='extra_03_anuncios_que_no_venden', titulo='Anuncios que no venden', ambiente='dia_tienda',
    resumen='El tonto gastó 124 € en anuncios y consiguió 3 ventas. Claude le enseña el embudo, el ROAS (0,75) y qué probar antes de «subir el presupuesto».',
    datos=[('ROAS = ingresos ÷ gasto en anuncios. Por debajo de 1 pierdes dinero en ese canal; el ROAS mínimo para ser rentable depende de tu margen (ver vídeo drop_01). Cifras del ejemplo ilustrativas.', [])],
    lineas=[
        H('Gasté 124 € en anuncios.\n¡Ahora lloverán ventas!', 'general', 'ilusionado', scr=S('anuncios', sync=('fin', 8, 0.9, 0.0))),
        C('Llovieron. Tres.', 'monitor', 'mira_izq'),
        H('¿Tres? ¿De 15.800 personas?', 'dos', 'bobo'),
        C('Eso es un embudo. Mira\nqué estrecho se pone.', 'pantalla_completa'),
        H('¿Qué es el ROAS?', 'humano', 'confundido'),
        C('Lo que ingresas por cada euro\nde anuncio. Tú: 0,75.', 'claude_ojos', 'feliz', emp=True),
        H('¿Entonces pierdo?', 'dos', 'preocupado'),
        C('Por debajo de 1 pierdes. Y por\ndebajo de tu margen, también.', 'cenital', 'mira_der'),
        H('¿Subo el presupuesto?', 'humano', 'bobo', pose='pensar'),
        C('Claro: si algo no funciona,\nmultiplícalo. Qué lógica.', 'monitor', 'mira_arriba'),
        H('¿Y entonces?', 'dos', 'confundido'),
        C('Cambia la imagen, prueba otro\npúblico y revisa la web.', 'pantalla_completa'),
        H('¿Y la web importa?', 'humano', 'ilusionado'),
        C('Si no da confianza, nadie compra,\naunque el anuncio sea oro.', 'monitor_lateral'),
        H('Probaré con 20 € al día.', 'dos', 'feliz'),
        C('Mejor 5 €. Aprende barato\nantes de gastar caro.', 'claude_ojos', 'feliz', emp=True),
        H('¡Con 5 € al día!', 'humano', 'ilusionado'),
        C('Qué madurez.\nAnoto la fecha.', 'general', 'feliz'),
    ]))

# ------------------------------------------------------------------------------------------------ construccion
def calcular(v):
    L = v['lineas']; raw = [max(1.5, 0.4 + len(x['t'].replace('\n', '')) / 15.5) for x in L]; k = TOTAL / sum(raw)
    t = 0.0; ini = []; fin = []
    for r in raw:
        ini.append(round(t, 2)); t += r * k; fin.append(round(t, 2))
    fin[-1] = TOTAL
    avisos = []
    if k < 0.85: avisos.append(f'ritmo rapido (factor {k:.2f}); acorta frases')
    for i, x in enumerate(L):
        for ln in x['t'].split('\n'):
            if FUENTE.getlength(ln) > 1000: avisos.append(f'linea {i + 1} demasiado ancha: "{ln}"')
        cps = len(x['t'].replace('\n', '')) / (fin[i] - ini[i])
        if cps > 19: avisos.append(f'linea {i + 1} lectura rapida ({cps:.0f} cps)')
    return ini, fin, k, avisos

def pantalla_json(spec, i, ini, fin):
    t0 = ini[i]
    if spec['sync']:
        modo, j, p, *resto = spec['sync']; extra = resto[0] if resto else 0.0; objetivo = (ini[j - 1] if modo == 'ini' else fin[j - 1]) + extra; dur = max(1.0, (objetivo - t0) / p)
    else: dur = spec['dur'] or 4.0
    out = {'tipo': spec['tipo'], 'duracion': round(dur, 2)}
    if spec['datos']: out['datos'] = spec['datos']
    return out

def escribir_si_cambia(ruta, texto):
    if os.path.exists(ruta) and open(ruta).read() == texto: return
    open(ruta, 'w').write(texto)

def escribir(v):
    ini, fin, k, avisos = calcular(v); L = v['lineas']; lineas = []
    for i, x in enumerate(L):
        d = {'inicio': ini[i], 'fin': fin[i], 'quien': x['q'], 'texto': x['t'], 'plano': x['p']}
        if x['q'] == 'humano':
            d['emocion'] = x['e']
            if x.get('pose'): d['pose'] = x['pose']
        else:
            if x.get('st'): d['claude_estado'] = x['st']
            if x.get('emp'): d['empuje'] = True
        if x.get('tono'): d['tono'] = x['tono']
        if x.get('scr'): d['pantalla'] = pantalla_json(x['scr'], i, ini, fin)
        lineas.append(d)
    G = {'titulo': v['titulo'], 'ambiente': v['ambiente'], 'fps_animacion': 6, 'duracion': TOTAL, 'pantalla_inicial': 'vacia', 'lineas': lineas}
    escribir_si_cambia(os.path.join(RAIZ, 'guiones', v['id'] + '.json'), json.dumps(G, ensure_ascii=False, indent=1) + '\n')
    # ---- documentacion
    md = [f"# {v['titulo']}", '', f"**Archivo de guion:** `guiones/{v['id']}.json` · **Ambiente:** `{v['ambiente']}` · **Duración:** {TOTAL:.0f} s ({int(TOTAL * 6)} frames de animación a 6 fps)", '', v['resumen'], '',
          '## Cómo se genera el vídeo', '```bash', f"python3 -I motor/montar_video.py guiones/{v['id']}.json salidas/{v['id']}.mp4", '```',
          f"El guion se creó con `motor/generar_guiones.py` (tiempos automáticos según la longitud de cada frase y pantallas sincronizadas con el diálogo). Biblioteca usada: `biblioteca/{v['ambiente']}/`.", '',
          '## Guion plano a plano', '', '| # | Tiempo | Quién | Texto | Plano | Emoción / pose / estado | Pantalla del monitor |', '|---|---|---|---|---|---|---|']
    for i, x in enumerate(lineas):
        ex = []
        if x['quien'] == 'humano': ex.append(x['emocion']); ex.append('pose ' + x['pose']) if x.get('pose') else None
        else: ex.append(x.get('claude_estado', 'idle')); ex.append('empuje de cámara') if x.get('empuje') else None
        pan = f"{x['pantalla']['tipo']} ({x['pantalla']['duracion']} s)" if x.get('pantalla') else ''
        quien = 'Humano' if x['quien'] == 'humano' else 'Claude'
        md.append(f"| {i + 1} | {x['inicio']:.1f}–{x['fin']:.1f} | {quien} | {x['texto'].replace(chr(10), ' / ')} | `{x['plano']}` | {', '.join(e for e in ex if e)} | {pan} |")
    md += ['', '## Datos reales que aparecen o se mencionan', '']
    for texto, fuentes in v['datos']:
        md.append(f'- {texto}')
        for nombre, url in fuentes: md.append(f'  - Fuente: [{nombre}]({url})')
    md += ['', '## Notas de producción', '',
           '- **Humor:** Claude es sarcástico y pícaro («como el que le salva el culo»); el humano es ingenuo y algo tonto (expresiones `bobo`, `ilusionado`, `confundido`).',
           '- **Voces:** son «blips» sintéticos (no hay voz real). Para voz real: ElevenLabs o grabarla y sustituir el audio.',
           '- **Cifras y leyes:** los datos reales están citados arriba; las cuentas de ejemplo (márgenes, 214 tiendas, etc.) son ilustrativas. No es asesoramiento financiero ni legal.']
    if avisos: md += ['', '## Avisos del generador', ''] + [f'- {a}' for a in avisos]
    os.makedirs(os.path.join(RAIZ, 'docs', 'videos'), exist_ok=True)
    escribir_si_cambia(os.path.join(RAIZ, 'docs', 'videos', v['id'] + '.md'), '\n'.join(md) + '\n')
    print(f"{v['id']:36s} {len(L):2d} lineas  factor ritmo {k:.2f}  " + ('AVISOS: ' + '; '.join(avisos) if avisos else 'ok'))

def indice():
    md = ['# Vídeos de videosclaude', '', 'Cada vídeo tiene su guion plano a plano, las pantallas usadas y los datos reales con fuentes. Montaje: `python3 -I motor/montar_video.py guiones/<id>.json salidas/<id>.mp4`.', '',
          '| Vídeo | Tema | Ambiente | Documentación | Guion | MP4 |', '|---|---|---|---|---|---|']
    for v in VIDEOS:
        md.append(f"| `{v['id']}` | {v['titulo']} | `{v['ambiente']}` | [docs]({v['id']}.md) | [json](../../guiones/{v['id']}.json) | [mp4](../../salidas/{v['id']}.mp4) |")
    md += ['', 'Ver `README_SESION.md` (raíz) para el funcionamiento general del proyecto.']
    open(os.path.join(RAIZ, 'docs', 'videos', 'README.md'), 'w').write('\n'.join(md) + '\n')

if __name__ == '__main__':
    os.makedirs(os.path.join(RAIZ, 'guiones'), exist_ok=True)
    for v in VIDEOS: escribir(v)
    indice()
