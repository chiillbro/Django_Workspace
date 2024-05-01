from django.shortcuts import render
from django.template import loader

from .models import Member
# Create your views here.


from django.http import HttpResponse


def home(request):
  template = loader.get_template('myFirst.html')
  return HttpResponse(template.render())
  



def members(request):
   

    mymembers = Member.objects.all()
    # print(mymembers)
    template = loader.get_template('all_members.html')
    context = {
        'mymembers' : mymembers
    }
    return HttpResponse(template.render(context, request))


def details(request, slug):
    mymember = Member.objects.get(slug=slug)
    # print(mymember)
    template = loader.get_template('details.html')
    context = {
        'mymember' : mymember
    }
    return HttpResponse(template.render(context, request))

def main(request):
   template = loader.get_template('main.html')
   return HttpResponse(template.render())

def testing(request):
   template = loader.get_template('template.html')
   context = {
      'myList':{ "Stack": ['MERN', 'Python', 'Django-in-process'], 'firstname':"Siva", "lastname":"Asam", "Role":"Software Developer"}
   }

   return HttpResponse(template.render(context, request))