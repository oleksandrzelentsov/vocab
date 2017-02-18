from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


words = """
Anyone who reads Old and Middle English
literary texts will be familiar with the
mid-brown volumes of the EETS, with the symbol
of Alfred's jewel embossed on the front
cover. Most of the works attributed to King
Alfred or to Aelfric, along with some of
those by bishop Wulfstan and much anonymous
prose and verse from the pre-Conquest period,
are to be found within the Society's three
series; all of the surviving medieval
drama, most of the Middle English romances,
much religious and secular prose and verse
including the English works of John Gower,
Thomas Hoccleve and most of Caxton's prints
all find their place in the publications.
Without EETS editions, study of medieval
English texts would hardly be possible.""".split()
words = set(map(lambda x: x.replace('.', '').replace(',', ''), words))


def api(request):
    word = request.GET.get('word')
    if word in words:
        return JsonResponse({'result': 'success',
                             'func': 'display_success',
                             'what': word,
                            })
    else:
        return JsonResponse({'result': 'success',
                             'func': 'check_failed',
                             'what': word,
                            })
