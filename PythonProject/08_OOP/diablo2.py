basic_energy = 10

def sing():
    return "lalala~~~"

class Amazon:

    strength = 20
    dexterity = 25
    vitality = 20
    energy = basic_energy + 15

    def attack(self):
        return  '=> Jab Jab'

    def exercise(self):
        self.strength += 2
        self.dexterity +=3
        self.vitality += 1

