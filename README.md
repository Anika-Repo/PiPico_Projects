Inventory Master
The Inventory Master is a robot built with a Raspberry Pi Pico, that counts boxes while it drives.

Features:
  Automatic Counting: A sensor on the right side detects and counts objects as the robot passes them.
  Obstacle Awareness: A front-facing sensor scans for obstacles.
  Safety Stop: If something blocks the robot's path, it stops moving and displays the final box count on an LCD screen.

Parts List
1 Raspberry Pi Pico
1 Motor Driver
2 Infrared Sensors
1 16x2 I2C LCD
2 18650 Batteries (3.7v)
2 BO Motors
1 Castor Wheel
10 F2F Jumper Wires

How It Works
  The robot starts driving forward using its two motors.
  The side IR sensor searches for items. Every time it senses one, the count goes up.
  The front IR sensor looks for a wall or a person.
  When the front sensor sees an obstacle, the Pico tells the motors to stop and shows the total count on the screen.
