from threading import Thread
import time
import guizero
import random


import WonderPy.core.wwMain
from WonderPy.core.wwConstants import WWRobotConstants
from WonderPy.components.wwMedia import WWMedia



class Mica(object):

    def on_connect(self, mica):
 
      #  Called when we connect to a mica.

        print("Connected to a Mica named %s." % (mica.name))
        Thread(target=self.micaThread, args=(mica,)).start()

    def micaThread(self, mica):
        # mica is the robot we've connected to.

        
        print("Welcome to Mica 1.0(alpha)\n\n")
        mica.cmds.RGB.stage_all(1, 1, 0)
        mode = raw_input("Mode(Free Time, Control): ")
        strMode = str(mode)

        if strMode == "Control":
             while True:
                cmd = raw_input("%s ready! >" % mica.name)
                strCmd = str(cmd)

                if strCmd == "Forward":
                    mica.cmds.body.do_forward(60, 10)
                    
                elif strCmd == "Back":
                    mica.cmds.body.do_forward(-60, 10)
                    
                elif strCmd == "Right":
                    mica.cmds.body.do_turn(-90, 200)
                    
                elif strCmd == "Left":
                    mica.cmds.body.do_turn(90, 200)
                elif strCmd == "Exit":
                    break
        elif strMode == "Free Time": 

          print("%s is so happy that he gets free time!" % mica.name)
          while True:
            #The variable used for AI
            
            ftm = random.randint(0, 20)
            ftm1 = random.randint(0, 20)
            ftm2 = random.randint(0, 20)
            ftm3 = random.randint(0, 20)
            ftm4 = random.randint(0, 20)

            if ftm == 1:
                if ftm1 > 19:
                    print("%s is bored" % mica.name)
                    mica.cmds.body.do_turn(-90, 200)
                    
            elif ftm == 2:
                print("%s is exploring his surroundings" % mica.name)
                mica.cmds.body.do_forward(30, 10)
                if ftm2 == 10:
                    mica.cmds.body.do_turn(90, 200)
                else:
                    mica.cmds.body.do_turn(-90, 200)
        
            elif ftm == 3:
                print("%s is dizzy" % mica.name)
                mica.cmds.body.do_turn(360, 200)
                
            elif ftm == 4:
                print("%s wants to play with you" % mica.name)

            elif ftm == 5:
              if ftm2 <= 10:
                print("%s wants to play Control Mode" % mica.name)
                rawDTP = raw_input("Do you want to play Control Mode with %s? " % mica.name)
                dtp = str(rawDTP)
                if dtp == "Yes":
                    print("Opening control mode..")
                    while True:
                        cmd = raw_input("%s ready! >" % mica.name)
                        strCmd = str(cmd)

                        if strCmd == "Forward":
                        mica.cmds.body.do_forward(60, 10)
                    
                        elif strCmd == "Back":
                            mica.cmds.body.do_forward(-60, 10)
                    
                        elif strCmd == "Right":
                            mica.cmds.body.do_turn(-90, 200)
                    
                        elif strCmd == "Left":
                            mica.cmds.body.do_turn(90, 200)
                        elif strCmd == "Exit":
                            break
            elif ftm == 6:
                print("%s is playing Disco!" % mica.name)
                lgt = random.randint(0, 1)
                lgt2 = random.randint(0, 1)
                lgt1 = random.randint(0, 1)
                mica.cmds.RGB.stage_all(lgt2, lgt, lgt1)
                time.sleep(0.5)
                lgt = random.randint(0, 1)
                lgt2 = random.randint(0, 1)
                lgt1 = random.randint(0, 1)
                mica.cmds.RGB.stage_all(lgt2, lgt, lgt1)
                time.sleep(0.5)
                lgt = random.randint(0, 1)
                lgt2 = random.randint(0, 1)
                lgt1 = random.randint(0, 1)
                mica.cmds.RGB.stage_all(lgt2, lgt, lgt1)
                time.sleep(0.5)
                lgt = random.randint(0, 1)
                lgt2 = random.randint(0, 1)
                lgt1 = random.randint(0, 1)
                mica.cmds.RGB.stage_all(lgt2, lgt, lgt1)
                time.sleep(0.5)
                lgt = random.randint(0, 1)
                lgt2 = random.randint(0, 1)
                lgt1 = random.randint(0, 1)
                mica.cmds.RGB.stage_all(lgt2, lgt, lgt1)
                time.sleep(0.5)
            elif ftm == 7:
                print("%s is hungry" % mica.name)
                rawFood = raw_input("Would you like to feed %s?" % mica.name)
                foodD = str(rawFood)
                if foodD == "Yes":
                    foodList = ["Nuts and Bolts", "Cereal", "Mango", "Pasta", "Ice Cream", "Popsicle", "Honeydew", "Almonds"]
                    ciList = random.randint(1,8)
                    print("Feeding Mica %s" % foodList[ciList])
                    print(".")
                    print("..")
            
                
                
                
                  
                
           
           
        print("That's all for now.")

    

# kick off the program !
if __name__ == "__main__":
    WonderPy.core.wwMain.start(Mica())
