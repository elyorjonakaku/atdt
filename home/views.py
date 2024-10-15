from django.shortcuts import render
from django.views import View

from user.models import CustomUser

# Create your views here.
class HomePageView(View):
    template_name = 'home.html'

    def get(self, request):
        users = CustomUser.objects.all()

        return render(request, self.template_name, {'users': users})