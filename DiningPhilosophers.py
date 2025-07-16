import random
import time

class Philosopher:
    def __init__(self, id, spoons):
        self.id = id
        self.spoons = spoons

    def eat(self):
        spoon1 = self.id
        spoon2 = (self.id + 1) % len(self.spoons)

        if self.spoons[spoon1] and self.spoons[spoon2]:
            self.spoons[spoon1] = False
            self.spoons[spoon2] = False
            print(f"Philosopher {self.id} ate.")
            time.sleep(0.1)
        else:
            print(f"Philosopher {self.id} couldn't eat.")

    def give_up(self):
        spoon1 = self.id
        spoon2 = (self.id + 1) % len(self.spoons)
        self.spoons[spoon1] = True
        self.spoons[spoon2] = True
        print(f"Philosopher {self.id} gave up spoons.")

def main():
    num_philosophers = 10
    spoons = [True] * num_philosophers
    philosophers = [Philosopher(i, spoons) for i in range(num_philosophers)]

    for philosopher in philosophers:
        action = random.choice(['eat', 'give_up'])
        if action == 'eat':
            philosopher.eat()
        else:
            philosopher.give_up()
    time.sleep(0.5)

if __name__ == "__main__":
    main()
