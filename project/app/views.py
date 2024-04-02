from django.shortcuts import render
from django.http import HttpResponse
from app.forms import *
from django.views.generic import View
# Create your views here.

def  insertschoolbyfbv(request):
   ESFO = SchoolForm()
   d = {'ESFO':ESFO}
   if request.method == 'POST':
      SFDO = SchoolForm(request.POST)
      if SFDO.is_valid():
         SFDO.save()
         return HttpResponse('School Created Successfully')
      return HttpResponse('Invalid Data')
   return render(request, 'insertschoolbyfbv.html', d)


class InsertSchoolByCBV(View):
   def get(self,request):
      ESFO = SchoolForm()
      d = {'ESFO':ESFO}
      return render(request, 'InsertSchoolByCBV.html', d)
   
   def post(self,request):
      SFDO = SchoolForm(request.POST)
      if SFDO.is_valid():
         SFDO.save()
         return HttpResponse('School Created Successfully using Class based views')
      return HttpResponse('Invalid Data')