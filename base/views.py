
from telnetlib import GA
from django.shortcuts import render,get_object_or_404
from django.http import JsonResponse
from .models import Games

def homeView(request):
    games=Games.objects.all()
    context={'games':games}
    return render(request, 'main/main.html', context)


def search_results(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        res=None
        game= request.POST.get('game')
        print(game)
        qs=Games.objects.filter(title__icontains=game)
        print(qs)
        if len(qs) > 0 and len(game)>0:
            data=[]
            for pos in qs:
                item={
                    'pk':pos.pk,
                    'title':pos.title,
                    'summary': pos.summary
                }
                data.append(item)
            res=data
        else:
            res= 'No games found'

        return JsonResponse({'data':res})
    return JsonResponse({})

def game_detail_view(request, pk):
    obj=get_object_or_404(Games, pk=pk)
    return render(request, 'main/details.html', {'obj':obj})