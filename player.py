import random
# ============================================================
# 2. PLAYER CLASS
# ============================================================
# The Player class is the blueprint for the player's character.
#
# A class allows us to group:
#   - Data about the player
#   - Functions that control what the player can do
#
# PROJECT NOTE:
# Classes are useful in games because characters have both
# attributes (data) and behaviours (actions).
# ============================================================

class Player:

    # ========================================================
    # 3.1 PLAYER INITIALISATION
    # ========================================================
    # __init__ runs automatically when a new Player object
    # is created.
    #
    # self refers to the particular Player object being created.
    #
    # PROJECT NOTE:
    # __init__ is used to give an object its starting attributes.
    # ========================================================

    def __init__(self, name, player_class, health):
        self.name = name
        self.player_class = player_class
        self.health = health
        self.max_health = health

        # -------------------------------
        # Character progression
        # -------------------------------

        self.level = 1
        self.xp = 25
        self.xp_to_next_level = 100

        # -------------------------------
        # Basic attack
        # -------------------------------

        self.attack_min = 3
        self.attack_max = 7

        # -------------------------------
        # Special attack
        # -------------------------------

        self.special_min = 6
        self.special_max = 12
        self.special_cooldown = 0

        # -------------------------------
        # Resources
        # -------------------------------

        self.potions = 3
        self.gold = 50

        # -------------------------------
        # Inventory and equipment
        # -------------------------------

        self.inventory = []
        self.equipped_weapon = "None"
        self.weapon_bonus = 0


    # ========================================================
    # 4. LEVEL-UP SYSTEM
    # ========================================================
    # Checks whether the player has enough XP to level up.
    #
    # while is used rather than if so that multiple level-ups
    # can happen if the player somehow receives a large amount
    # of XP at once.
    #
    # PROJECT NOTE:
    # This section demonstrates:
    #   - while loops
    #   - object attributes
    #   - arithmetic
    #   - comparison operators
    #   - progression systems
    # ========================================================

    def check_level_up(self):

        while self.xp >= self.xp_to_next_level:

            self.level += 1
            self.xp -= self.xp_to_next_level
            self.xp_to_next_level *= 2

            self.max_health += 3
            self.health = self.max_health

            self.attack_min += 1
            self.attack_max += 1

            self.special_min += 1
            self.special_max += 1

            print()
            print("========================")
            print("LEVEL UP")
            print("========================")
            print("Congratulations! You reached Level", self.level)
            print()
            print("Max Health:", self.max_health)
            print("Attack:", self.attack_min, "-", self.attack_max)
            print("XP remaining:", self.xp)
            print("XP needed for next level:", self.xp_to_next_level)
            print("========================")


    # ========================================================
    # 5. XP SYSTEM
    # ========================================================
    # Adds XP to the player's current XP total and then checks
    # whether the player has reached the next level.
    #
    # PROJECT NOTE:
    # This demonstrates how one method can call another method
    # belonging to the same object using self.
    # ========================================================

    def gain_xp(self, amount):

        self.xp += amount

        print("You gained", amount, "XP!")
        print("Current XP:", self.xp)

        self.check_level_up()


    # ========================================================
    # 6. POTION SYSTEM
    # ========================================================
    # Allows the player to restore health by using a potion.
    #
    # The method checks:
    #   - Whether the player has potions
    #   - Whether the player's health is already full
    #   - How much health should be restored
    #
    # PROJECT NOTE:
    # This section demonstrates conditional logic and making
    # sure values do not exceed a maximum.
    # ========================================================

    def use_potions(self):

        if self.potions <= 0:
            print("You have no potions left!")

        elif self.health == self.max_health:
            print("You are already at full health!")

        else:
            healing = 5
            self.health += healing

            if self.health > self.max_health:
                self.health = self.max_health

            self.potions -= 1

            print(self.name, "uses a potion!")
            print("Healed:", healing)
            print("Health:", self.health)
            print("Potions remaining:", self.potions)


    # ========================================================
    # 7. NORMAL ATTACK
    # ========================================================
    # Performs the player's standard attack.
    #
    # There is a 20% chance of a critical hit.
    #
    # Normal attacks use:
    #   attack_min
    #   attack_max
    #   weapon_bonus
    #
    # Critical attacks can deal additional damage.
    #
    # PROJECT NOTE:
    # This section demonstrates:
    #   - random numbers
    #   - if/else
    #   - arithmetic
    #   - modifying another object's attributes
    #   - returning a value
    # ========================================================

    def attack(self, enemy):

        roll = random.randint(1, 100)

        if roll <= 20:

            print("Critical Hit!")

            damage = random.randint(
                self.attack_max + self.weapon_bonus,
                self.attack_max + self.weapon_bonus + 3
            )

        else:

            print("Normal Hit.")

            damage = random.randint(
                self.attack_min + self.weapon_bonus,
                self.attack_max + self.weapon_bonus
            )

        print(self.name, "attacks", enemy.name + "!")
        print("Damage:", damage)

        enemy.health -= damage

        if enemy.health < 0:
            enemy.health = 0

        return damage


    # ========================================================
    # 8. SNEAK ATTACK / COOLDOWN
    # ========================================================
    # Sneak Attack is a stronger attack but cannot be used
    # every turn.
    #
    # When used successfully, the cooldown becomes 3.
    #
    # If the player tries to use it during cooldown, the attack
    # does NOT happen.
    #
    # The enemy still gets its normal turn afterwards because
    # the main game loop continues.
    #
    # This is intentionally designed so the PLAYER must keep
    # track of the cooldown rather than the game preventing the
    # player from making the choice.
    #
    # PROJECT NOTE:
    # This demonstrates:
    #   - state tracking
    #   - Boolean return values
    #   - cooldown mechanics
    #   - conditional logic
    # ========================================================

    def special_attack(self, enemy):

        if self.special_cooldown > 0:

            print("Sneak Attack is on cooldown!")
            print("Turns remaining:", self.special_cooldown)

            return False

        damage = random.randint(
            self.special_min,
            self.special_max
        )

        print(self.name, "uses Sneak Attack!")
        print("Damage:", damage)

        enemy.health -= damage

        if enemy.health < 0:
            enemy.health = 0

        self.special_cooldown = 3

        return True


    # ========================================================
    # 9. CHARACTER STATUS
    # ========================================================
    # Displays the player's current character information.
    #
    # PROJECT NOTE:
    # This demonstrates how object attributes can be displayed
    # to the player and how calculated values can be shown.
    # ========================================================

    def show_status(self):

        print()
        print("====================")
        print("CHARACTER STATUS")
        print("====================")

        print("Name:", self.name)
        print("Class:", self.player_class)
        print("Level:", self.level)
        print("Health:", self.health, "/", self.max_health)
        print("XP:", self.xp, "/", self.xp_to_next_level)

        print(
            "Attack:",
            self.attack_min + self.weapon_bonus,
            "-",
            self.attack_max + self.weapon_bonus
        )

        print("Sneak Attack:", self.special_min, "-", self.special_max)
        print("Sneak Attack Cooldown:", self.special_cooldown)
        print("Potions:", self.potions)
        print("Gold:", self.gold)

        print("=====================")


    # ========================================================
    # 10. RECEIVING LOOT
    # ========================================================
    # Adds an item to the player's inventory.
    #
    # Inventory currently stores weapons as tuples:
    #
    # ("Iron Dagger", 1)
    #
    # PROJECT NOTE:
    # This introduces storing multiple pieces of information
    # together inside a list.
    # ========================================================

    def receive_loot(self, item, bonus):

        self.inventory.append((item, bonus))

        print()
        print("=================")
        print("LOOT FOUND!")
        print("=================")
        print("You found:", item)
        print("=================")


    # ========================================================
    # 11. EQUIP WEAPON
    # ========================================================
    # Changes the player's currently equipped weapon.
    #
    # The weapon bonus is then used by the normal attack.
    #
    # PROJECT NOTE:
    # This demonstrates how one system can affect another system.
    #
    # Inventory -> Equipment -> Attack Damage
    # ========================================================

    def equip_weapon(self, weapon_name, bonus):

        self.equipped_weapon = weapon_name
        self.weapon_bonus = bonus

        print()
        print("=================")
        print("WEAPON EQUIPPED")
        print("=================")
        print("Weapon:", self.equipped_weapon)
        print("Attack Bonus: +", self.weapon_bonus)
        print("=================")


    # ========================================================
    # 12. INVENTORY DISPLAY
    # ========================================================
    # Displays everything currently stored in the inventory.
    #
    # enumerate() gives each item a number.
    #
    # PROJECT NOTE:
    # This demonstrates:
    #   - lists
    #   - tuples
    #   - for loops
    #   - enumerate()
    #   - checking whether a list is empty
    # ========================================================

    def show_inventory(self):

        print()
        print("===============")
        print("INVENTORY")
        print("===============")

        if not self.inventory:

            print("Your inventory is empty.")

        else:

            for item in self.inventory:
                print("-", item[0], "(+", item[1], ")")

        print()
        print("Equipped Weapon:", self.equipped_weapon)
        print("Weapon Bonus: +", self.weapon_bonus)
        print("===============")


    # ========================================================
    # 13. WEAPON SELECTION
    # ========================================================
    # Allows the player to select a weapon from the inventory.        #
    # The player's input is checked before accessing the list.
    #
    # PROJECT NOTE:
    # This demonstrates:
    #   - input validation
    #   - string methods
    #   - converting strings to integers
    #   - list indexes
    #   - conditional logic
    # ========================================================
        
    def choose_weapon(self, game_input):
        
        if not self.inventory:
        
            print("You have no weapons in your inventory.")
            return
        
        print()
        print("================")
        print("CHOOSE A WEAPON")
        print("================")
        
        for number, item in enumerate(self.inventory, start=1):
            print(number, "-", item[0], "(+", item[1], ")")
        
        print("0 - Cancel")
        
        choice = game_input("Choose a weapon: ")
        
        if choice == "0":
        
            print("Cancelled.")
            return
        
        if choice.isdigit():
        
            choice = int(choice)
        
            if 1 <= choice <= len(self.inventory):
        
                weapon = self.inventory[choice - 1]
        
                self.equip_weapon(
                    weapon[0],
                    weapon[1]
                )
        
            else:
        
                print("Invalid weapon choice.")
        
        else:
        
            print("Invalid choice.")


