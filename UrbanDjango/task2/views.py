from django.shortcuts import render
from django.views.generic import TemplateView


def index(request):
    return render(request, 'index.html')
# Create your views here.
class class_template(TemplateView):
    template_name = 'second_task/class_template.html'


class func_temlate(TemplateView):
    template_name = 'second_task/func_template.html'
