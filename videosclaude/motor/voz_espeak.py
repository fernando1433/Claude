"""Voz sintetica OFFLINE con eSpeak NG (libreria que viene en la rueda de PyPI `espeakng-loader`). Voz robotica pero inteligible, en español.
    from voz_espeak import sintetizar
    pcm, sr = sintetizar('Hola, mundo', voz='es', tono=50, velocidad=170)   # -> numpy int16 mono, 22050 Hz
"""
import ctypes, os
import numpy as np
import espeakng_loader as _e

_lib = None; _buf = []; SR = 22050
CB = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_short), ctypes.c_int, ctypes.c_void_p)

def _cb(wav, n, ev):
    if wav and n > 0: _buf.append(np.ctypeslib.as_array(wav, shape=(n,)).copy())
    return 0
_cbc = CB(_cb)

def _init():
    global _lib, SR
    if _lib: return
    _lib = ctypes.CDLL(_e.get_library_path())
    _lib.espeak_Initialize.restype = ctypes.c_int
    SR = _lib.espeak_Initialize(1, 0, _e.get_data_path().encode(), 0)       # AUDIO_OUTPUT_RETRIEVAL
    _lib.espeak_SetSynthCallback(_cbc)

def sintetizar(texto, voz='es', tono=50, velocidad=165, volumen=100):
    """tono 0-99 (50 = normal), velocidad en palabras/min"""
    _init(); _buf.clear()
    _lib.espeak_SetVoiceByName(voz.encode())
    _lib.espeak_SetParameter(1, int(velocidad), 0)   # RATE
    _lib.espeak_SetParameter(2, int(volumen), 0)     # VOLUME
    _lib.espeak_SetParameter(3, int(tono), 0)        # PITCH
    b = texto.encode('utf-8')
    _lib.espeak_Synth(b, len(b) + 1, 0, 0, 0, 1, None, None)               # espeakCHARS_UTF8 = 1
    _lib.espeak_Synchronize()
    return (np.concatenate(_buf) if _buf else np.zeros(1, np.int16)), SR
