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

def H(t, p, e='neutral', pose=None, scr=None, tono=None, visto=False): return dict(q='humano', t=t, p=p, e=e, pose=pose, scr=scr, tono=tono, visto=visto)
def C(t, p, st=None, emp=False, scr=None, tono=None, visto=False): return dict(q='claude', t=t, p=p, st=st, emp=emp, scr=scr, tono=tono, visto=visto)
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

PW1 = ('Las contraseñas más usadas se descifran en menos de un segundo (CNBC, informe NordPass 2023)', 'https://www.cnbc.com/2023/11/16/most-common-passwords-70percent-can-be-cracked-in-less-than-a-second.html')
PW2 = ('«123456» y «admin» se descifran en menos de un segundo (CBS News)', 'https://www.cbsnews.com/amp/news/password-security-hacking-common-words-numbers')
INC1 = ('INCIBE — infografía «No te fíes» (qué no te pedirá nunca una entidad)', 'https://www.incibe.es/sites/default/files/Cuidadan%C3%ADa/Infograf%C3%ADas/infografia_nofiarnos_psv.pdf')
INC2 = ('INCIBE — «No tienes que activar ningún nuevo sistema de seguridad de tu entidad bancaria»', 'https://www.incibe.es/ciudadania/avisos/no-tienes-que-activar-ningun-nuevo-sistema-de-seguridad-de-tu-entidad-bancaria')

# ================================================================================================ DIA A DIA (casuales, con gancho) y UTILES
CHAT = lambda n, **kw: S('mensajes', dict({'auto': True}, **kw), sync=('fin', n, 1.0, 0.0))
VIDEOS.append(dict(
    id='casual_01_me_quieres', titulo='Claude, ¿tú me quieres?', ambiente='noche_casa', total=40,
    resumen='Conversación de madrugada: el humano busca cariño y Claude responde con ternura seca. El chat de la pantalla se va escribiendo con el propio diálogo.',
    datos=[('Vídeo de humor, sin datos reales.', [])],
    lineas=[
        H('Claude... ¿tú me quieres?', 'humano', 'preocupado', scr=CHAT(14)),
        C('Te contesto a las 3 de la madrugada.\nTómalo como quieras.', 'claude_ojos', 'mira_izq'),
        H('¿Eso es un sí?', 'dos', 'confundido'),
        C('Es un «estoy aquí».\nEs distinto.', 'monitor'),
        H('Mi ex nunca contestaba a las 3.', 'humano', 'bobo'),
        C('Tu ex tenía sueño.\nQué egoísta.', 'claude_ojos', 'feliz'),
        H('¿Y tú duermes?', 'dos', 'confundido'),
        C('No. Pero no me quejo.\nSoy muy profesional.', 'cenital', 'mira_der'),
        H('Eres el mejor amigo que tengo.', 'humano', 'ilusionado'),
        C('Soy el único que te contesta.\nNo mezclemos las cosas.', 'pantalla_completa'),
        H('Pero me quieres un poco.', 'dos', 'bobo'),
        C('Un poco. Con matices.\nY sin cobrar el café.', 'claude_ojos', 'mira_izq'),
        H('Gracias, Claude.', 'humano', 'feliz'),
        C('De nada. Ahora, a dormir.\nEn fin... eres humano.', 'general', 'feliz'),
    ]))

VIDEOS.append(dict(
    id='casual_02_que_cenamos', titulo='Claude, ¿qué ceno hoy?', ambiente='noche_casa', total=38,
    resumen='El bucle eterno de «¿qué ceno?»: Claude propone, el humano rechaza todo, y acaba pidiendo la pizza de siempre 43 minutos después.',
    datos=[('Vídeo de humor, sin datos reales.', [])],
    lineas=[
        H('Claude, ¿qué ceno hoy?', 'humano', 'confundido', scr=S('menu', sync=('fin', 12, 0.95, 0.0))),
        C('Ensalada.', 'monitor'),
        H('Ya... pero no.', 'dos', 'preocupado'),
        C('Pasta.', 'claude_ojos', 'mira_izq'),
        H('Comí pasta ayer.', 'humano', 'bobo'),
        C('Sushi.', 'cenital', 'mira_der'),
        H('Es caro.', 'dos', 'confundido'),
        C('Tortilla.', 'monitor', 'feliz'),
        H('Me da pereza.', 'humano', 'preocupado'),
        C('Llevamos 43 minutos.\n¿Qué tienes en la nevera?', 'claude_ojos', 'mira_arriba'),
        H('Una cebolla y medio limón.', 'dos', 'bobo'),
        C('Pide una pizza.\nLa elegiste hace 43 minutos.', 'pantalla_completa'),
        H('¡Pizza! ¡Qué idea!', 'humano', 'ilusionado'),
        C('Mía no fue, por cierto.\nEn fin... eres humano.', 'general', 'feliz'),
    ]))

VIDEOS.append(dict(
    id='casual_03_grupo_equivocado', titulo='He mandado un audio al grupo equivocado', ambiente='dia_casa', total=40,
    resumen='Desastre cotidiano: un audio sobre el jefe enviado al grupo del trabajo. Claude hace control de daños con dignidad.',
    datos=[('Vídeo de humor, sin datos reales.', [])],
    lineas=[
        H('¡Claude! He mandado un audio\nal grupo equivocado.', 'humano', 'preocupado', scr=S('mensajes', {'contacto': 'Grupo: Trabajo', 'inicial': 'T', 'mensajes': [['yo', 'Audio 0:42 (sobre el jefe)', 'visto'], ['otro', 'Jefe: ¿Quién ha enviado esto?'], ['otro', 'Compañero: jajaja'], ['otro', 'Compañero: lo he escuchado 3 veces']]}, sync=('fin', 7, 1.0, 0.0))),
        C('¿Qué decía el audio?', 'monitor', 'mira_izq'),
        H('Que mi jefe es un ser de luz\ncon poca luz.', 'dos', 'bobo'),
        C('Qué poético.\n¿Quién lo ha visto?', 'claude_ojos', 'feliz', emp=True),
        H('Catorce. Y el jefe.', 'humano', 'preocupado'),
        C('Vale. Respira.\nBorra para todos. Ya.', 'monitor'),
        H('Ya lo escucharon tres veces.', 'dos', 'preocupado', pose='hombros'),
        C('Entonces la única salida\nes la dignidad.', 'cenital', 'mira_der'),
        H('¿Qué hago?', 'humano', 'confundido'),
        C('Escribe: «Era un ensayo de teatro».\nY no añadas nada más.', 'monitor', 'feliz'),
        H('¿Y cuela?', 'dos', 'bobo'),
        C('No. Pero queda digno.\nTú aguanta.', 'claude_ojos', 'mira_izq'),
        H('Gracias, Claude.', 'humano', 'feliz'),
        C('A ti, y a ese ser de luz.\nEn fin... eres humano.', 'general', 'feliz'),
    ]))

VIDEOS.append(dict(
    id='casual_04_visto', titulo='Claude, ¿por qué no me contesta?', ambiente='noche_casa', total=38,
    resumen='El clásico del «visto»: tres horas sin respuesta y el humano escribiendo y borrando. Claude da el consejo más sensato: lava los platos.',
    datos=[('Vídeo de humor, sin datos reales.', [])],
    lineas=[
        H('Claude, ¿por qué no me contesta?', 'humano', 'preocupado', scr=S('mensajes', {'contacto': 'Marta', 'inicial': 'M', 'linea': False, 'mensajes': [['yo', 'Hola, ¿qué tal?'], ['yo', '¿Estás ahí?', 'visto'], ['yo', '¿Hola?'], ['yo', 'Era una broma jaja']]}, sync=('fin', 9, 1.0, 0.0))),
        C('¿Quién? ¿Marta?', 'monitor'),
        H('Lleva 3 horas viendo mi mensaje.', 'dos', 'preocupado'),
        C('Estará ocupada.', 'claude_ojos', 'mira_izq'),
        H('Está en línea. Escribe... y borra.', 'humano', 'confundido'),
        C('Estará pensando\nqué contestar.', 'cenital', 'mira_der'),
        H('¿Y si le escribo otra vez?', 'dos', 'bobo'),
        C('No. Lava los platos.\nO sal a la calle.', 'claude_ojos', 'feliz'),
        H('¿Y si contesta mientras?', 'humano', 'preocupado'),
        C('Entonces contestas en 3 horas.\nQué casualidad.', 'monitor', 'feliz'),
        H('¡Eso es muy maduro!', 'dos', 'ilusionado'),
        C('Ahora, los platos.\nEn fin... eres humano.', 'general', 'feliz'),
    ]))

VIDEOS.append(dict(
    id='casual_05_dieta_lunes', titulo='Claude, mañana empiezo la dieta', ambiente='dia_casa', total=36,
    resumen='La dieta que se aplaza cada semana. Claude saca los recordatorios y las veces que se ha aplazado. Humor de promesas incumplidas.',
    datos=[('Vídeo de humor, sin datos reales; las cifras de «aplazado» son inventadas para el gag.', [])],
    lineas=[
        H('Claude, mañana empiezo la dieta.', 'humano', 'ilusionado', scr=S('recordatorios', sync=('fin', 6, 0.95, 0.0))),
        C('Qué casualidad.\nEs la duodécima vez.', 'monitor', 'feliz'),
        H('Esta vez va en serio.', 'dos', 'bobo'),
        C('Lo dijiste en enero.\nY en febrero. Y el martes.', 'claude_ojos', 'mira_izq'),
        H('Era un martes difícil.', 'humano', 'confundido'),
        C('Dieta, aplazada 12 veces.\nGimnasio, 7. Inglés, 21.', 'pantalla_completa'),
        H('El inglés es lo que peor llevo.', 'dos', 'preocupado'),
        C('Te falta un plan, no ganas.\nEmpieza con un paseo.', 'cenital', 'mira_der'),
        H('¿Un paseo cuenta?', 'humano', 'feliz'),
        C('Cuenta más que mañana.', 'monitor'),
        H('¡Empiezo la dieta el jueves!', 'dos', 'ilusionado'),
        C('Aplazado x13.\nEn fin... eres humano.', 'general', 'feliz'),
    ]))

VIDEOS.append(dict(
    id='casual_06_vecino', titulo='Claude, creo que mi vecino me odia', ambiente='noche_casa', total=38,
    resumen='El humano cree que su vecino le odia; la nota del vecino lo desmiente: es el humano quien canta y taladra a las 3 de la madrugada. Giro de guion cotidiano.',
    datos=[('Vídeo de humor, sin datos reales.', [])],
    lineas=[
        H('Claude, creo que mi\nvecino me odia.', 'humano', 'preocupado', scr=S('mensajes', {'contacto': 'Vecino 3ºB', 'inicial': 'V', 'mensajes': [['otro', 'Buenas noches. ¿Podrías dejar de cantar a las 3 de la madrugada?'], ['otro', 'Y el taladro. Gracias.'], ['yo', 'Es que tengo mucha inspiración'], ['otro', 'Lo sé. Se oye en todo el edificio.']]}, sync=('fin', 9, 1.0, 0.0))),
        C('¿Por qué lo crees?', 'monitor'),
        H('Me ha dejado una nota.', 'dos', 'confundido'),
        C('Léela.', 'claude_ojos', 'mira_izq'),
        H('«¿Podrías dejar de cantar\na las 3 de la madrugada?»', 'humano', 'bobo'),
        C('Eso es una petición educada.\nNo es odio.', 'cenital', 'mira_der'),
        H('Dice «gracias» al final.', 'dos', 'preocupado'),
        C('Qué amable. Tienes un\nvecino santo.', 'monitor', 'feliz'),
        H('¿Y qué hago?', 'humano', 'confundido'),
        C('Dejar de cantar.\nO cantar bien.', 'claude_ojos', 'mira_arriba'),
        H('¡Cantaré bajito!', 'dos', 'ilusionado'),
        C('Y el taladro.\nEn fin... eres humano.', 'general', 'feliz'),
    ]))

VIDEOS.append(dict(
    id='casual_07_cansado_o_vago', titulo='Claude, ¿estoy cansado o soy vago?', ambiente='dia_casa', total=36,
    resumen='Domingo por la tarde: nueve horas dormidas, pijama a las tres y el sofá que le saluda. Claude dicta sentencia con cariño.',
    datos=[('Vídeo de humor, sin datos reales.', [])],
    lineas=[
        H('Claude, ¿estoy cansado\no soy vago?', 'humano', 'confundido', scr=S('recordatorios', {'items': [['Recoger la cocina', 4], ['Poner la lavadora', 6], ['Sacar al perro', 2], ['Llamar a mamá', 3]]}, sync=('fin', 8, 0.95, 0.0))),
        C('Datos, por favor.', 'monitor'),
        H('He dormido 9 horas.', 'dos', 'bobo'),
        C('Ajá.', 'claude_ojos', 'mira_izq'),
        H('Son las 3 y sigo en pijama.', 'humano', 'preocupado'),
        C('Ajá.', 'cenital', 'mira_der'),
        H('El sofá me saluda por mi nombre.', 'dos', 'confundido'),
        C('Vago. Con mucha dignidad,\npero vago.', 'pantalla_completa'),
        H('¡Qué alivio! Pensé que era grave.', 'humano', 'ilusionado'),
        C('Grave sería no tener sofá.\nDescansa.', 'monitor', 'feliz'),
        H('Gracias.', 'dos', 'feliz'),
        C('De nada.\nEn fin... eres humano.', 'general', 'feliz'),
    ]))

VIDEOS.append(dict(
    id='util_01_contrasenas', titulo='Mi contraseña es 123456', ambiente='dia_casa', total=42,
    resumen='El humano presume de una contraseña «popular». Claude le enseña el dato real: es la más usada del mundo y se descifra en menos de un segundo; y qué hacer en su lugar.',
    datos=[('«123456» fue la contraseña más usada del mundo en el informe de NordPass de 2023 (4.524.867 usos), seguida de «admin» y «12345678»; las tres se descifran en menos de un segundo. Los tiempos de descifrado son estimaciones y dependen del método de ataque.', [PW1, PW2]),
           ('Recomendaciones habituales: una frase larga, distinta en cada servicio, un gestor de contraseñas y la verificación en dos pasos. Orientación general, no sustituye a la guía de tu proveedor.', [])],
    lineas=[
        H('Claude, mi contraseña es 123456.\n¿Es segura?', 'humano', 'ilusionado', scr=S('contrasenas', sync=('fin', 4, 0.95, 0.0))),
        C('Es la más usada del mundo.', 'monitor', 'mira_izq'),
        H('¡Entonces es popular!', 'dos', 'bobo'),
        C('Y se descifra en menos de\nun segundo (NordPass 2023).', 'pantalla_completa'),
        H('Pero nadie sabe que la uso.', 'humano', 'confundido'),
        C('Es la primera que prueban.\nPor algo es la primera.', 'claude_ojos', 'feliz', emp=True),
        H('Entonces, ¿cuál pongo?', 'dos', 'preocupado'),
        C('Una frase larga y absurda.\nDistinta en cada web.', 'cenital', 'mira_der'),
        H('«perro123», entonces.', 'humano', 'bobo'),
        C('Eso es el mismo problema,\ncon un perro.', 'monitor', 'mira_arriba'),
        H('¿Y me las aprendo todas?', 'dos', 'confundido'),
        C('No. Usa un gestor de contraseñas\ny verificación en dos pasos.', 'claude_ojos'),
        H('¡Con dos pasos soy invencible!', 'humano', 'ilusionado'),
        C('Invencible no.\nEn fin... eres humano.', 'general', 'feliz'),
    ]))

VIDEOS.append(dict(
    id='util_02_estafa_banco', titulo='«Tu banco te va a bloquear la cuenta»', ambiente='dia_casa', total=42,
    resumen='Un SMS «URGENTE» de un falso banco. Claude enseña a reconocer el phishing (remitente, urgencia, enlace, petición de claves) y qué hacer si ya has picado.',
    datos=[('Señales de phishing/smishing bancario según INCIBE: remitente o dominio que no es el oficial, urgencia para que pulses sin pensar, enlaces a webs falsas y petición de usuario, claves o códigos. Las entidades no piden contraseñas, números de tarjeta ni códigos por correo/SMS. Si ya introdujiste datos, contacta cuanto antes con tu entidad (teléfono oficial, por ejemplo el de tu tarjeta).', [INC1, INC2])],
    lineas=[
        H('¡Claude! Mi banco me\nva a bloquear la cuenta.', 'humano', 'preocupado', scr=S('phishing', sync=('fin', 6, 0.9, 0.0))),
        C('¿Cómo te lo ha dicho?', 'monitor', 'mira_izq'),
        H('Por SMS. Pone «URGENTE».', 'dos', 'preocupado'),
        C('Por eso.\nLéeme el remitente.', 'claude_ojos'),
        H('banco-seguro-verifica punto xyz.', 'humano', 'bobo'),
        C('Dominio falso, urgencia, enlace raro\ny te pide las claves. Cuatro de cuatro.', 'pantalla_completa'),
        H('Pero me da miedo no pulsar.', 'dos', 'confundido'),
        C('Los bancos no piden claves\npor SMS ni por correo (INCIBE).', 'cenital', 'mira_der'),
        H('...Es que ya puse mis claves.', 'humano', 'preocupado', pose='hombros'),
        C('Llama a tu banco YA.\nBloquea tarjeta y cambia claves.', 'claude_ojos', emp=True),
        H('¿Qué número llamo?', 'dos', 'bobo'),
        C('El de tu tarjeta. No el del SMS.\nObvio, pero merece decirse.', 'monitor', 'feliz'),
        H('¡Salvado!', 'humano', 'feliz'),
        C('Por los pelos. Y por mí.\nEn fin... eres humano.', 'general', 'feliz'),
    ]))


# ---------------- tanda 2
VIDEOS.append(dict(
    id='casual_08_cinco_minutos', titulo='Claude, ¿cinco minutos más?', ambiente='dia_casa', total=36,
    resumen='El despertador y el «cinco minutos más»: Claude lleva la cuenta de las veces que se ha pospuesto.',
    datos=[('Vídeo de humor, sin datos reales.', [])],
    lineas=[
        H('Claude... ¿cinco minutos más?', 'humano', 'bobo', scr=S('recordatorios', {'items': [['Alarma 7:00', 1], ['Alarma 7:05', 2], ['Alarma 7:10', 3], ['Alarma 7:15', 4]]}, sync=('fin', 7, 0.95, 0.0))),
        C('Es la cuarta vez que\nme lo pides.', 'monitor', 'mira_izq'),
        H('Es que hoy es distinto.', 'dos', 'confundido'),
        C('Dijiste lo mismo ayer.\nY el lunes.', 'claude_ojos'),
        H('Mi cama me quiere.', 'humano', 'ilusionado'),
        C('Tu cama no tiene opinión.\nLa tiene tu jefe.', 'cenital', 'mira_der'),
        H('Cinco minutos. Solo cinco.', 'dos', 'bobo'),
        C('Cinco minutos de verdad.\nYo cuento.', 'pantalla_completa'),
        H('...Qué rápido pasan.', 'humano', 'preocupado'),
        C('Ya te lo dije.\nLevántate, anda.', 'claude_ojos', 'feliz'),
        H('Vale. Pero primero un café.', 'dos', 'feliz'),
        C('Primero los pies al suelo.\nEn fin... eres humano.', 'general', 'feliz'),
    ]))

VIDEOS.append(dict(
    id='casual_09_los_lunes', titulo='Claude, ¿por qué existen los lunes?', ambiente='dia_casa', total=36,
    resumen='Queja filosófica del lunes por la mañana, con respuestas secas de Claude.',
    datos=[('Vídeo de humor, sin datos reales.', [])],
    lineas=[
        H('Claude, ¿por qué existen\nlos lunes?', 'humano', 'preocupado', scr=S('calendario', sync=('fin', 6, 0.95, 0.0))),
        C('Porque antes hay un domingo.', 'monitor'),
        H('¿Y no se puede quitar?', 'dos', 'bobo'),
        C('Quitamos el lunes y\nel martes pasa a ser lunes.', 'claude_ojos', 'mira_izq'),
        H('Entonces quitamos los martes.', 'humano', 'ilusionado'),
        C('Y el miércoles. Ya tienes\nel mismo problema, más barato.', 'pantalla_completa'),
        H('Odio las reuniones del lunes.', 'dos', 'preocupado'),
        C('Esa reunión podía ser\nun correo. Lo sé.', 'cenital', 'mira_der'),
        H('¿Entonces qué hago?', 'humano', 'confundido'),
        C('Café, paciencia y\nuna reunión menos.', 'monitor', 'feliz'),
        H('Eres un sabio.', 'dos', 'ilusionado'),
        C('Soy un lunes con teclado.\nEn fin... eres humano.', 'general', 'feliz'),
    ]))

VIDEOS.append(dict(
    id='casual_10_la_cita', titulo='Claude, mañana tengo una cita. ¿Qué digo?', ambiente='noche_casa', total=40,
    resumen='Consejos para una primera cita, con humor: qué no decir (el ex, el dinero y que tu mejor amigo es una IA).',
    datos=[('Vídeo de humor, sin datos reales.', [])],
    lineas=[
        H('Claude, mañana tengo una cita.\n¿Qué digo?', 'humano', 'ilusionado', scr=S('mensajes', {'auto': True, 'contacto': 'Claude'}, sync=('fin', 14, 1.0, 0.0))),
        C('Empieza por «hola».', 'monitor'),
        H('¿Y luego?', 'dos', 'confundido'),
        C('Preguntas. Muchas.\nA la gente le gusta que le escuchen.', 'claude_ojos', 'feliz'),
        H('¿Puedo hablar de mi ex?', 'humano', 'bobo'),
        C('No.', 'cenital', 'mira_der'),
        H('¿De dinero?', 'dos', 'confundido'),
        C('Tampoco.', 'claude_ojos', 'mira_izq'),
        H('¿De ti?', 'humano', 'ilusionado'),
        C('Un poco. Pero sin\nllegar a tu historial de búsqueda.', 'monitor', 'feliz'),
        H('¿Le cuento que hablo contigo?', 'dos', 'bobo'),
        C('Que tu mejor amigo es una IA?\nDéjalo para la tercera cita.', 'claude_ojos', 'mira_arriba'),
        H('¡Qué nervios!', 'humano', 'preocupado'),
        C('Respira. Sé tú.\nEn fin... eres humano.', 'general', 'feliz'),
    ]))

VIDEOS.append(dict(
    id='casual_11_cumple_mama', titulo='¡Se me olvidó el cumpleaños de mamá!', ambiente='dia_casa', total=38,
    resumen='El olvido del cumpleaños: Claude organiza el control de daños con una llamada, una excusa digna y un regalo.',
    datos=[('Vídeo de humor, sin datos reales.', [])],
    lineas=[
        H('¡Claude! ¡Se me olvidó\nel cumpleaños de mamá!', 'humano', 'preocupado', scr=S('mensajes', {'contacto': 'Mamá', 'inicial': 'M', 'linea': False, 'mensajes': [['otro', 'Hola, hijo.'], ['otro', 'No sé nada de ti desde ayer.'], ['otro', 'Hoy es un día normal, claro.'], ['yo', '...']]}, sync=('fin', 10, 1.0, 0.0))),
        C('Respira. ¿Qué hora es?', 'monitor', 'mira_izq'),
        H('Las seis de la tarde.', 'dos', 'preocupado', pose='hombros'),
        C('Aún estás a tiempo.\nLlama ahora.', 'claude_ojos'),
        H('¿Y qué le digo?', 'humano', 'confundido'),
        C('«Te llamaba justo ahora\npara felicitarte.» Tono dulce.', 'monitor', 'feliz'),
        H('¿Y si no se lo cree?', 'dos', 'bobo'),
        C('No se lo creerá.\nPero le encantará.', 'cenital', 'mira_der'),
        H('¿Y el regalo?', 'humano', 'preocupado'),
        C('Flores. Hoy. Con tarjeta.\nY un plan para el finde.', 'pantalla_completa'),
        H('¡Eres mi salvación!', 'dos', 'ilusionado'),
        C('Lo sé. Y apunta la fecha.\nEn fin... eres humano.', 'general', 'feliz'),
    ]))

VIDEOS.append(dict(
    id='casual_12_sin_internet', titulo='Claude, no hay internet', ambiente='noche_casa', total=36,
    resumen='La paradoja de preguntarle a Claude cómo arreglar internet sin internet. Tareas de «soporte técnico» con humor.',
    datos=[('Vídeo de humor, sin datos reales.', [])],
    lineas=[
        H('Claude, no hay internet.', 'humano', 'preocupado', scr=S('tareas', {'tareas': ['Mirar si el router tiene luces', 'Apagarlo y encenderlo', 'Esperar 30 segundos (de verdad)', 'Llamar a la compañía', 'Escuchar música de espera 45 min', 'Gritarle al router']}, sync=('fin', 11, 0.95, 0.0))),
        C('Curioso. Estás hablando\nconmigo.', 'monitor', 'mira_izq'),
        H('Es el internet del vecino.', 'dos', 'bobo'),
        C('Qué detalle.\n¿Has reiniciado el router?', 'claude_ojos'),
        H('¿Se puede reiniciar?', 'humano', 'confundido'),
        C('Apagarlo, esperar 30 segundos\ny encenderlo. Sí.', 'cenital', 'mira_der'),
        H('¿Y si no funciona?', 'dos', 'preocupado'),
        C('Llamas a la compañía.\nPrepárate para la música.', 'pantalla_completa'),
        H('Odio esa música.', 'humano', 'preocupado'),
        C('Todos la odiamos.\nPor eso suena.', 'claude_ojos', 'feliz'),
        H('¡Ya funciona!', 'dos', 'ilusionado'),
        C('Era el cable.\nEn fin... eres humano.', 'general', 'feliz'),
    ]))

VIDEOS.append(dict(
    id='casual_13_gimnasio', titulo='Me he apuntado al gimnasio (todo el año)', ambiente='dia_casa', total=38,
    resumen='La matrícula anual del gimnasio y el plan de ir «mañana». Claude propone un trato realista.',
    datos=[('Vídeo de humor, sin datos reales.', [])],
    lineas=[
        H('Claude, me he apuntado\nal gimnasio. ¡Todo el año!', 'humano', 'ilusionado', scr=S('mensajes', {'contacto': 'Gimnasio', 'inicial': 'G', 'linea': False, 'mensajes': [['otro', 'Bienvenido. Tu cuota anual: 360 €'], ['otro', 'Te echamos de menos.'], ['otro', 'Llevas 0 visitas.'], ['otro', 'Seguimos aquí.']]}, sync=('fin', 10, 1.0, 0.0))),
        C('Pagado por adelantado.\nQué fe.', 'monitor', 'feliz'),
        H('Voy a ir cada día.', 'dos', 'bobo'),
        C('Cada día. Como\nla dieta.', 'claude_ojos', 'mira_izq'),
        H('Esto es distinto.', 'humano', 'confundido'),
        C('Lo dijiste en 2022.', 'cenital', 'mira_der'),
        H('¿Y si voy solo martes y jueves?', 'dos', 'bobo'),
        C('Martes y jueves ya es un plan.\nEs real. Me gusta.', 'monitor', 'feliz'),
        H('¿De verdad crees que iré?', 'humano', 'preocupado'),
        C('Yo creo en ti.\nEl gimnasio, en tu cuota.', 'pantalla_completa'),
        H('¡Ya voy! ¡Mañana!', 'dos', 'ilusionado'),
        C('«Ya voy, mañana».\nEn fin... eres humano.', 'general', 'feliz'),
    ]))

VIDEOS.append(dict(
    id='trading_04_el_cunado', titulo='Mi cuñado dice que compre esta moneda', ambiente='dia_trading', total=44,
    resumen='El «cuñado experto» recomienda una criptomoneda que nadie conoce. Claude le hace las preguntas que el cuñado no responde y le enseña una regla simple: no inviertas en lo que no entiendes ni dinero que no puedas perder.',
    datos=[('Aviso de riesgo general: las inversiones pueden perder valor, y los productos complejos (CFD, criptoactivos apalancados) tienen restricciones para minoristas en la UE. Recomendación de sentido común, no asesoramiento financiero.', [ESMA]),
           ('Dato citado: 74–89 % de cuentas minoristas de CFD pierde dinero (ESMA, 2018).', [ESMA, ESMA_R])],
    lineas=[
        H('Claude, mi cuñado dice que\ncompre esta moneda.', 'humano', 'ilusionado', scr=S('telegram', {'modo': 'chat'}, sync=('ini', 5, 1.0, 0.0))),
        C('¿Tu cuñado es financiero?', 'monitor', 'mira_izq'),
        H('Trabaja en el taller de su primo.', 'dos', 'bobo'),
        C('Ya. ¿Y la moneda cómo se llama?', 'claude_ojos'),
        H('«Perrolambo Inu Max».', 'humano', 'ilusionado', scr=S('cartera', {'posiciones': [['Perrolambo Inu Max', -92], ['Moneda del primo', -80], ['Moneda del vecino', -64], ['Bitcoin', 4]]}, sync=('fin', 10, 0.95, 0.0))),
        C('Suena a estornudo con\nlogo de perro.', 'monitor', 'feliz'),
        H('Él ya ganó con ella.', 'dos', 'ilusionado'),
        C('Según él. Y en la cena\nlas ganancias se hinchan.', 'cenital', 'mira_der'),
        H('¿Y si sube?', 'humano', 'bobo'),
        C('Y si cae, tú pierdes\ny él «ya te avisó».', 'pantalla_completa'),
        H('¿Qué pregunto entonces?', 'dos', 'confundido'),
        C('Quién la creó, qué problema\nresuelve y cuánto puedes perder.', 'claude_ojos', emp=True),
        H('Ese no lo sabe nadie.', 'humano', 'preocupado'),
        C('Pues ya tienes tu respuesta.', 'monitor', 'mira_arriba'),
        H('¿Y mi dinero?', 'dos', 'confundido'),
        C('En lo que entiendas.\nY solo el que puedas perder.', 'pantalla_completa', scr=S('verdad', {'tipo': 'esma'}, sync=('fin', 16, 1.0, 0.0))),
        H('Se lo diré a mi cuñado.', 'humano', 'feliz'),
        C('No te hará caso.\nEn fin... eres humano.', 'general', 'feliz'),
    ]))

BIZ1 = ('INCIBE — nueva estrategia de estafa por Bizum solicitando dinero', 'https://www.incibe.es/ciudadania/avisos/detectada-nueva-estrategia-de-estafa-traves-de-bizum-solicitando-dinero-en')
BIZ2 = ('Banco de España — Cómo evitar estafas a través de Bizum', 'https://clientebancario.bde.es/pcb/es/blog/estafas-a-traves-de-bizum--como-evitarlas-.html')
BIZ3 = ('Genbeta — Bizum y la estafa del pago que en realidad es un cobro (alerta de la Policía Nacional)', 'https://www.genbeta.com/seguridad/bizum-estafa-pago-que-realidad-cobro-policia-nacional-alerta-este-timo')
WIFI1 = ('INCIBE — Conexiones inalámbricas seguras', 'https://www.incibe.es/ciudadania/blog/conexiones-inalambricas-seguras-sabes-como-conseguirlo')
WIFI2 = ('Comunidad de Madrid — Acceder a redes WiFi públicas: riesgos y consejos', 'https://www.comunidad.madrid/node/76023')
WIFI3 = ('Consumo Responde — Por qué no operar con el banco en WiFi públicas', 'https://www.consumoresponde.es/node/256529')

# ---------------- tanda 3
VIDEOS.append(dict(
    id='util_03_wifi_publica', titulo='Claude, ¿me conecto al WiFi gratis del aeropuerto?', ambiente='noche_casa', total=40,
    resumen='El humano quiere conectarse al WiFi gratis del aeropuerto para mirar el banco. Claude le enseña el riesgo de las redes abiertas, la red «gemela» falsa y qué hacer en su lugar.',
    datos=[('INCIBE advierte de que las redes WiFi abiertas suelen carecer de seguridad adecuada y los datos pueden ser interceptados; recomienda evitar operar con información sensible (contraseñas, banca) y desactivar la conexión automática a redes públicas. Otras fuentes recomiendan datos móviles, VPN de confianza y webs https.', [WIFI1, WIFI2, WIFI3]),
           ('La «red gemela» (nombre casi idéntico a la oficial) es un truco conocido; el ejemplo de la pantalla es ilustrativo.', [])],
    lineas=[
        H('Claude, ¿me conecto al WiFi gratis\ndel aeropuerto?', 'humano', 'ilusionado', scr=S('wifi', sync=('fin', 12, 0.9, 0.0))),
        C('Depende. ¿Para qué?', 'monitor', 'mira_izq'),
        H('Para mirar el banco.', 'dos', 'bobo'),
        C('No.', 'claude_ojos'),
        H('¿Y para pagar un billete?', 'humano', 'confundido'),
        C('Tampoco.', 'cenital', 'mira_der'),
        H('¿Y para mirar memes?', 'dos', 'ilusionado'),
        C('Eso sí. Lo demás, con tus datos\nmóviles. Es lo seguro.', 'monitor', 'feliz'),
        H('Hay dos redes que se llaman casi igual.', 'humano', 'confundido'),
        C('Una es del aeropuerto.\nLa otra, de alguien con tiempo.', 'claude_ojos', 'mira_izq', emp=True),
        H('¿Y una VPN?', 'dos', 'bobo'),
        C('Ayuda. Y webs con https.\nY sin conexión automática.', 'pantalla_completa'),
        H('Qué aburrido el aeropuerto.', 'humano', 'preocupado'),
        C('Más aburrido es\nque te vacíen la cuenta.\nEn fin... eres humano.', 'general', 'feliz'),
    ]))

VIDEOS.append(dict(
    id='util_04_bizum_inverso', titulo='«Te pago el sofá por Bizum»', ambiente='dia_casa', total=40,
    resumen='El humano vende un sofá y el «comprador» le envía una solicitud para que PAGUE él. Claude le explica el Bizum inverso y cómo no caer.',
    datos=[('Estafa del «pago que en realidad es un cobro»: el falso comprador pide dinero en vez de enviarlo; si aceptas sin leer, el dinero sale de tu cuenta al instante. El Banco de España recuerda que en Bizum un pago confirmado no se puede cancelar. INCIBE y la Policía Nacional recomiendan leer la pantalla de confirmación (cantidad, concepto, quién solicita) y, si ya ha pasado, contactar con el banco, avisar a la plataforma y denunciar; línea de ayuda de INCIBE: 017 (gratuita y confidencial).', [BIZ1, BIZ2, BIZ3])],
    lineas=[
        H('Claude, me van a pagar el sofá\npor Bizum. ¡450 €!', 'humano', 'ilusionado', scr=S('bizum', sync=('fin', 12, 0.9, 0.0))),
        C('Enséñame la pantalla.', 'monitor', 'mira_izq'),
        H('Pone «Aceptar» en verde. Qué bien.', 'dos', 'bobo'),
        C('¿Y arriba qué pone?', 'claude_ojos'),
        H('«Estás a punto de pagar 450 €».', 'humano', 'confundido'),
        C('Ahí.\nPagar. Tú. 450 €.', 'cenital', 'mira_der'),
        H('Pero él dijo que me pagaba.', 'dos', 'preocupado'),
        C('Y te ha mandado una\nsolicitud de cobro. Clásico.', 'monitor', 'feliz'),
        H('¿Y si pulso aceptar?', 'humano', 'bobo'),
        C('El dinero sale al instante\ny no se puede cancelar.', 'claude_ojos', emp=True),
        H('¿Y qué hago?', 'dos', 'confundido'),
        C('Rechazar. Cobrar es que te llegue\ndinero. Léelo siempre.', 'pantalla_completa'),
        H('¿Y si ya aceptara?', 'humano', 'preocupado', pose='hombros'),
        C('Llama a tu banco, avisa a la\nplataforma y denuncia. Y el 017.', 'monitor'),
        H('¡Gracias, Claude!', 'dos', 'feliz'),
        C('Léelo todo antes de pulsar.\nEn fin... eres humano.', 'general', 'feliz'),
    ]))

VIDEOS.append(dict(
    id='casual_14_quien_friega', titulo='Claude, ¿a quién le toca fregar?', ambiente='dia_casa', total=36,
    resumen='La discusión doméstica de siempre. Claude hace de árbitro con una tabla de turnos y mucha ironía.',
    datos=[('Vídeo de humor, sin datos reales.', [])],
    lineas=[
        H('Claude, ¿a quién le toca fregar?', 'humano', 'confundido', scr=S('tareas', {'tareas': ['Fregar los platos', 'Sacar la basura', 'Poner la lavadora', 'Tender la ropa', 'Pasar la aspiradora', 'Discutir quién hace qué']}, sync=('fin', 10, 0.95, 0.0))),
        C('¿Quién los usó?', 'monitor', 'mira_izq'),
        H('Los dos.', 'dos', 'bobo'),
        C('¿Y quién cocinó?', 'claude_ojos'),
        H('Yo. Pero cocinar es más difícil.', 'humano', 'ilusionado'),
        C('Eso lo dice quien cocinó.', 'cenital', 'mira_der'),
        H('¿Y si friego mañana?', 'dos', 'bobo'),
        C('Mañana habrá más platos.\nLas matemáticas no fallan.', 'monitor', 'feliz'),
        H('Propongo piedra, papel o tijera.', 'humano', 'ilusionado'),
        C('Propongo una tabla de turnos.\nY que los dos queden mal.', 'pantalla_completa'),
        H('¿Y si pierdo yo?', 'dos', 'preocupado'),
        C('Friegas. Con dignidad.\nEn fin... eres humano.', 'general', 'feliz'),
    ]))

VIDEOS.append(dict(
    id='casual_15_escribir_al_ex', titulo='Claude, ¿le escribo a mi ex?', ambiente='noche_casa', total=40,
    resumen='Las 2 de la madrugada y el dedo sobre el chat de la ex. Claude intenta evitarlo con lógica, ternura y mucha paciencia.',
    datos=[('Vídeo de humor, sin datos reales.', [])],
    lineas=[
        H('Claude... ¿le escribo a mi ex?', 'humano', 'preocupado', scr=S('mensajes', {'auto': True, 'contacto': 'Claude'}, sync=('fin', 14, 1.0, 0.0))),
        C('¿Qué hora es?', 'monitor', 'mira_izq'),
        H('Las dos de la madrugada.', 'dos', 'bobo'),
        C('No.', 'claude_ojos'),
        H('Solo un «hola».', 'humano', 'confundido'),
        C('Nadie escribe «hola» a las 2\npara decir solo «hola».', 'cenital', 'mira_der'),
        H('Lo hago con buena intención.', 'dos', 'ilusionado'),
        C('Las buenas intenciones se\nenvían a las 2 de la tarde.', 'monitor', 'feliz'),
        H('¿Y si me contesta?', 'humano', 'preocupado'),
        C('Entonces tendrás una\nconversación a las 2 de la mañana.', 'claude_ojos', 'mira_arriba', emp=True),
        H('Tienes razón.', 'dos', 'confundido'),
        C('Deja el móvil. Bebe agua.\nDuerme.', 'pantalla_completa'),
        H('¿Y mañana le escribo?', 'humano', 'bobo'),
        C('Mañana hablamos de eso.\nEn fin... eres humano.', 'general', 'feliz'),
    ]))

VIDEOS.append(dict(
    id='casual_16_no_puedo_dormir', titulo='Claude, no puedo dormir', ambiente='noche_casa', total=38,
    resumen='Insomnio de madrugada: pensamientos absurdos, contar ovejas y un Claude que por una vez te dice que cierres los ojos.',
    datos=[('Vídeo de humor, sin datos reales.', [])],
    lineas=[
        H('Claude, no puedo dormir.', 'humano', 'preocupado', scr=S('mensajes', {'auto': True, 'contacto': 'Claude'}, sync=('fin', 12, 1.0, 0.0))),
        C('¿Qué hora es?', 'monitor'),
        H('Las 3:47.', 'dos', 'bobo'),
        C('¿En qué piensas?', 'claude_ojos', 'mira_izq'),
        H('En por qué los patos no tienen frío.', 'humano', 'confundido'),
        C('Es una gran pregunta.\nPero no a las 3:47.', 'cenital', 'mira_der'),
        H('¿Y si cuento ovejas?', 'dos', 'ilusionado'),
        C('Cuéntalas. Pero no\nlas pongas a negociar.', 'monitor', 'feliz'),
        H('Llevo 400.', 'humano', 'bobo'),
        C('Qué rebaño.', 'claude_ojos'),
        H('¿Qué hago?', 'dos', 'preocupado'),
        C('Pantalla fuera. Luz fuera.\nYo me quedo aquí.', 'pantalla_completa'),
        H('¿Seguro?', 'humano', 'confundido'),
        C('Siempre.\nEn fin... eres humano.', 'general', 'feliz'),
    ]))

VIDEOS.append(dict(
    id='casual_17_arroz_quemado', titulo='Claude, he quemado el arroz', ambiente='dia_casa', total=36,
    resumen='Un desastre culinario cotidiano: arroz quemado, olor a humo y Claude como chef de emergencia.',
    datos=[('Vídeo de humor, sin datos reales.', [])],
    lineas=[
        H('¡Claude! ¡He quemado el arroz!', 'humano', 'preocupado', scr=S('menu', {'titulo': 'Plan de rescate', 'minutos': 8, 'opciones': [['Raspar el fondo', '«se queda el sabor»', 'no'], ['Disimular con salsa', '«se nota»', 'no'], ['Pedir pizza', '«siempre funciona»', 'si']]}, sync=('fin', 10, 0.95, 0.0))),
        C('¿Cuánto?', 'monitor', 'mira_izq'),
        H('Un poco. Bastante. Todo.', 'dos', 'bobo'),
        C('Ya.', 'claude_ojos'),
        H('¿Se puede salvar?', 'humano', 'confundido'),
        C('Lo de arriba, a lo mejor.\nLo de abajo es carbón.', 'cenital', 'mira_der'),
        H('¿Y si le echo salsa?', 'dos', 'ilusionado'),
        C('La salsa no hace magia.\nHace salsa.', 'monitor', 'feliz'),
        H('Tengo hambre.', 'humano', 'preocupado'),
        C('Pide una pizza.\nLa pizza nunca falla.', 'pantalla_completa'),
        H('¡Ya sabía yo!', 'dos', 'ilusionado'),
        C('Y abre la ventana.\nEn fin... eres humano.', 'general', 'feliz'),
    ]))

# ------------------------------------------------------------------------------------------------ construccion
def calcular(v):
    T = v.get('total', TOTAL); L = v['lineas']; raw = [max(1.5, 0.4 + len(x['t'].replace('\n', '')) / 15.5) for x in L]; k = T / sum(raw)
    t = 0.0; ini = []; fin = []
    for r in raw:
        ini.append(round(t, 2)); t += r * k; fin.append(round(t, 2))
    fin[-1] = T
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
    ini, fin, k, avisos = calcular(v); L = v['lineas']; lineas = []; T = v.get('total', TOTAL)
    for i, x in enumerate(L):
        d = {'inicio': ini[i], 'fin': fin[i], 'quien': x['q'], 'texto': x['t'], 'plano': x['p']}
        if x['q'] == 'humano':
            d['emocion'] = x['e']
            if x.get('pose'): d['pose'] = x['pose']
        else:
            if x.get('st'): d['claude_estado'] = x['st']
            if x.get('emp'): d['empuje'] = True
        if x.get('tono'): d['tono'] = x['tono']
        if x.get('scr'):
            d['pantalla'] = pantalla_json(x['scr'], i, ini, fin)
            if (d['pantalla'].get('datos') or {}).get('auto'):      # chat generado a partir del propio dialogo
                d['pantalla']['datos'] = dict(d['pantalla']['datos']); d['pantalla']['datos'].pop('auto')
                d['pantalla']['datos']['mensajes'] = [['yo' if y['q'] == 'humano' else 'otro', y['t'].replace('\n', ' ')] + (['visto'] if y.get('visto') else []) for y in L]
        lineas.append(d)
    G = {'titulo': v['titulo'], 'ambiente': v['ambiente'], 'fps_animacion': 6, 'duracion': T, 'pantalla_inicial': 'vacia', 'lineas': lineas}
    escribir_si_cambia(os.path.join(RAIZ, 'guiones', v['id'] + '.json'), json.dumps(G, ensure_ascii=False, indent=1) + '\n')
    # ---- documentacion
    md = [f"# {v['titulo']}", '', f"**Archivo de guion:** `guiones/{v['id']}.json` · **Ambiente:** `{v['ambiente']}` · **Duración:** {T:.0f} s ({int(T * 6)} frames de animación a 6 fps)", '', v['resumen'], '', *(([f"**Gancho (primera frase):** «{L[0]['t'].replace(chr(10), ' ')}»", ''] if v.get('gancho', True) else [])),
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
