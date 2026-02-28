from .models import Category, Adv
import random

def categories_processor(request):
    categories = Category.objects.all()
    return {
        'categories': categories,
    }

def advs_processor(request):
    ads_list = list(Adv.objects.all())
    advs = random.sample(ads_list, min(len(ads_list), 4))
    return {
        'advs': advs,
    }