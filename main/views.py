from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306244974',
        'name': 'Calvin Joy Tarigan',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)