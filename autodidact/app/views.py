from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import Tag
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


@csrf_exempt
def addTag(request):
    if request.POST:
        obj = Tag()
        tag_name = request.POST['name']
        print(tag_name)
        obj.name = tag_name
        obj.save()
        return HttpResponse('Done')
    else:
        return HttpResponse('Get request')
