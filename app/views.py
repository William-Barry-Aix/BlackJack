from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView





class HomeView(TemplateView):
    template_name = 'home.html'

    def getUser(self, request):
        username = None
        if request.user.is_authenticated():
            username = request.user.username