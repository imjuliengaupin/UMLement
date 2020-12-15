from django.shortcuts import render


def example(request):
    template_name = "umlement/index.html"
    return render(request, template_name)
