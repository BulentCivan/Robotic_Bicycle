from controller import Robot
import math
from controller import Supervisor
import sys
import matplotlib.pyplot as plt

TIMESTEP = 64
MAX_SPEED = 6.28
WHEEL_RADIUS = 0.14

if __name__ == "__main__":    

    supervisor = Supervisor() 
    
    cube = supervisor.getFromDef("TARGET")
    cube_translation = cube.getField("translation")  
    
    bicycle_robot = supervisor.getFromDef("robot")     
    bicycle_translation = bicycle_robot.getField("translation")
    bicycle_rotation = bicycle_robot.getField("rotation") 
    
    motor_shaft = supervisor.getDevice('motor_shaft')
    motor_steering = supervisor.getDevice('motor_steering')
    motor_front= supervisor.getDevice('motor_front')
    
    motor_shaft.setPosition( float ('inf'))
    motor_shaft.setVelocity( 0.0)
    motor_steering.setPosition( float ('inf'))
    motor_steering.setVelocity( 0.0)
    motor_front.setPosition( float ('inf'))
    motor_front.setVelocity( 0.0)

    ps_steering = supervisor.getDevice('ps_front1')
    ps_steering.enable(TIMESTEP)

    Xvalues = [] #stores x position values of the robot
    Yvalues = [] #stores y position values of the robot
    
    # Main loop:
    while supervisor.step(TIMESTEP) != -1:
       
       target_position = cube_translation.getSFVec3f()  
       target_x = target_position[0]
       target_y = target_position[1]
       rotation_angle = bicycle_rotation.getSFRotation()[3]
       
       if target_x <0 and target_y > 0:
           rotation_angle =rotation_angle - 3.1415 # to the left
       elif target_x < 0 and target_y < 0:
           rotation_angle=-rotation_angle + 3.1415 # to the right
       elif target_x > 0 and target_y < 0:
           rotation_angle=-rotation_angle # opposite direction
           
       ps_value=ps_steering.getValue()#Steering turn value
       
       translation_values = bicycle_translation.getSFVec3f()
       current_x = translation_values[0]
       current_y = translation_values[1]
       distance = math.sqrt(math.pow((target_x-current_x),2)+math.pow((target_y-current_y),2))
       
       angle_values = bicycle_translation.getSFVec3f()
       angle = math.atan((target_y-angle_values[1])/(target_x-angle_values[0]))
            
       Xvalues.append(angle_values[0])
       Yvalues.append(angle_values[1])

       if distance<0.15:
           distance=0
           motor_front.setVelocity(distance*5)
           motor_shaft.setVelocity(distance*5)
           motor_steering.setVelocity(0)
           
           # x axis values
           x = [0,target_x]
            # corresponding y axis values
           y = [0,target_y]   
            # plotting the points 
           plt.plot(x, y, label = "Displacement")
           plt.plot(Xvalues, Yvalues, label = "Distance")
            # naming the x axis
           plt.xlabel('x - axis')
            # naming the y axis
           plt.ylabel('y - axis')  
            # giving a title to my graph
           plt.title('Graph')
           plt.legend()
            # function to show the plot
           plt.show()
           break
      
       if distance>9: #WEBOTS let velocity to be max 10
           motor_front.setVelocity(MAX_SPEED)
           motor_shaft.setVelocity(MAX_SPEED)
       else:
           motor_front.setVelocity(distance)
           motor_shaft.setVelocity(distance)
           
       if ps_value < 0.5 and angle > rotation_angle: # set steering wheel to right
           motor_steering.setVelocity(1)
       elif ps_value >-0.5 and angle < rotation_angle: # set steering wheel to left
           motor_steering.setVelocity(-1)
       else:
           motor_steering.setVelocity(0)