# HKN CuriosityJr Team

###### Additional information and diagrams will be added later.

### Objectives:

1. Spin the Rover until it finds the object in frame.

  * The mounted Microsoft camera will draw a circle around the payload, colored FIU Blue when it finds the object.

2. Once it finds the object (colored FIU Blue), center the rover and move forward.

  * The camera compares the x-coordinate of the center of the object's circle with the center of the camera frame. This allows the rover to move in the appropriate direction until both x-coordinates are equiavlent.
  
  * If the rover overshoots the position, the rover then slightly move in the other direction until it matches the exact value.

3. As the rover moves forward, if it becomes off-center, recenter the rover as it moves. Once the rover is close enough to the object, have the rover stop.

4. Have the rover pick up the object, and search for the payload ramp (ORANGE).
  
  * The Pi does not have PWM pins, so the servos do not function optimially.
  
  * As a remedy, we used an Arduino UNO to drive the servos. 
  
  * The Rasberry Pi communicates to the Arduino via Serial communication. The Pi checks the conditions necessary to move the arm, and then sends a single character to the Arduino. The Arduino reads the character and determines how it should move the arm.
  
  * Sending the character 'l' for example, will tell the Ardunio to move and grab the payload.

5. Once the payload ramp is in the rover's frame, have the rover center itself and move towards it.

6. Have the rover continually move along the ramp until it sees the payload bay (GREEN)

7. Have the rover approach the payload bay, and drop the payload.

8. Have the rover reverse and follow the center of the payload ramp until it reaches the bottom. 

9. Have the rover stop at the bottom.

### Materials needed:

  * [SHARP IR distance sensor](https://www.adafruit.com/products/164)

  * [MCP3008 with SPI interface](https://www.adafruit.com/products/856) 
	This product will be used to convert the analogue readings of the sensor to digital
	
### Other Information/Datasheets:

* Rasberry pi 2 model B pinouts:
![alt tag](http://www.jameco.com/Jameco/workshop/circuitnotes/raspberry_pi_circuit_note_fig2a.jpg)

* H-Bridge Pinouts:
![alt tag](http://api.ning.com/files/2JurkTHbQdyEJc0Us*C9I5BgklPg596Okj8IKIsIa8WQR3T3KTnIIyLYDn9llE4Hao3cvc2vNy2S8ytKUmseZB*S5uMsuuwT/l293dpin.jpeg)

* MCP3008 Pinouts:

![alt tag](http://i.imgur.com/5t3wZug.png)
