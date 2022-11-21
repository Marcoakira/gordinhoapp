#from django.http import HttpResponse
# crinado paginação com python
from django.core.paginator import Paginator
from django.shortcuts import redirect, render

from app.form import EleitorForm
from app.models import Eleitor

# Create your views here.

'''
def home(request):
    return HttpResponse("Helo markinho 2")
'''


def home(request):
    data = {}

    search = request.GET.get('search')
    if search:
        data['db'] = Eleitor.objects.filter(cpf__icontains=search)
    else:
        data['db'] = Eleitor.objects.all()
    return render(request, 'index.html', data)


"""
    abaixo o codigo para ser usado em paginação
    
def home(request):
    data = {}
    all = Eleitor.objects.all()

    paginator = Paginator(all, 10)
    pages = request.GET.get('page')
    data['db'] = paginator.get_page(pages)
    return render(request, 'index.html', data)
"""


def form(request):
    data = {}
    data['form'] = EleitorForm()
    return render(request, 'form.html', data)


def create(request):
    form = EleitorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')


def view(request, pk):
    data = {}
    data['db'] = Eleitor.objects.get(pk=pk)

    return render(request, 'view.html', data)


def edit(request, pk):
    data = {}
    data['db'] = Eleitor.objects.get(pk=pk)
    data['form'] = EleitorForm(instance=data['db'])
    return render(request, 'form.html', data)


def update(request, pk):

    data = {}
    data['db'] = Eleitor.objects.get(pk=pk)
    form = EleitorForm(request.POST or None, instance=data['db'])

    if form.is_valid():
        form.save()
        return redirect('home')


def delete(request, pk):
    db = Eleitor.objects.get(pk=pk)
    db.delete()

    return redirect('home')
