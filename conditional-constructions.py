
a = input("Input a: ")
b = input("Input b: ")

if a > b:
    print(f"{a} > {b}")
elif a == b:
    print(f"{a} = {b}")
else:
    print(f"{a} < {b}")

language = input(str("Enter the language you speak: "))
if language.lower() == "english":
    print("Hello")
elif language.lower() == "spanish":
    print("Hola!")
else:
    print("Glory to Ukraine!")

print("End!")