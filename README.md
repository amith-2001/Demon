# DeMonS
Reva Hackathon

![slide1](https://github.com/HarshithDR/DeMonS/blob/main/slide2.jpeg?raw=true)

DeMonS stands for Deforestation Monitoring System. The basic idea is to facilitate the detection of illegal cutting of trees.
Trees are so important for the global environment and the health of the species that live there, and they need our unconditional care and protection. Hence it is our duty to protect and conserve them.

![slide2](https://github.com/HarshithDR/DeMonS/blob/main/slide3.jpeg?raw=true)

![slide3](https://github.com/HarshithDR/DeMonS/blob/main/slide4.jpeg?raw=true)

In our proposal, we make use of nodes placed in a beehive structure. Each node has the capacity to sense audio within 200mtrs of radius. We make use of beehive architecture since it has the highest coverage to overlap ratio.
Each node is a pair of Raspberry Pi and Node MCU. Raspberry pi is incharge of computations and Node MCU is incharge of the communication.
10 seconds audio is recorded for fixed intervals of time and is reported to a master unit, which inturn pushes the data into the database.

![slide4](https://github.com/HarshithDR/DeMonS/blob/main/slide5.jpeg?raw=true)

![slide5](https://github.com/HarshithDR/DeMonS/blob/main/slide6.jpeg?raw=true)

Each of the raspberry pi will have the ability to sense the audio of wood cutting tools. This is enabled through ARtificial intelligence.
The audio recorded by the nodes will be converted to mel spectograms so that image processing algorithms can be applied on it.

Then, ultimately the web application will provide the user with the insights about the nodes and the suspicous activities detected by them.

Hardware:

![hardware](https://github.com/HarshithDR/DeMonS/blob/main/hardware.jpeg?raw=true)

User interface: 

![login page](https://github.com/HarshithDR/DeMonS/blob/main/webpage2.png?raw=true)
![status page](https://github.com/HarshithDR/DeMonS/blob/main/webpage1.png?raw=true)

model: 
![model training](https://github.com/HarshithDR/DeMonS/blob/main/modeltraining.jpeg?raw=true)
