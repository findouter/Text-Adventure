# import statements
import time
import random
# global variables
inventory = {"torch": 2}
# print inventory
def print_inventory():
  global inventory
  for (k, v) in inventory.items():
    print("%s: %d" % (k, v))


def print_output(decision):
  choice = "i"
  while (choice == "i"):
    choice = input("{0} [y/n] \nEnter i to see you inventory. ".format(decision))
    if (choice == "i"):
      print_inventory()
  if choice in ['y', 'Y', 'Yes', 'YES', 'yes']:
    return True
  return False

def cyclops_battle(stick):
  print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
  print (" Fighting... ")
  print (" You must have above a 5 to kill the cyclops. ")
  print ("It the cyclops hits higher than you, you will die.")
  print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
  time.sleep(2)
  # calculate hit
  if stick:
    your_hit = int(random.randint(3, 10))
  else:
    your_hit = int(random.randint(1, 8))
  cyclops_hit = int(random.randint(1, 5))
  print ("you hit a", your_hit)
  print ("the cyclops hits a", cyclops_hit)
  time.sleep(2)
  
  if cyclops_hit > your_hit:
    print ("The cyclops has dealt more damage than you!")
    complete = 0
    return complete
  elif your_hit < 5:
    print ("You didn't do enough damage to kill the cyclops, but you manage to escape")
    complete = 1
    return complete
  else:
    print ("You killed the cyclops!")
    complete = 1
    return complete


