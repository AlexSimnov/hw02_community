from django.views.generic.base import TemplateView


class AboutAuthorView(TemplateView):
    template_name = 'posts/author.html'


class AboutTechView(TemplateView):
    template_name = 'posts/tech.html'
