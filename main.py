
from player import Player
from enemy import Enemy
from combat import start_combat


import random


def start_game(game_input, clear_screen, game_heading):

    player = Player(
        "Toogar Sarbar",
        "Rogue",
        14
    )
    while player.health > 0:

        clear_screen()

        enemy = create_enemy(player)

        print()
        print("======================")
        print("A new enemy approaches!")
        print("======================")
        print("Enemy:", enemy.name)
        print("Health:", enemy.health)
        print("Type:", enemy.enemy_type)
        print()

        result = start_combat(player, enemy, game_input, clear_screen)

        if result == "Victory":

            clear_screen()

            print()
            print("====================")
            game_heading("VICTORY")
            print("====================")

            defeat_enemy(player, enemy, game_input)

        if result == "Defeat":

            clear_screen()

            print()
            print("====================")
            game_heading("DEFEAT")
            print("====================")

            print()
            print("You have been defeated by", enemy.name + ".")
            print("Game Over.")

            break


        continue_game = game_input("Fight another enemy? (y/n): ").lower()

        if continue_game != "y":

            print()
            print("Thanks for playing!")

            break


def create_enemy(player):


    enemies = [

        Enemy(
            "Goblin",
            20,
            2,
            5,
            25,
            1,
            5,
            10,
            "normal"
        ),

        Enemy(
            "Wolf",
            15,
            3,
            6,
            20,
            2,
            8,
            15,
            "fast"
        ),

        Enemy(
            "Orc",
            35,
            4,
            8,
            50,
            3,
            15,
            25,
            "strong"
        ),

        Enemy(
            "Rat",
            10,
            1,
            3,
            15,
            1,
            2,
            5,
            "weak"
        )
    ]


    available_enemies = [

        enemy for enemy in enemies
        if enemy.level <= player.level

    ]


    enemy = random.choice(available_enemies)


    enemy.health += player.level - enemy.level
    enemy.max_health = enemy.health

    enemy.min_damage += player.level - enemy.level
    enemy.max_damage += player.level - enemy.level

    return enemy


def reward_gold(player, enemy):

    gold = random.randint(
        enemy.gold_min,
        enemy.gold_max
    )

    player.gold += gold

    print()
    print("You found", gold, "gold!")
    print("Total gold:", player.gold)




def generate_loot(player, enemy, game_input):


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

        equip = game_input(
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



def defeat_enemy(player, enemy, game_input):

    print()
    print("=================")
    print("ENEMY DEFEATED")
    print("=================")

    player.gain_xp(enemy.xp_reward)

    generate_loot(player, enemy, game_input)

    reward_gold(player, enemy)




