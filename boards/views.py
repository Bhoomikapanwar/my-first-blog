from django.shortcuts import render
from django.http import HttpResponse
from .models import Board
from django.views import View
# Create your views here.
def home(request):
    boards = Board.objects.all()

    return render(request,'home.html',{'boards' : boards})

#use class based views
class Home (View):   
    response_template='home.html'
    
    def get(self, request, *args, **kwargs):
        boards = Board.objects.all()
        return render_to_response(self.response_template, boards, context_instance=RequestContext(request))
