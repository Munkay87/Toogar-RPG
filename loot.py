


def reward_gold(player, enemy):

    gold = random.randint(
        enemy.gold_min,
        enemy.gold_max
    )

    player.gold += gold

    print()
    print("You found", gold, "gold!")
    print("Total gold:", player.gold)



def generate_loot(player, enemy):


    loot_chance = random.randint(1, 100)

    if enemy.enemy_type == "weak":

        loot_chance_limit = 50

    else:

        loot_chance_limit = 30


    if loot_chance <= loot_chance_limit:

        weapons = [

            ("Iron Dagger", 1),
            ("Steel Dagger", 2),
            ("Hunter's Blade", 3),
            ("Shadow Dagger", 5)

        ]


        possible_weapons = [

            weapon for weapon in weapons
            if weapon[1] <= player.level + 2

        ]


        weapon = random.choice(possible_weapons)

        player.receive_loot(
            weapon[0],
            weapon[1]
        )

        print("Attack bonus:", weapon[1])

        equip = input(
            "Equip this weapon? (y/n):"
        ).lower()

        if equip == "y":

            player.equip_weapon(
                weapon[0],
                weapon[1]
            )

    else:

        print()
        print("No equipment found.")
        print("The enemy dropped nothing useful.")



def defeat_enemy(player, enemy):

    print()
    print("=================")
    print("ENEMY DEFEATED")
    print("=================")

    player.gain_xp(enemy.xp_reward)

    generate_loot(player, enemy)

    reward_gold(player, enemy)