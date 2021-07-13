from django.test import TestCase
from character.models import Character
from django.urls import resolve, reverse
from usersAPI.models import User
from rest_framework.test import APIClient, APIRequestFactory


class ModelTest(TestCase):
    def setUp(self):
        player = User(username='Neca', email='tester@mail.com', first_name='Nenad', last_name='Bartole', password='test123!')
        player.save()
        client = APIClient(enforce_csrf_checks=True)
        client.login(username='Neca', password='test123!')
        self.char = Character()
        self.char.player_name = player
        self.char.char_name = 'Yennefer'
        self.char.intelligence = 10
        self.char.reflexes = 8
        self.char.dexterity = 6
        self.char.body = 7
        self.char.speed = 5
        self.char.empathy = 6
        self.char.craft = 8
        self.char.will = 10
        self.char.luck = 7
        self.char.vigor = 25
        self.char.perception = 10
        self.char.spell_casting = 10
        self.char.hex_weaving = 10
        self.char.ritual_crafting = 10
        self.char.presuasion = 7
        self.char.charisma = 5
        self.char.riding = 7
        self.char.courage = 10
        self.char.social_etiquette = 8
        self.char.seduction = 10
        self.char.groom_style = 8
        self.char.staff_spear = 4
        self.char.remanasist_magic = 10
        self.char.resist_coercion = 10
        self.char.education = 9
        self.char.awareness = 6
        self.char.endurance = 5
        self.char.doge_escp = 8
        self.char.stealth = 8
        self.char.save()
    
    def test_slug_method(self):
        self.assertEqual(self.char.slug, 'neca-yennefer')
    
    def test_get_absolute_url(self):       
        self.assertEqual(
            self.char.get_absolute_url(),
            "/Characters/details/%s/" % (self.char.slug)
        )
