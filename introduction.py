def get_info():
    name = input("Please enter your name: ")
    age = int(input("Please enter your age: "))
    print()
    return name, age

name, age = get_info()
print("Name: ", name)
print("Age: ", age) 