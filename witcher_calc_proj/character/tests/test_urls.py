from django.test import TestCase
from character.models import Character
from django.urls import resolve, reverse
    
            
class UrlTest(TestCase):   
    def test_list_url(self):    
       path = reverse('characters:char-list')
       assert resolve(path).view_name == 'characters:char-list'
    
    def test_details_url(self):    
       path = reverse('characters:char-details', kwargs={'slug': 'neca-yennefer'})
       assert resolve(path).view_name == 'characters:char-details'

    def test_update_url(self):    
       path = reverse('characters:char-update', kwargs={'slug': 'neca-yennefer'})
       assert resolve(path).view_name == 'characters:char-update'
    
    def test_update_url(self):    
       path = reverse('characters:char-create')
       assert resolve(path).view_name == 'characters:char-create'