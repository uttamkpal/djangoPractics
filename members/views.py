# from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Members

def index(request):
    allmembers = Members.objects.all().values()
    template = loader.get_template('members.html')
    context = {
        'allmembers' : allmembers,
    }
    # return HttpResponse(allmembers)
    return HttpResponse(template.render(context, request))


def add(request):
    template = loader.get_template('add.html')
    return HttpResponse(template.render({}, request))

def addrecord(request):
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    member = Members(firstname = firstname, lastname = lastname)
    member.save()
    return HttpResponseRedirect(reverse('index'))

def delete(request, id):
    member = Members.objects.get(id=id)
    member.delete()
    return HttpResponseRedirect(reverse('index'))

def update(request, id):
    member = Members.objects.get(id=id)
    context = {
        'member' : member,
    }
    template = loader.get_template('update.html')
    return HttpResponse(template.render(context, request))

    
def updaterecord(request, id):
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    member = Members.objects.get(id=id)
    member.firstname = firstname
    member.lastname = lastname
    member.save()
    return HttpResponseRedirect(reverse('index'))
