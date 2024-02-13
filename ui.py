from animal import Animal
from dog import Dog
from cat import Cat

class UserInterface:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def display_animals(self):
        print("List of Animals:")
        for animal in self.animals:
            print(animal.speak())

    def run(self):
        while True:
            print("\n1. Add a Dog\n2. Add a Cat\n3. Display Animals\n4. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                name = input("Enter dog's name: ")
                dog = Dog(name)
                self.add_animal(dog)
            elif choice == '2':
                name = input("Enter cat's name: ")
                cat = Cat(name)
                self.add_animal(cat)
            elif choice == '3':
                self.display_animals()
            elif choice == '4':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    ui = UserInterface()
    ui.run()
