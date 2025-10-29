from django.shortcuts import render
from django.http import JsonResponse
from .crypto_algorithm import CryptoAlgorithm
# ARCHIVO: encryptor/views.py



def index(request):
    return render(request, 'encryptor/index.html')

def process_crypto(request):
    # Tu código aquí
    pass

def index(request):
    """Vista principal de la aplicación"""
    return render(request, 'encryptor/index.html')  # ← SIN 'templates'

def process_crypto(request):
    """Procesa la encriptación o desencriptación"""
    if request.method == 'POST':
        text = request.POST.get('text', '')
        key = request.POST.get('key', '')
        mode = request.POST.get('mode', 'encrypt')
        
        if not text or not key:
            return JsonResponse({
                'success': False,
                'error': 'Debes ingresar texto y clave'
            })
        
        if mode == 'encrypt':
            result = CryptoAlgorithm.encrypt(text, key)
        else:
            result = CryptoAlgorithm.decrypt(text, key)
        
        if result:
            return JsonResponse({
                'success': True,
                'result': result
            })
        else:
            return JsonResponse({
                'success': False,
                'error': 'Error en el procesamiento'
            })
    
    return JsonResponse({'success': False, 'error': 'Método no permitido'})