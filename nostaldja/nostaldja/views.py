from django.shortcuts import render, redirect

# Create your views here.
from .models import Decade, Fad
from .forms import DecadeForm


def decades_list(request):
    decades = Decade.objects.all()
    return render(request, 'nostaldja/decades_list.html', {'decades': decades})


def fads_list(request):
    fads = Fad.objects.all()
    return render(request, 'nostaldja/fads_list.html', {'fads': fads})


def decade_detail(request, pk):
    decade = Decade.objects.get(id=pk)
    return render(request, 'nostaldja/decade_detail.html', {'decade': decade})


def fad_detail(request, pk):
    fad = Fad.objects.get(id=pk)
    return render(request, 'nostaldja/fad_detail.html', {'fad': fad})


def decade_create(request):
    if request.method == 'POST':
        form = DecadeForm(request.POST)
        if form.is_valid():
            decade = form.save()
            return redirect('decade_detail', pk=decade.pk)
    else:
        form = DecadeForm()
    return render(request, 'nostaldja/decade_form.html', {'form': form})


def decade_edit(request, pk):
    decade = Decade.objects.get(pk=pk)
    if request.method == "POST":
        form = DecadeForm(request.POST, instance=decade)
        if form.is_valid():
            decade = form.save()
            return redirect('decade_detail', pk=decade.pk)
    else:
        form = DecadeForm(instance=decade)
    return render(request, 'nostaldja/decade_form.html', {'form': form})


def decade_delete(request, pk):
    Decade.objects.get(id=pk).delete()
    return redirect('decades_list')


def fad_delete(request, pk):
    Fad.objects.get(id=pk).delete()
    return redirect('fads_list')
