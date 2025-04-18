class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []

    def eat(self):
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)

    def sleep(self):
        self.energy = min(10, self.energy + 5)

    def play(self):
        self.energy = max(0, self.energy - 2)
        self.happiness = min(10, self.happiness + 2)
        self.hunger = min(10, self.hunger + 1)

    def train(self, trick):
        self.tricks.append(trick)

    def show_tricks(self):
        print(f"\n{self.name}'s Tricks:")
        if self.tricks:
            for trick in self.tricks:
                print(f"- {trick}")
        else:
            print("No tricks learned yet.")

    def get_status(self):
        print(f'\nStatus of {self.name}:')
        print(f'Hunger: {self.hunger}')
        print(f'Energy: {self.energy}')
        print(f'Happiness: {self.happiness}')
