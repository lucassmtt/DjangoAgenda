from django.shortcuts import render


def index_view(request):
    return render(
        request=request,
        template_name='contact/index.html',
    )