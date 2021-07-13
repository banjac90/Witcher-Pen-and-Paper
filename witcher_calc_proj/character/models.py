from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.urls import reverse
from witcher_app.utils import unique_slug_generator
from django.conf import settings
from usersAPI.models import User

choices_of_professions = [
        ('bard', 'Bard'),
        ('craftsman', 'Craftsman'),
        ('criminal', 'Criminal'),
        ('doctor', 'Doctor'),
        ('mage', 'Mage'),
        ('MAA', 'Man At Arms'),
        ('merchant', 'Merchant'),
        ('priest', 'Priest'),
        ('witcher', 'Witcher')
]
choices_of_races = [
        ('human', 'Human'),
        ('dwarf', 'Dwarf'),
        ('elf', 'Elf'),
        ('witcher', 'Witcher'),      
]


class Character(models.Model):
    player_name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    char_name = models.CharField(max_length=30, null=True)
    race = models.CharField(max_length=30, null=True, choices=choices_of_races)
    profession = models.CharField(max_length=30, null=True, choices=choices_of_professions)
    
    #statusi
    intelligence = models.IntegerField(default=1)
    reflexes = models.IntegerField(default=1)
    dexterity = models.IntegerField(default=1)
    body = models.IntegerField(default=1)
    speed = models.IntegerField(default=1)
    empathy = models.IntegerField(default=1)
    craft = models.IntegerField(default=1)
    will = models.IntegerField(default=1)
    luck = models.IntegerField(default=1)    
    
    #drived stats
    run = models.IntegerField(null=True, default=1)
    leap = models.DecimalField(null=True, max_digits=10, decimal_places=2)
    hp = models.IntegerField(null=True, default=1)
    stamina = models.IntegerField(null=True, default=1)
    stun = models.IntegerField(null=True, default=1)
    encumbrance = models.IntegerField(null=True, default=1)
    recovery = models.IntegerField(null=True, default=1)
    punch = models.CharField(blank=True, max_length=10)
    kick = models.CharField(blank=True, max_length=10)    
    vigor = models.IntegerField(null=True, default=0)
    #inteligence
    awareness = models.IntegerField(null=True)
    business = models.IntegerField(null=True)
    deduction = models.IntegerField(null=True)
    education = models.IntegerField(null=True)
    common_speech = models.IntegerField(null=True)
    elder_speech = models.IntegerField(null=True)
    dwarven = models.IntegerField(null=True)
    monster_lore = models.IntegerField(null=True)
    social_etiquette = models.IntegerField(null=True)
    streetwise = models.IntegerField(null=True)
    tactics = models.IntegerField(null=True)
    teaching = models.IntegerField(null=True)
    wilderness_survival = models.IntegerField(null=True)
    #dexterity
    archery = models.IntegerField(null=True)
    athletics = models.IntegerField(null=True)
    crossbow = models.IntegerField(null=True)
    sleight_of_hand = models.IntegerField(null=True)
    stealth = models.IntegerField(null=True)
    #reflex
    brawling = models.IntegerField(null=True)
    doge_escp = models.IntegerField(null=True)
    melee = models.IntegerField(null=True)
    riding = models.IntegerField(null=True)
    sailing = models.IntegerField(null=True)
    small_blades = models.IntegerField(null=True)
    staff_spear = models.IntegerField(null=True)
    swordsmanship = models.IntegerField(null=True)
    #body
    physique = models.IntegerField(null=True)
    endurance = models.IntegerField(null=True)
    #empathy
    charisma = models.IntegerField(null=True)
    deceit = models.IntegerField(null=True)
    fine_arts = models.IntegerField(null=True)
    gambling = models.IntegerField(null=True)
    groom_style = models.IntegerField(null=True)
    perception = models.IntegerField(null=True)
    leadership = models.IntegerField(null=True)
    presuasion = models.IntegerField(null=True)
    preformance = models.IntegerField(null=True)
    seduction = models.IntegerField(null=True)
    #craft
    alchemy = models.IntegerField(null=True)
    crafting = models.IntegerField(null=True)
    disguise = models.IntegerField(null=True)
    first_aid = models.IntegerField(null=True)
    forgery = models.IntegerField(null=True)
    lock = models.IntegerField(null=True)
    trap = models.IntegerField(null=True)
    #will
    courage = models.IntegerField(null=True)
    hex_weaving = models.IntegerField(null=True)
    intimidation = models.IntegerField(null=True)
    spell_casting = models.IntegerField(null=True)
    resist_magic = models.IntegerField(null=True)
    resist_coercion = models.IntegerField(null=True)
    ritual_crafting = models.IntegerField(null=True)

    #slug
    slug = models.SlugField(unique=True, blank=True, null=True, max_length=250)


    def get_absolute_url(self):
            return reverse('characters:char-details', kwargs={'slug':self.slug})
    
    def __str__(self):
        return self.char_name



@receiver(pre_save, sender=Character)
def save_char(sender, instance, **kwargs):
        run = instance.speed*3
        leap = instance.run/5
        encumbrance = instance.body*10
        bodywill = int((instance.body + instance.will)/2)        
        hp = bodywill*5
        sta = bodywill*5
        rec = bodywill
        stun = bodywill
        checkBody = instance.body
        if checkBody == 1 or checkBody == 2:
                punch = '1d6-4'
                kick = '1d6'
        elif checkBody == 3 or checkBody == 4:
                punch = '1d6-2'
                kick = '1d6+2'
        elif checkBody == 5 or checkBody == 6:
                punch = '1d6'
                kick = '1d6+4'
        elif checkBody == 7 or checkBody == 8:
                punch = '1d6+2'
                kick = '1d6+6'
        elif checkBody == 9 or checkBody == 10:
                punch = '1d6+4'
                kick = '1d6+8'
        elif checkBody == 11 or checkBody == 12:
                punch = '1d6+6'
                kick = '1d6+10'
        elif checkBody == 13:
                punch = '1d6+8'
                kick = '1d6+12'
        else:
                punch = '0'
                kick = '0'        
        
        if not instance.slug:                
                slug_text = f'{instance.player_name}-{instance.char_name}'
                instance.slug = unique_slug_generator(instance, slug_text, instance.slug)
      
        instance.punch = punch
        instance.kick = kick
        instance.hp = hp
        instance.stamina = sta
        instance.recovery = rec
        instance.stun = stun
        instance.run = run
        instance.leap = leap
        instance.encumbrance = encumbrance




