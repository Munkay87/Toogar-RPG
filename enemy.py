import random


class Enemy:


    def __init__(
        self,
        name,
        health,
        min_damage,
        max_damage,
        xp_reward,
        level,
        gold_min,
        gold_max,
        enemy_type
    ):

        self.name = name
        self.health = health
        self.max_health = health
        self.min_damage = min_damage
        self.max_damage = max_damage
        self.xp_reward = xp_reward
        self.level = level
        self.gold_min = gold_min
        self.gold_max = gold_max
        self.enemy_type = enemy_type



    def attack_once(self, player, defending):

        roll = random.randint(1, 100)

        if self.enemy_type == "fast":
            critical_chance = 20
        else:
            critical_chance = 10

        if self.enemy_type == "strong":
            damage_bonus = 2
        else:
            damage_bonus = 0

        if roll <= critical_chance:

            print("CRITICAL HIT!")

            damage = random.randint(
                self.max_damage * 2 + damage_bonus,
                self.max_damage * 2 + 2 + damage_bonus
            )

        else:

            print("Normal Hit.")

            damage = random.randint(
                self.min_damage + damage_bonus,
                self.max_damage + damage_bonus
            )

        print(self.name, "attacks", player.name + "!")

        if defending:

            print(player.name, "is defending!")

            damage = damage // 2

        print("Damage:", damage)

        player.health -= damage

        if player.health < 0:
            player.health = 0

        return damage



    def attack(self, player, defending):


        self.attack_once(player, defending)


        if self.enemy_type == "fast" and player.health > 0:

            second_attack = random.randint(1, 100)

            if second_attack <= 25:

                print()
                print("SECOND ATTACK")
                print()

                self.attack_once(player, defending)


        if self.enemy_type == "weak":

            flee_chance = random.randint(1, 100)

            if self.health <= self.max_health * 0.25:

                flee_limit = 50

            elif self.health <= self.max_health * 0.50:

                flee_limit = 30

            else:

                flee_limit = 20

            if flee_chance <= flee_limit:

                print()
                print(self.name, "flees!")
                print()

                return True

        return False