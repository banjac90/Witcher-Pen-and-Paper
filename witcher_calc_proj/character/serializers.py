from rest_framework import serializers
from .models import Character, choices_of_professions, choices_of_races

class CreateCharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = [
            'player_name', 'char_name', 'race', 'profession',
            'intelligence', 'reflexes', 'dexterity', 'body', 'speed', 'empathy', 'craft', 'will', 'luck',
            'vigor', 'awareness', 'business', 'deduction', 'education', 'common_speech', 'elder_speech',
            'dwarven', 'monster_lore', 'social_etiquette', 'streetwise', 'tactics', 'teaching', 'wilderness_survival',
            'archery', 'athletics', 'crossbow', 'sleight_of_hand', 'stealth', 'brawling', 'doge_escp', 'melee',
            'riding', 'sailing', 'small_blades', 'staff_spear', 'swordsmanship', 'physique', 'endurance', 'charisma',
            'deceit', 'fine_arts', 'gambling', 'groom_style', 'perception', 'leadership', 'presuasion', 'preformance',
            'seduction', 'alchemy', 'crafting', 'disguise', 'first_aid', 'forgery', 'lock', 'trap', 'courage',
            'hex_weaving', 'intimidation', 'spell_casting', 'resist_magic', 'resist_coercion', 'ritual_crafting'     
        ]

class UpdateDetailsCharacterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Character
        fields = [            
            'player_name', 'char_name', 'race', 'profession', 'run', 'leap', 'hp', 'stamina', 'stun',
            'encumbrance', 'recovery', 'punch', 'kick', 'intelligence', 'reflexes', 'dexterity', 'body', 
            'speed', 'empathy', 'craft', 'will', 'luck', 'vigor', 'awareness', 'business', 'deduction', 
            'education', 'common_speech', 'elder_speech', 'dwarven', 'monster_lore', 'social_etiquette', 
            'streetwise', 'tactics', 'teaching', 'wilderness_survival', 'archery', 'athletics', 'crossbow', 
            'sleight_of_hand', 'stealth', 'brawling', 'doge_escp', 'melee', 'riding', 'sailing', 'small_blades',
            'staff_spear', 'swordsmanship', 'physique', 'endurance', 'charisma', 'deceit', 'fine_arts', 'gambling',
            'groom_style', 'perception', 'leadership', 'presuasion', 'preformance', 'seduction', 'alchemy', 'crafting', 
            'disguise', 'first_aid', 'forgery', 'lock', 'trap', 'courage', 'hex_weaving', 'intimidation', 
            'spell_casting', 'resist_magic', 'resist_coercion', 'ritual_crafting'     
        ]
        

class listCharacterSerializer(serializers.ModelSerializer):   
    url = serializers.HyperlinkedIdentityField(
        view_name = 'characters:char-details',
        lookup_field = 'slug'
    )
    class Meta:
        model = Character
        fields = ['url', 'player_name', 'char_name', 'race', 'profession']
        