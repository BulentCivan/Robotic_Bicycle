# Robotic_Bicycle
1. Introduction
In this project, a 3-wheeled bicycle robot has been designed. The robot moves to the target position by using wheel sensors and steering wheel. 

2. Implementation
 







				 	










 











The screenshot above shows the design of the bicycle robot.
Front, back and steering wheels have their own motors as front-motor, shaft-motor, and steering-motor. The front-motor and shaft-motor allow moving forward of the robot, by giving speed to the wheels. By giving speed to the steering-motor, the front wheel is rotated to the target point. The range of the rotation angle of the steering wheel is limited with +0.5/-0.5 radian, so the robot can not go out of the target point. As the robot approaches the target point the speed of the motors decreases proportionally. When the robot reaches the target point, the speeds of the all motors are set to 0, hereby the robot has been stopped.
⦁	The target point can be changed from node DEF TARGET Robot>translation
.




Code Explanation
Firstly, we add necessary libraries as matplotlib, math, Supervisor, robot and sys. Then we create global variables like timestep, max speed and wheel radius.
In main we start with define robot and target as supervisor. Cube variable is our target and we get translation points to calculate target’s position. 
We define devices on world one by one to get information.
We add position sensor to get how many angle our steering wheel turned as ps_front1.
Then we create two lists to store bicycle’s x and y coordinates.
In our main loop, we start with getting target’s coordinates and bicycle’s rotation from world information. Getting target’s position in while loop, ensure us to steer robot to target even it is moving. Then we equalize our calculated angle and rotation variable by adding or subtracting pi on rotation angle. Because world cartesian system and our calculations were not matching. 
We are getting currentX and currentY variables from translation to calculate robot’s current position. So, we know distance from target. In same way we calculate angle between bicycle and target. Then we add current position values to lists that we created before.
Then we add if statement to stop robot close position to target. After robot stops we draw our graphics.
Our velocity is related with distance to target. If distance is bigger than 10 webots gives error so we limit our speed to our global variable max_speed. 
In last if statements we limit steering because we want to prevent full spin of steering wheel. Our steering can turn right or left between 0.5 radian and -0.5. 
To turn target, we compare target’s angle and bicycle’s rotation angle. If target’s angle is bigger than rotation angle, we set steering velocity to 1. If target’s angle is smaller than rotation angle, we set steering velocity to -1. Else we set steering velocity to 0 so bicycle can go straight.

3. Simulation
When the robot arrives at the target point, a displacement/distance graph is shown. The graphs below show the displacement of the robot to the target point.
→ When the robot is at (0,0) and the target is at (-5,-5); 
  









→ At the beginning the robot is at (0,0) and the target is at (5,5), after a while the target position is changed to (5,-5);
 







4. Conclusion
	The desired robot model and robot movement was designed with teamwork. In this project we learnt how to design robot and move it with physic engine. It brings us to ability of work as a team with people from different disciplines.

5. References
1- Robotics, Vision and Control Fundamental Algorithms in MATLAB by Peter Corke. 
2- How to design a 2 wheel differential drive robot in Webots? // Webots tutorial 2 // Kajal Gada
3- Webots Tutorial 4: using encoders to compute robot position (Odometry) // Position Sensor in Webots
