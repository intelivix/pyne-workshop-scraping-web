from django.views.generic.base import TemplateView


class HomePageView(TemplateView):

    template_name = "index.html"


index = HomePageView.as_view()
