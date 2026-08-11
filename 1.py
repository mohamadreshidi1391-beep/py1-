# Simple Creature Game - Teaching Classes and Objects

class Creature:
    """A class to represent a creature in our game"""
    
    def __init__(self, name, creature_type, health=100, attack_power=10):
        """Initialize a creature with basic attributes"""
        self.name = name
        self.creature_type = creature_type
        self.health = health
        self.attack_power = attack_power
        self.level = 1
        self.experience = 0
        
    def attack(self, target):
        """Attack another creature"""
        print(f"{self.name} attacks {target.name} for {self.attack_power} damage!")
        target.take_damage(self.attack_power)
        
    def take_damage(self, damage):
        """Take damage from an attack"""
        self.health -= damage
        print(f"{self.name} takes {damage} damage! Health: {self.health}")
        
        if self.health <= 0:
            print(f"{self.name} has been defeated!")
            
    def gain_experience(self, exp):
        """Gain experience points"""
        self.experience += exp
        print(f"{self.name} gained {exp} experience points!")
        
        # Check if we level up
        if self.experience >= 100:
            self.level_up()
            
    def level_up(self):
        """Level up the creature"""
        self.level += 1
        self.health += 20
        self.attack_power += 5
        self.experience = 0
        print(f"*** {self.name} leveled up to level {self.level}! ***")
        print(f"Health: {self.health}, Attack Power: {self.attack_power}")
        
    def __str__(self):
        """String representation of the creature"""
        return f"{self.name} ({self.creature_type}) - Level {self.level} | Health: {self.health} | Attack: {self.attack_power}"

# Game class to manage the game
class Game:
    """Class to manage the game"""
    
    def __init__(self):
        """Initialize the game"""
        self.creatures = []
        self.player_creature = None
        
    def create_creature(self, name, creature_type):
        """Create a new creature"""
        creature = Creature(name, creature_type)
        self.creatures.append(creature)
        return creature
        
    def start_game(self):
        """Start the game"""
        print("=== WELCOME TO CREATURES VS MONSTERS ===")
        print("Create your own creature and battle against monsters!")
        
        # Create player's creature
        name = input("What is your creature's name? ")
        creature_type = input("What type of creature are you? (e.g. Dragon, Wizard, Warrior) ")
        self.player_creature = self.create_creature(name, creature_type)
        print(f"\nGreat! Your creature is: {self.player_creature}")
        
        # Create some monsters
        monster1 = self.create_creature("Goblin", "Goblin")
        monster2 = self.create_creature("Orc", "Orc")
        monster3 = self.create_creature("Skeleton", "Undead")
        
        print("\n=== BATTLE TIME ===")
        print("Your creatures:")
        for creature in self.creatures:
            print(f"  - {creature}")
            
        # Simple battle
        self.battle(self.player_creature, monster1)
        
    def battle(self, creature1, creature2):
        """Simulate a battle between two creatures"""
        print(f"\n--- BATTLE: {creature1.name} vs {creature2.name} ---")
        
        # Simple turn-based battle
        turn = 1
        while creature1.health > 0 and creature2.health > 0:
            print(f"\n--- Turn {turn} ---")
            creature1.attack(creature2)
            
            if creature2.health > 0:
                creature2.attack(creature1)
            
            turn += 1
            
        # Determine winner
        if creature1.health > 0:
            print(f"\n🎉 {creature1.name} wins the battle!")
            creature1.gain_experience(50)
        else:
            print(f"\n💀 {creature2.name} wins the battle!")
            creature2.gain_experience(50)

# Run the game
if __name__ == "__main__":
    # Create and start the game
    game = Game()
    game.start_game()
    
    # Show all creatures at the end
    print("\n=== FINAL CREATURE STATUS ===")
    for creature in game.creatures:
        print(creature)
