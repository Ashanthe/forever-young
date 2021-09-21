from RobotArm import RobotArm

robotArm = RobotArm('exercise 6')
robotArm.speed = 2
# Jouw python instructies zet je vanaf hier:
# Op volgorde
robotArm.moveRight()
robotArm.grab()
for x in range(0,7):
    robotArm.moveRight()
robotArm.drop()
for x in range(0,8):
    robotArm.moveLeft()
robotArm.grab()
robotArm.moveRight()
robotArm.drop()
for right in range(0,7):
    robotArm.moveRight()
robotArm.grab()
for d in range(0,7):
    robotArm.moveLeft()
robotArm.drop()
robotArm.moveRight()
robotArm.grab()
robotArm.moveLeft()
robotArm.drop()
for k in range(0,2):
    robotArm.moveRight()
robotArm.grab()
for l in range(0,2):
    robotArm.moveLeft()
robotArm.drop()
for c in range(0,3):
    robotArm.moveRight()
robotArm.grab()
for d in range(0,3):    
    robotArm.moveLeft()
robotArm.drop()
for e in range(0,4):
    robotArm.moveRight()
robotArm.grab()
for f in range(0,4):
    robotArm.moveLeft()
robotArm.drop()   
for g in range(0,5):
    robotArm.moveRight()
robotArm.grab()
for h in range(0,5):
    robotArm.moveLeft()
robotArm.drop() 
for i in range(0,4):
    robotArm.moveRight()
robotArm.grab()  
for j in range(0,4):
    robotArm.moveLeft()
robotArm.drop()  
for k in range(0,6):
    robotArm.moveRight()
robotArm.grab()
for l in range(0,6):   
    robotArm.moveLeft()
robotArm.grab()







    

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()