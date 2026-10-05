from player import Player
from enemy import Enemy



def start_combat(player, enemy, game_input, clear_screen):


    while enemy.health > 0 and player.health > 0:

    
        print()
        print("What do you want to do")
        print("1. Attack")
        print("2. Sneak Attack")
        print("3. Defend")
        print("4. Potion")
        print("5. Run")
        print("6. Character Status")
        print("7. Inventory")
    
        choice = game_input("Choose an action: ")
    
    
        defending = False
    
    
    
        if choice == "1":
    
            player.attack(enemy)
    
            print("Enemy Health:", enemy.health)
    
            if enemy.health <= 0:
    
                return "Victory"
                
    
    
    
        elif choice == "2":
    
            player.special_attack(enemy)
    
            print("Enemy Health:", enemy.health)
    
            if enemy.health <= 0:
    
                return "Victory"
                
    
    
    
        elif choice == "3":
    
            print(player.name, "defends!")
    
            defending = True
    
    
    
        elif choice == "4":
    
            player.use_potions()
    
    
    
        elif choice == "5":
    
            print(player.name, "runs away!")
    
            return "Run"
    
    
    
        elif choice == "6":
    
            player.show_status()
    
            continue
    
    
    
        elif choice == "7":
    
            player.show_inventory()
    
            print("1. Equip Weapon")
            print("2. Return")
    
            inventory_choice = game_input("Choose an option: ")
    
            if inventory_choice == "1":
    
                player.choose_weapon(game_input)
    
            continue
    
    
    
        else:
    
            print("Invalid choice!")
    
            continue
    
    
        print()
    
        enemy_fled = enemy.attack(player, defending)
    
        print("Player Health:", player.health)
    
    
    
        if enemy_fled:
    
            print()
            print(enemy.name, "has escaped!")
    
            return "Enemy Fled"
    
    
    
        if player.special_cooldown > 0:
    
            player.special_cooldown -= 1
    
    
    
        if player.health <= 0:
    
            return "Defeat"
    
    
    
    if enemy.health <= 0:

        print()
        print("====================")
        print("VICTORY")
        print("====================")
    
        return "Victory"