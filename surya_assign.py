# 1. login function
def login():
    print("welcome")
    username = input("username:  ")
    password = input("password:    ")
    if username == "surya" and password == "passwo":
        print("login successful")
    else:
        print("credential failure")
        return login()
login()

# 2.write s prgram to find odd number and even number
num = int(input("please enter a numner:"))
if num%2 ==0:
    print("the number is even")
else:
    print("the number is odd")


# 3. create a list of fruits and iterate through them
fruits = ["APPLE", "MANGO","ORANGE", "BANANA", "KIWI","POMEGRANATE"]
FRUIT = [x for x in fruits if "L" in x]
Tasty = [x for x in fruits  if "E" in x]
yummy = [x for x in fruits  if "O" in x]
Healthy = [x for x in fruits  if "A" in x]
print(FRUIT)
print(Tasty)
print(yummy)
print(Healthy)

