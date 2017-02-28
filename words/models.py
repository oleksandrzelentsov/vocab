from django.db import models
from vocab.settings import DEFAULT_LANGUAGE, WORD_FILES
from django.core.cache import cache

# Create your models here.

def update_word_cache():
    words = []
    for f in WORD_FILES[DEFAULT_LANGUAGE]:
        with open(f, 'r') as fp:
            words += list(map(lambda x: x.strip(), fp.readlines()))
    cache.set('words', words, None)



