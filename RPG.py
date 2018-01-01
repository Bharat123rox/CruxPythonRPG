class Character():
	'''Assuming name is public, health and damage are private variables'''
    def __init__(self,damage,health,name,**kwargs):
        self._damage = damage
        self._health = health
        self.name = name
    '''Getter and Setter Methods'''    
    def GetHealth()
    	return self._health
    def GetDamage()
    	return self._damage
    def SetHealth(health):
    	self._health = health
    def	SetDamage(damage):
    	self._damage = damage		
    def Attack(self,enemy):
        enemy.Take_damage(self.GetDamage())
    def Take_damage(self,damage):
        if self.GetHealth() <= damage:
        	print(self.name + " Wasted")
        else:		
        	self.GetHealth() -= damage
class Hero(Character):
	'''max_health is a public var for now '''
    def __init__(self,damage=10,health=30,max_health=50,name="Hero",**kwargs):
        self.max_health = max_health
        super().__init__(damage,health,name,**kwargs)
    def rest(self):
        self.GetHealth() += self.GetDamage()
        if self.GetHealth() > max_health:
        	self.GetHealth() = max_health
class Monster(Character):
	def __init__(self,damage,health,name,**kwargs):
		super().__init__(damage,health,name,**kwargs)	        	
class Goblin(Monster):
    def __init__(self,damage=5,health=10,name="Goblin",**kwargs):
        super().__init__(damage,health,name,**kwargs)
class Orc(Monster):
    def __init__(self,damage=10,health=20,name="Orc",**kwargs):
        super().__init__(damage,health,name,**kwargs)