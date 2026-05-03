from django.shortcuts import render

def textAnalyzer(request):
    return render(request, 'textAnalyzer.html')

def finalOutput(request):
    text   = request.GET.get('data', '')
    pun    = request.GET.get('removePunc', 'off')
    spa    = request.GET.get('removeSpa', 'off')
    exLine = request.GET.get('removeExtraLine', 'off')

    punctuation = set('!()-[]{};:\'"\\,<>./?@#$%^&*_~')

    if pun == 'on':
        text = ''.join(ch for ch in text if ch not in punctuation)

    if spa == 'on':
        text = ''.join(ch for ch in text if ch != ' ')

    if exLine == 'on':
        text = ''.join(ch for ch in text if ch not in ('\r', '\n'))

    return render(request, 'finalOutput.html', {'data': text, 'counter': len(text)})