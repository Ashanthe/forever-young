from RobotArm import RobotArm

robotArm = RobotArm('exercise 6')
robotArm.speed = 3
# Jouw python instructies zet je vanaf hier:
# Op volgorde
for i in range(7):
    robotArm.moveRight()
        
robotArm.grab()
robotArm.moveRight()   
robotArm.drop()
for x in range(8):
    robotArm.moveLeft()
    robotArm.grab()
    robotArm.moveRight()
    robotArm.drop()
    robotArm.moveLeft()   


       


    

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()