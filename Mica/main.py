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
                    mica.cmds.body.do_forward(30, 10)
                    
                elif strCmd == "Back":
                    mica.cmds.body.do_forward(-30, 10)
                    
                elif strCmd == "Right":
                    mica.cmds.body.do_turn(-90, 200)
                    
                elif strCmd == "Left":
                    mica.cmds.body.do_turn(90, 200)
        elif strMode = "Free Time":

            #The variable used for AI
            
            ftm = random.randint(0, 20)
            ftm1 = random.randint(0, 20)
            ftm2 = random.randint(0, 20)
            ftm3 = random.randint(0, 20)
            ftm4 = random.randint(0, 20)
            print("%s is so happy that he gets free time!" % mica.name)

            if ftm == 1:
                if ftm1 > 19:
                    print("%s is bored." % mica.name)
                    mica.cmds.body.do_turn(-90, 200)
                    
           
           
        print("That's all for now.")

    

# kick off the program !
if __name__ == "__main__":
    WonderPy.core.wwMain.start(Mica())
