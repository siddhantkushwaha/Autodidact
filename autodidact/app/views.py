from django.http import HttpResponse
from django.shortcuts import render


def main(request):
    context = {

    }
    return render(request, template_name='index.html', context=context)
