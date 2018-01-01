class Character():
    def __init__(self,damage,health,name,**kwargs):
        self.damage = damage
        self.health = health
        self.name = name
    def Attack(self,enemy):
        enemy.health -= self.damage
        if enemy.health <= 0:
        	print(enemy.name + " Wasted")
    def Take_damage(self,damage):
        if self.health <= damage:
        	print(self.name + " Wasted")
        else:		
        	self.health -= damage
class Hero(Character):
    def __init__(self,damage=10,health=30,max_health=50,name="Hero",**kwargs):
        self.max_health = max_health
        super().__init__(damage,health,name,**kwargs)
    def rest(self):
        self.health += self.damage
        if self.health > max_health:
        	self.health = max_health
class Monster(Character):
	def __init__(self,damage,health,name,**kwargs):
		super().__init__(damage,health,name,**kwargs)	        	
class Goblin(Monster):
    def __init__(self,damage=5,health=10,name="Goblin",**kwargs):
        super().__init__(damage,health,name,**kwargs)
class Orc(Monster):
    def __init__(self,damage=10,health=20,name="Orc",**kwargs):
        super().__init__(damage,health,name,**kwargs)