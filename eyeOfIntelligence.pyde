# Macro for minimum number: numbers smaller than this is 0
epsil = 0.001

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
DECADE = 102
STICKY = 103

# Macros for _mov_modifier
MOV_MODIFIER = 200
INERTIA = 201

# Macros for items
ITEMS = 300
MONUMENT_STONE = 301

# Macros for buffs
BUFFS = 600
LEARNING = 601
TOLERATE = 602

# Macros for special modifier
SPECIAL_MODIFIER = 1000
CHARGE = 1001


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
        
    TODO: MRIFT, MECHA, SWARM
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
        
        # common values
        self._full_hp = 10
        self._phy_attack = 10
        self._phy_defend = 10
        self._mag_attack = 10
        self._mag_defend = 10
        self._act_point = 10
        self._item_slot = 5
        self._inventory_slot = 10
        
        # traits, buffs, items, etc.
        self._consist_modifier = set()
        self._inventory = set()
        self._item_equipped = set()
        self._buff_possessed = set()
        self._special = set()
        
        # human character
        if self._race == HUMAN:
            self._phy_defend += 5
            self._act_point += 2
            
            self._consist_modifier.add(AUTO_CLEAR)
            self._item_equipped.add(MONUMENT_STONE)
            self._buff_possessed.add(LEARNING)
            
            self._phy_attack_modifier += self._phy_attack*0.1
            self._phy_defend_modifier += self._phy_defend*0.1
            self._mag_attack_modifier += self._mag_attack*0.1
            self._mag_defend_modifier += self._mag_defend*0.1
        # solar sun character
        elif self._race == SOLAR:
            self._phy_attack += 5
            self._mag_attack += 5
            self._full_hp -= 5
            self._mag_defend -= 5
            self._act_point -= 5
            self._mov_modifier = INERTIA
            
            self._consist_modifier.add(DECADE)
            self._consist_modifier.add(STICKY)
            self._buff_possessed.add(TOLERATE)
            self._special.add(CHARGE)
    
    def getName(self):
        return self._name
    
    def getRace(self):
        return self._race

    
# placeholder for the battle function
def battle(A, B):
    textSize(32);
    text("{} beats {} and wins!".format(A.getName(), B.getName()), 10, 30); 



# main function
size(1280, 720)
humanA = Character(HUMAN, "Feiyangyang", True)
solarA = Character(SOLAR, "Meiyangyang")
battle(humanA, solarA)
print("All Good")
    
