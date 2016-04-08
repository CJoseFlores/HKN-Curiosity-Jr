# HKN CuriosityJr Team

# Note: This README is heavily outdated. The following is simply reference for the arm.
### Main Branch

### Objectives:

1. Move the arm in sync using:

  * Arm objects
	
  * Sensors
	
2. Create a "Default Position" 

  * This position will be used to calibrate the arm.
	
  * S1 and S2 will be used to tell the arm when to start/stop moving to return/exit the default position.
	
  * X and Y are distances that will be used to perform the above statement.
	  
  * The arm will return to the "Default Position" when powered on, and after picking up or dropping off the payload.
  
  * The Default Position is depicted below:

![alt tag][defaultpos]

[defaultpos]: http://i.imgur.com/JYRuONC.jpg

* After the rover finds the object with the Object-Tracking camera, the arm will turn and pickup the payload, and return to the default position.

  * Once it sees the payload, it will move motors 2 & 3 to get the arm close, and finally motor 5 to grab/release it, as depicted below:
	
	![alt tag](http://i.imgur.com/y6iTx2m.jpg)

* Once next to the drop-off area, the arm will drop the payload, and return to the default position.

------
Note: The default position and lunge depicted above and below are outdated. We are using the same concept, except we are mounting s2 under s3 (on the bottom of the claw section). These are currently being coded as defaultconfig2 and lunge2.
	
### Objective Progress:
* Motors move well individually, we are working on moving them in sync with the sensors

* Sensors are currently functional, but they give off strange distance readings. Currently working off those readings and will begin testing the arm movement in conjunction to it.


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
