class Character():
    def __init__(self,Damage,Health,name,**kwargs):
        self.Damage = Damage
        self.Health = Health
        self.name = name
    def Attack(self,enemy):
        enemy.Health -= self.Damage
        if enemy.Health <= 0:
        	print(enemy.name + "Wasted")
    def Take_damage(self,Damage):
        self.Health -= Damage
        if self.Health <= 0:
        	print(self.name + "Wasted")	
class Hero(Character):
    def __init__(self,Damage=10,Health=30,MAX_HEALTH=50,name="Hero",**kwargs):
        self.MAX_HEALTH = MAX_HEALTH
        super().__init__(Damage,Health,name,**kwargs)
    def rest(self):
        self.Health += self.Damage
        if self.Health > MAX_HEALTH:
        	self.Health = MAX_HEALTH
class Goblin(Character):
    def __init__(self,Damage=5,Health=10,name="Goblin",**kwargs):
        super().__init__(Damage,Health,name,**kwargs)
class Orc(Character):
    def __init__(self,Damage=10,Health=20,name="Orc",**kwargs):
        super().__init__(Damage,Health,name,**kwargs)