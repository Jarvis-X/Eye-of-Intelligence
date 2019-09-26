import main


# Macro for minimum number: numbers smaller than this is 0
epsil = 0.01

# Macros for races
HUMAN = 1
SOLAR = 2
MRIFT = 3
MECHA = 4
SWARM = 5

# Macro for enemy types
CHARA = 10    # a main character as the enemy
POLIC = 11    # one police
POLIC_2 = 12  # two police
POLIC_3 = 13  # three police


# Macro for no modification:
NO_MOD = 0

# Macros for _consist_modifier
CONSIST_MODIFIER = 100
AUTO_CLEAR = 101


# Macros for _mov_modifier
MOV_MODIFIER = 200


# Macros for items
ITEMS = 300
MONUMENT_STONE = 301


# Macros for buffs
BUFFS = 600
LEARNING = 601


# class def for a character
class Character:
    """
    the basic class for a character
    it contains private members:
        _race: stores the race of the character
        _name: the name of this character
        _is_player: whether this is a character controlled by the player
        
        properties that can be described with pure numbers:
        _base_hp
        _hp_modifier
        _phy_attack 
        _phy_attack_modifier
        _phy_defend
        _phy_defend_modifier
        _mag_attack
        _mag_attack_modifier
        _mag_defend
        _mag_defend_modifier
        _act_point
        _act_point_modifier
        _item_slot: number of items a character can still equip
        _inventory_slot: number of items a character can still carry
        
        properties that needs a look-up table to numerize:
        _mov_modifier: a set of modifiers that affect the character's movement property
        _consist_modifier: a set of modifiers that affect the character's consist attack/defend
        _inventory: items the character carries but does not equip
        _item_equipped: a set holding the items that have an impact on character data
        _buff_possessed: a set holding the buffs that have an impact on character data
        _special: a set of special traits a character holds or special environmental hazards the character is affected by
        
    it contains public methods:
        
    TODO: add implementations for other races
    
    """
    def __init__(self, race, name = "John_Wick", is_player = False):
        self._race = race
        self._name = name
        self._is_player = is_player
        
        # initialize all races with no modifier
        self._hp_modifier = NO_MOD
        self._phy_attack_modifier = NO_MOD
        self._phy_defend_modifier = NO_MOD
        self._mag_attack_modifier = NO_MOD
        self._mag_defend_modifier = NO_MOD
        self._act_point_modifier = NO_MOD
        self._mov_modifier = NO_MOD
        
        # human character
        if self._race == HUMAN:
            self._full_hp = 10
            self._phy_attack = 10
            self._phy_defend = 15
            self._mag_attack = 10
            self._mag_defend = 10
            self._act_point = 12
            self._item_slot = 5
            self._inventory_slot = 10
            
            self._consist_modifier = set()
            self._inventory = set()
            self._item_equipped = set()
            self._buff_possessed = set()
            self._special = set()
            
            self._consist_modifier.add(AUTO_CLEAR)  # human's racial trait
            self._item_equipped.add(LEARNING)       # human's racial trait
            
            self._phy_attack_modifier += self._phy_attack*0.1
            self._phy_defend_modifier += self._phy_defend*0.1
            self._mag_attack_modifier += self._mag_attack*0.1
            self._mag_defend_modifier += self._mag_defend*0.1
            
            
if __name__ == "__main__":
    humanA = Character(HUMAN)
    
