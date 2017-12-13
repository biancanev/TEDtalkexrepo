import random
inventory1 = []
P1_health = 100
def inventory(storyline):
  if storyline == 1:
    print 'You have nothing in your inventory'
    scene1 = raw_input('What do you do?')
    if scene1 != F:
      print 'You cant do that here'
    else:
      forest()
  if storyline == 2:
    print inventory
def forest():
  print 'The forest is dark and foreboding, you shiver at the sight of it. However, you notice a small KNIFE on the ground . . . [Type PICK KNIFE to pick up the knife]'
  scene2 = raw_input('What do you do?')
  if scene2 == 'PICK KNIFE':
    inventory1.append('knife')
    print 'You picked up the knife, heading towards the CASTLE . . .'
print 'To access the Inventory, press I'
print
print
print 'You arrive to find your house in ruins. Intent on finding the culprit, you head out on your journey . . . [type F to go to the Forest]'
scene1 = raw_input('What do you do?')
if scene1 == 'I':
  inventory(1)
elif scene1 == 'F':
  forest() 
