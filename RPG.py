class Character():
    '''Assuming name is public, health and damage are private variables'''
    def __init__(self, damage, health, name, **kwargs):
        self.damage = damage
        self.health = health
        self.name = name

    def Attack(self, enemy):
        enemy.Take_damage(self.damage)

    def Take_damage(self, damage):
        if self.health <= damage:
            print(self.name + " Wasted")
            self.health = 0
        else:
            self.health -= damage


class Hero(Character):
    '''max_health is a public var for now '''
    def __init__(self, damage=10, health=30, max_health=50, name="Hero", **kwargs):
        self.max_health = max_health
        super().__init__(damage, health, name, **kwargs)
        self.xp = 0
        self.level = 1
        self.xp_increments = [i for i in range(0, 210, 10)]
        self.xp_level = [sum(self.xp_increments[0:x+1]) for x in range(len(
            self.xp_increments))]
        self.xp_to_next_level = self.xp_increments[self.level]

    def rest(self):
        if self.health >= self.max_health:
            print("No need to rest")
            self.health = max_health
            return
        self.health += self.damage
        print
        if self.health > max_health:
            self.health = max_health

    def level_check(enemy):
        self.xp += enemy.health
        if self.xp is self.xp_to_next_level:
            self.level += 1
            print("You have leveled up to Level {}!!".format(self.level))
            self.xp_to_next_level = self.xp_increments[self.level]
        else:
            print("You have {} XP remaining to Level {}".format(self.xp_level[self.level+1]-self.xp, self.level+1))

    def __str__(self):
        return "____________________________________\nName: {0}\n"\
        "Health:{1}\nLevel: {2}\nTotal XP towards next level: {3}\n"\
        "____________________________________\n".format(self.name,
        self.health, self.level, self.xp_level[self.level+1]-self.xp)

    def Attack(self, enemy):
        super().Attack(enemy)
        if enemy.health == 0:
            level_check(enemy)


class Monster(Character):
    def __init__(self, damage, health, name, prob, **kwargs):
        self.prob = prob
        super().__init__(damage, health, name, **kwargs)


class Goblin(Monster):
    def __init__(self, damage=5, health=10, name="Goblin", prob=0.4, **kwargs):
        super().__init__(damage, health, name, prob, **kwargs)

    def __str__(self):
        return "Name: {}\nHealth: {}\n".format(self.name, self.health)


class Orc(Monster):

    def __init__(self, damage=10, health=20, name="Orc", prob=0.1, **kwargs):
        super().__init__(damage, health, name, prob, **kwargs)

    def __str__(self):
        return "Name: {}\nHealth: {}\n".format(self.name, self.health)
monster_subs = [m.__name__+str('()') for m in Monster.__subclasses__()]
monster_subs = [eval(i) for i in monster_subs]
prob_spawn = [m.prob for m in monster_subs]
prob_spawn.append(1-sum(prob_spawn))
monster_subs.append(None)


def explore():
    monster = random.choices(population=monster_subs, weights=prob_spawn, k=1)
    return monster[0]
