import gamefunctions
import random


'''Call the class Monster() stores monster information including movement and traits.'''
class Monster():
    '''This class stores monster traits, information and the movement function.
    
    Arguments:
    None

    Return:
    None

    '''
    hp = None
    damage = None
    name = None
    gold = None
    position = None
    color = None


    '''This function initializes a new instance in the class Monster(). '''
    def __init__(self):
        '''This function calls the new_random_monster function.
        
        Arguments:
        self

        Return:
        None

        '''
        self.new_random_monster()


    '''Call this function to move the monster.'''
    def move(self):
        '''This function is used to move the monster around the game screen.
        
        Arguments:
        self

        Return:
        None

        '''
        direction = random.choice(["left", "right", "up", "down"])
        new_pos = self.position
        if direction == "left":
            if new_pos[1] - 1 < 0:
                return
            new_pos[1] -= 1
        elif direction == "right":
            if new_pos[1] + 1 > 9:
                return
            new_pos[1] += 1
        elif direction == "up":
            if new_pos[0] - 1 < 0:
                return
            new_pos[0] -= 1
        else:
            if new_pos[0] + 1 > 9:
                return
            new_pos[0] += 1
        if new_pos == [6, 5]:
            return
        self.position = new_pos


    '''Call new_random_monster to generate a random monster.'''
    def new_random_monster(self):
        '''This function is used to generate a random monster from a set selection.
        
        Arguments:
        self

        Return:
        None
        
        '''
        self.hp = random.randint(10, 50)
        self.damage = random.randint(5, 10)
        self.name = random.choice(["Goblin", "Mummy", "Vampire"])
        self.gold = random.randint(5, 25)
        self.position = [random.randint(0,9), random.randint(0,9)]
        if self.name == "Goblin":
            self.color = (34, 139, 34, 1)
        elif self.name == "Mummy":
            self.color = (255, 255, 0, 1)
        elif self.name == "Vampire":
            self.color = (255, 0, 0, 1)


    '''Call serialize to convert current object states into a dictionary.'''    
    def serialize(self):
        '''This function converts current object states into a dictionary.
        
        Arguments:
        self

        Return:
        monster_dict
        
        '''
        monster_dict = {
            "hp": self.hp,
            "damage": self.damage,
            "name": self.name,
            "gold": self.gold,
            "position": self.position,
            "color": self.color
        }
        return monster_dict
    

    '''Call this fuction to redefine attributes based on the dictionary.'''
    def deserialize(self, monster_dict):
        '''This function is used to redefine attributes based on monster_dict.
        
        Arguments:
        self, monster_dict

        Return:
        self
        
        '''
        self.hp = monster_dict["hp"]
        self.damage = monster_dict["damage"]
        self.name = monster_dict["name"]
        self.gold = monster_dict["gold"]
        self.position = monster_dict["position"]
        self.color = monster_dict["color"]
        return self

