from django.core.cache import cache
from django.http import JsonResponse
from .models import update_word_cache


def check(request):
    try:
        word = request.GET.get('word')
        guid = request.GET.get('guid')
        if guid is None:
            return JsonResponse({'result': 'no guid'})
        func = request.GET.get('func')
        # if func is None:
        #     return JsonResponse({'result': 'no func'})
        if not cache.get('words'):
            update_word_cache()
        words = cache.get('words')

        info = cache.get(guid, {'words': [],
                                'score': 0})

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
