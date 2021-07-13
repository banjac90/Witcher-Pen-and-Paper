import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from usersAPI.models import User
from character.models import Character
from character.serializers import listCharacterSerializer


class ViewTest(APITestCase):
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

    maxDiff = None    
    
    def test_list(self):                 
        response = self.client.get(reverse('characters:char-list'))
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        

    def test_details(self):        
        response = self.client.get(reverse('characters:char-details', kwargs={'slug': 'neca-yennefer'}))
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response.data['player_name'], 'Neca')
        

    def test_update(self):       
        data = {
            'brawling': 4
        }
        response = self.client.put(reverse('characters:char-update', kwargs={'slug': 'neca-yennefer'}), data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(json.loads(response.content),
           {
               'player_name': 'Neca', 'char_name': 'Yennefer', 'race': 'Human',
               'profession': 'Mage', 'intelligence': 10, 'reflexes': 8,
               'dexterity': 6,'body': 7, 'speed': 5,'empathy': 6,
               'craft': 8, 'will': 10, 'luck': 7, 'run': 15, 'leap': '3.00',
               'hp': 40, 'stamina': 40, 'stun': 8, 'encumbrance': 70,
               'recovery': 8, 'punch': '1d6+2', 'kick': '1d6+6', 'vigor': 25,
               'awareness': 6, 'business': None, 'deduction': None,'education': 9,
               'common_speech': None, 'elder_speech': None, 'dwarven': None,
               'monster_lore': None, 'social_etiquette': 8, 'streetwise': None,
               'tactics': None, 'teaching': None, 'wilderness_survival': None,
               'archery': None, 'athletics': None, 'crossbow': None,
               'sleight_of_hand': None, 'stealth': 8, 'brawling': 4, 'doge_escp': 8,
               'melee': None, 'riding': 7, 'sailing': None, 'small_blades': None,
               'staff_spear': 4, 'swordsmanship': None, 'physique': None, 'endurance': 5,
               'charisma': 5, 'deceit': None, 'fine_arts': None, 'gambling': None, 
               'groom_style': 8, 'perception': 10, 'leadership': None, 'presuasion': 7,
               'preformance': None, 'seduction': 10, 'alchemy': None, 'crafting': None,
               'disguise': None, 'first_aid': None, 'forgery': None, 'lock': None, 'trap': None,
               'courage': 10, 'hex_weaving': 10, 'intimidation': None, 'spell_casting': 10,
               'resist_magic': 10, 'ritual_crafting': 10, 'resist_coercion': 10, 
            }
        )
