from RobotArm import RobotArm

robotArm = RobotArm('exercise 2')
robotArm.speed = 5
# Jouw python instructies zet je vanaf hier:
for n in range(0,3):
    for move in range(0,9):
        robotArm.grab()
        robotArm.moveRight()
        robotArm.drop()
    for left in range(0,9):
        robotArm.moveLeft()


    


    
    




    


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()