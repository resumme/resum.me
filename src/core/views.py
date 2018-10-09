from django.shortcuts import render

def privacy(request):
    return render(request, 'core/legal.html')

def terms_and_condition(request):
    return render(request, 'core/terms.html')
