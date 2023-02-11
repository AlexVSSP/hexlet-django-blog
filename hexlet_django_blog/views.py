from django.shortcuts import render
from django.views.generic.base import TemplateView


# def index(request):
#     return render(request, 'index.html', context={
#         'who': 'World',
#     })

# 7 Представления (Views) вместо предыдущ. функции
class HomePageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['who'] = 'World'
        return context

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context=self.get_context_data())


def about(request):
    return render(request, 'about.html')
