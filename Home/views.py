from django.shortcuts import render

def search_view(request):
    return render(request, 'index.html') 
