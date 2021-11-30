# replitPython
print("welcome kateltnn")
# overview of if and else with user input
#first we'll print an intoduction:
print('Hi there, welcome to my story. You get up in the morning.')
#then let's get some user input. We'll assign a variable to the user's input:

choice1 = input('Do you get [up] or go back to [sleep]? ')

if choice1 == 'sleep':
  print("You go back to sleep and have a nightmare.")

  #let's add a choice here
  choice1a=input("You finally get up. Do you go to school? [yes] or [no] ")
  if choice1a=="yes":
    print("You are late to school. The End.")
  else:
    print("You stay home. The End.")
else:
  print("You get up and brush your teeth.")


  choice1b = input("do you ride your [bike] or steal a [car], or take the [bus]? ")
  if choice1b == "car":
    print("you get arrested. The End.")
  elif choice1b == "bus":
    print("You take the bus and get run over. The End.")
  elif choice1b == "bike":
    print("you ride your bike and get to school on time and refreshed. The End")
  else:
    print("You did't mak ea correct choice. The end.")  