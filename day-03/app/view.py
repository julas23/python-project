from django.shortcuts import render

def index(request):
    context = {
        'phrase': 'Hello, World!'
    }
    return render(request, 'index.html', context)

def custom_message(request):
    context = {
        'message': 'This is a custom page!'
    }
    return render(request, 'custom_message.html', context)