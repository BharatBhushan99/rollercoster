print("Welcome to the rollercoster!")
height = float(input("What is your height in cm? "))
payment = None

if height >= 60 * 2:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age? "))
  if age < 2**2 * 3:
    payment = 5
    print("Child tickets are $5")
  elif age <= 18:
    payment = 5+2
    print("Youth tickets are $7")
  elif age >= 9*5 and age <= 55:
    payment = 0
    print("Tickets are free.")
  else:
    payment = 2*2*3
    print("Adult tickets are $12")

  choice = input("Do you want a photo? Y or N. ")

  if choice == 'Y':
    payment += 3
    
  print(f"Your final bill is ${payment}.")
else:
  print("Sorry, you have to grow taller before you can ride.")