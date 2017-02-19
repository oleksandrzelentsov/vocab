from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from vocab.settings import DEFAULT_LANGUAGE, WORD_FILES
from django.core.cache import cache
from .models import update_word_cache


# words = {'a', 'o', 'i', 'e', 'u'}


def api(request):
    try:
        word = request.GET.get('word')
        guid = request.GET.get('guid')
        score = int(request.GET.get('score'))
        func = request.GET.get('func')
        # if not cache.get('words'):
        update_word_cache()
        words = cache.get('words')
        if not guid:
            return JsonResponse({'result': 'no GUID given'})

        info = cache.get(guid, {'words': [],
                                'score': score})

        if (word not in info['words']) and word in words:
            info['score'] += 1
            info['words'].append(word)
            cache.set(guid, info, 60 * 60)
            return JsonResponse({'result': 'success',
                                 'func': 'print' if func == 'debug' else 'display_success',
                                 'what': word + ' ' + guid + ' ' + ', '.join(cache.get(guid)['words']),
                                 'score': info['score'],
                                 'words': cache.get(guid)['words'],
                                })

        cache.set(guid, info, 60 * 60)
        return JsonResponse({'result': 'success',
                             'func': 'check_failed',
                             'what': word,
                            })
    except Exception as e:
        return JsonResponse({'result': str(e)})

