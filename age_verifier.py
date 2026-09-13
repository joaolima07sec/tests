from datetime import datetime
def age_verifier():
  while True:
    name = input("what's your name?: ")
    verifier = input("you typed the name correctly? (y/n)")
    if verifier == "y" or verifier == "Y":
      break

  while True:
    try:
      birthdate = int(input("what's the year you born?: "))
      age = datetime.now().year - birthdate
      break
    except ValueError:
      print("type a valid year")

  if age < 18:
    print('you are underage\n')
  elif age > 130:
    print('are you in a casket?\n')
  else:
    print(f'your name is {name} and your age is {age}\n')
  return name, age

my_list = []
users = 0

while True:
   name, age = age_verifier()
   people = input("wanna log more people? (y/n)\n")

   my_list.append(('name:', name, 'age:', age))
   users = users + 1 
   if people == 'n' or people == 'N':
     break

print (users)
print (my_list)
