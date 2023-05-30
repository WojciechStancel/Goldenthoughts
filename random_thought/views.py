from django.shortcuts import render, redirect, get_object_or_404
from random_thought.models import GoldenThougthData
from .forms import GoldenForm
import random

# Create your views here.


def thought(request):
    randomly_thought = GoldenThougthData.objects.all()
    return render(
        request,
        'random_thought/thoughts.html',
        context={
            'thought': random.choice(randomly_thought),
        }
    )


def create_thought(request):
    form = GoldenForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {'form': form}
    return render(request, 'random_thought/thought_list.html', context)


def list_view(request):

    thoughts = GoldenThougthData.objects.all()

    return render(request, 'random_thought/thought_list_view.html', context={'thoughts': thoughts})


def thought_detail(request, pk):

    thought = GoldenThougthData.objects.get(id=pk)

    return render(request, 'random_thought/thought_detail_view.html', context={'thought': thought})








    # if request.method == 'POST':
    #     updated_thought =request.POST.get('thought')
    #     if updated_thought:
    #         thought = updated_thought
    #         thought.save()
    #
    #     return redirect('random_thought:list_view')



