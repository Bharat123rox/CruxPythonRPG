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
    xp = 0
    level = 1
    xp_increments = [i for i in range(0,210,10)]
    xp_level = [sum(xp_increments[0:x+1]) for x in range(len(xp_increments))]
    xp_to_next_level = xp_increments[level]
	'''max_health is a public var for now '''
    def __init__(self,damage=10,health=30,max_health=50,name="Hero",**kwargs):
        self.max_health = max_health
        super().__init__(damage,health,name,**kwargs)
    def rest(self):
        if self.GetHealth() >= self.max_health:
            print("No need to rest")
            self.SetHealth(max_health)
            return
        self.GetHealth() += self.GetDamage()
        print
        if self.GetHealth() > max_health:
        	self.GetHealth() = max_health
    def level_check(enemy):
        self.xp += enemy.health
        if self.xp is self.xp_to_next_level:
            self.level += 1
            print("You have leveled up to Level {}!!".format(self.level))
            self.xp_to_next_level = self.xp_increments[self.level]
        else:
            print("You have {} XP remaining to Level {}".format(self.xp_level[self.level+1]-self.xp,self.level+1))
    def __str__(self):
        return "____________________________________\nName: {0}\nHealth: {1}\nLevel: {2}\nTotal XP towards next level: {3}\n____________________________________\n".format(self.name,self.GetHealth(),self.level,self.xp_level[self.level+1]-self.xp)        
    def Attack(self,enemy):
        super().Attack(enemy)
        if enemy.health == 0:
            level_check(enemy)
class Monster(Character):
	def __init__(self,damage,health,name,**kwargs):
		super().__init__(damage,health,name,**kwargs)	        	
class Goblin(Monster):
    def __init__(self,damage=5,health=10,name="Goblin",**kwargs):
        super().__init__(damage,health,name,**kwargs)
    def __str__(self):
        return "Name: {}\nHealth: {}\n".format(self.name, self.GetHealth())
class Orc(Monster):
    def __init__(self,damage=10,health=20,name="Orc",**kwargs):
        super().__init__(damage,health,name,**kwargs)
    def __str__(self):
        return "Name: {}\nHealth: {}\n".format(self.name,self.GetHealth())
def explore():
    monster = random.choices(population=[Orc(),Goblin(),None],cum_weights=[0.1,0.5,1.0],k=1)
    return monster[0]
