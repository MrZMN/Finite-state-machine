#!/usr/bin/env python
# coding: utf-8

class Robot(object):
    
    def __init__(self):
        self.fsm = IdleState()      # initial state
        self.fsm.enter_state(self)
        self.fsm.exec_state(self)
    
    def change_state(self, new_fsm):
        self.fsm.exit_state(self) 
        self.fsm = new_fsm 
        self.fsm.enter_state(self) 
        self.fsm.exec_state(self)
        
    # motions
    def speak(self, text):
        print(text)
        
    def move(self, x, y, z):
        print("Moving to:", x, y, z)



class BaseState(object):
    #    template of all states

    def enter_state(self, obj):
        raise NotImplementedError()

    def exec_state(self, obj):
        raise NotImplementedError()
    
    def exit_state(self, obj):
        raise NotImplementedError()



class IdleState(BaseState):
    
    def enter_state(self, obj):
        pass
        
    def exec_state(self, obj):
        print("zzz...")
        
    def exit_state(self, obj):
        print("Wake up!")



class SpeakState(BaseState):
    
    def enter_state(self, obj):
        pass

    def exec_state(self, obj):
        obj.speak("Hi I'm NAO")
        self.exit_state(obj)

    def exit_state(self, obj):
        obj.fsm = IdleState()
        obj.fsm.enter_state(obj)
        obj.fsm.exec_state(obj)



class MoveState(BaseState):

    def enter_state(self, obj):
        pass

    def exec_state(self, obj):
        obj.move(1,1,1)
        self.exit_state(obj)

    def exit_state(self, obj):
        obj.fsm = IdleState()
        obj.fsm.enter_state(obj)
        obj.fsm.exec_state(obj)



class StateMgr(object):

    def __init__(self):
        self.fsms = {}
        self.fsms[0] = IdleState()     # 0 is idle state
        self.fsms[1] = SpeakState()    # 1 is speak state
        self.fsms[2] = MoveState()     # 2 is move state
    
    def frame(self, robot, state):    # change state of a robot given input
        robot.change_state(self.fsms[state])



class World(object):

    def __init__(self):
        self.robot = Robot() 
        self.StateMgr = StateMgr() 
        
    # run state machine according to input
    def run(self):
        while True:
            command = input("What do you want from NAO?")
            
            if command == "speak":
                self.StateMgr.frame(self.robot, 1)    
            elif command == "move":
                self.StateMgr.frame(self.robot, 2)    



if __name__ == "__main__":
    world = World() 
    world.run()


# https://blog.51cto.com/flandycheng/389597
