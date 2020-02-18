# airgarage_coding_challenge

installation instructions: no special libraries need to be installed. Just clone the repository.

running instructions: the program should run as expected in the commandline as follows;

./parkbot airgarage-data.json [command] [argument]

if it does not run as expected, use:

chmod +x parkbot 

then try again.
If that fails, use:

python3 parkbot airgarage.json [command] [argument]


list of files:
- airgarage-data.json: json of all the parking lots
- lot.py: module - contains Lot class that holds data for each lot
- parkinglot.py: module - ParkingLot class that contains data structure which holds all instances of Lots as well as processes the data and returns output
- parkbot: the driver for the program and unix executable
- testing.py: contains unit tests for the main methods used

