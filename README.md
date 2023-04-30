# Network-v2v-Comunication

What is V2V?

Vehicle-To-Vehicle (V2V) is an automobile technology designed to allow automobiles to “talk” to each other i.e., to communicate with each other.
 
 
Vehicle-to-vehicle (V2V) communication’s ability to wirelessly exchange information
about the speed and position of surrounding vehicles shows great promise in help-
ing to avoid crashes, ease traffic congestion, and improve the environment. But the
greatest benefits can only be achieved when all vehicles can communicate with each
other thanks to appropriate software (or safety applications). Vehicle-to-vehicle
(V2V) communication is an automobile technology designed for dedicated short-
range communication (DSRC) to allow vehicles to communicate with one another.
Scope of V2V Connection

In my project i implemented a program by which every vehicle which are on the
same server can interact with each other.
Therefore, here i created a server and client. Where i developed a server for a
particular road and a client as a vehicle. By that, if any vehicle will enter on the road
having a server, vehicle will connect to that server and can interact with all other
vehicles and can get an information about that road. Like, traffic, road accident, police
activities etc.

![image](https://user-images.githubusercontent.com/104581680/235346309-8dc9ec5f-a706-42c9-af8b-7250995f80e0.jpeg)

For the first, to create a socket of a server we created a “build_socket()” function. In
which we mentioned a host as a localhost and a port number as 6065 and by listen()
function we are getting request from the vehicle.

![image](https://user-images.githubusercontent.com/104581680/235346334-5a7b352b-9231-41e4-95de-3d9ff240c7ad.jpeg)


By using the above function, we are accepting the request which we got in
build_socket() function and will store the IP Address of client in variable named “car”.
After in the “name” variable we are storing the name of the vehicle which we received
from the vehicle as a particular buffer size. Moreover, we are sending a message that
the vehicle joined the road to other vehicles.

With the thread function we are managing different vehicles and their messages at a
same time using multi_cars() function.

![image](https://user-images.githubusercontent.com/104581680/235346341-0e2c4cee-3cb2-4483-bf99-ce27340d5dde.jpeg)


In this function, we are receiving the message from vehicle of a particular buffer size
and sending to all other vehicles. We have put try and except part to avoid any error.


![image](https://user-images.githubusercontent.com/104581680/235346347-af1fb6e8-ecb7-4180-8b3c-8a00e495cac2.jpeg)


This is the same function of building a socket we have in server but, here we have the
connect() function to send the request of connection to the server instead of having
bind() function we have in server. And we are also sending the name and the date &
time information to the server.

![image](https://user-images.githubusercontent.com/104581680/235346373-0b139ecb-566a-4ef4-8144-5668ee39c9a4.jpeg)

with this function vehicle can send the messages to the server and interact with other
vehicles.

![image](https://user-images.githubusercontent.com/104581680/235346381-2128d2cb-a0b5-4c43-84e9-d97b2c0f66b0.jpeg)

This function is receiving the data from the server and print that to the user. If anything will go wrong then it will give error to avoid that error we put except part in this function.

![image](https://user-images.githubusercontent.com/104581680/235346341-0e2c4cee-3cb2-4483-bf99-ce27340d5dde.jpeg)

run_forever() is the function by which vehicle can manage multiple messages at a
same time by using thread function.

