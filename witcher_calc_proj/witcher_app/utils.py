from django.utils.text import slugify
import random
import string

def unique_slug_generator(model_istance, slug_text, slug_field):


    slug = slugify(slug_text)
    model_class = model_istance.__class__

    while model_class._default_manager.filter(slug=slug).exists():
        object_pk = model_class._default_manager.latest('pk')
        object_pk = object_pk.pk + 1 

        slug = f'{slug}-{object_pk}'
        
    return slug

