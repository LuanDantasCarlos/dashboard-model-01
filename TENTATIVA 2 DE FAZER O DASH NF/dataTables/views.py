from django.shortcuts import render
from django.http import HttpResponse
from .models import DadosNF

def dataTables(request):
         if request.method == "GET":
           dados_list = DadosNF.objects.all()
           return render(request, 'dataTables.html', {'dados': dados_list})
         elif request.method == "POST":
             classificacao = request.POST.get('classificacao')
             return HttpResponse('modificação realizada')



