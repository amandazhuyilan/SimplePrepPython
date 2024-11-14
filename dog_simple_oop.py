# Write a Python program that defines a Dog class with the following characteristics:

# A private member variable _name (string) that stores the dog's name.
# A private member variable _age (int) that stores the dog's age.
# A public constructor that initializes _name and _age.
# A public method bark that prints "Woof!".
# A public method get_info that returns a string in the format: "Name: {name}, Age: {age}".

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("woof")

    def get_info(self):
        return(f"Name: {self.name}, age: {self.age}")


if __name__ == "__main__":
    my_dog = Dog("jeff", 2)
    my_dog.bark()
    print(my_dog.get_info())