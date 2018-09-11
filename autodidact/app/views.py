from django.http import HttpResponse
from django.shortcuts import render

from app.forms import SignUpForm


def main(request):
    if request.POST:
        form = SignUpForm(request.POST)
        print(form)
        if form.is_valid():
            return HttpResponse('Done')
    else:
        form = SignUpForm()

    context = {
        'form': form,
    }

    print(form)

    return render(request, template_name='index.html', context=context)
