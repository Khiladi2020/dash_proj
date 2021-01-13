## Instructions to run the code
Note: all commands must be executed in terminal in projects directory

1) Latest version of python3 is required 
2) Install all required packages (Flask and pytest) by below commands
	->	pip install Flask
	->	pip install pytest
3) Type below Commands to run the Flask server
	->	python main_app.py

	Note: If above commands does not works , then try below command
	->	python3 main_app.py

4) After running the Server copy the address of server from terminal to browser to open the website
5) After do above all steps if website opens up means everything is working fine 

## Steps to run all tests

1) Type below command in terminal
	-> pytest
2) If everything worked fine results of all test will be printed on terminal

3) **Note:** 
	- flask server must be running before testing
	- all tests are present in "test_application.py" file.



## Assumptions Made

1) One Container Only Contains one type of beer
	Reason - Each Beer has a specific requirement of temperature to be maintained. So it will be
	 difficult to maintain temperature if different type of beers were placed in one container

2) Realtime Data about current temperature of container will be provided through a API to the website
	Reason - Data sharing through API between different applications is standard

## Features 
1) **Responsive User Interface**
	- website interface will adapt itself according to screen size

2) **Auto Update of Container Status**
	- No need to refresh page each time to see new update

3) **Extensible, New Beers and Containers can be easily added**
	- Option to add new beer and container is provided in dashboard

4) **Single Page Application**
	- No server-side roundtrips
	- Everything on a single Page that a user needs

5) **Container Stats Sidebar**
	- Shows information about number of safe/unsafe containers

6) **Good User Experience**
	- Used Animations for hover on containers and sidebar stats.
	- Loading animations
	- Popup alerts on adding new data

7) **Efficieny and Integration**
	- by using API
	- seperating UI and backend logic



## Core Logic 

### Data Source

- As there is no real source for getting current temperature from container's temperature sensor so temeperature data 
	is generated randomly using a function at backend
- API(Application Programming Interface) is used for data exchange between client side and server side
- API concept is more practical as in real life if there were sensors to measure temperature then they must have uploaded 
	collected data on cloud , and API can be used to fetch the data from cloud and server to client website. 


### Data Of Beer Types and Containers (Easily Extensible)

- All data related to beers is stored in "data_beers.json"
- All data related to containers is stored in "data_containers.json"
- **Note:** 
	storing of data in seperate files makes solution extensible as if one needs to enter more 
	beer type or containers that can be easily done by adding that data to the files and new data
	will be reflected in website after refreshing. 


### Main DashBoard
- DashBoard is made using web technologies and can be viewed on browser
- Shows All Containers available and their current temperature along with beer type and current status
- ** Data Refresh: **
	- Data is Refreshed every 5 seconds
	- updated on dashboard without any full page reload
	- Manual refresh button is also provided

- **Container Color Indication: **
	- Red    -> Container in Unsafe Temperature
	- Blue   -> Container in Safe Temperature
	- Yellow -> Alert! Misconfiguraion of data

- **Statistics Sidebar Indication: **
	- Blue   -> No. of Safe Containers
	- Green  -> No. of UnSafe Containers
	- Yellow -> Total No. of Containers

- **Add Container: **
	- used to create new container with specific beer type
	- updates Data file by adding new entry
	- input fields 
		- Container name
		- Beer Type

- **Add Beer: **
	- used to create new beer type
	- updates Data file by adding new entry
	- input fields 
		- Beer name
		- min. temperature
		- max. temperature

## Possible Improvements
- More Interactive and Aesthetic user Interface
- Some Alert System like SMS or email.
- Buzzer warning system.
- Using IOT devices to enable realtime temerature check.
- Add capability to show user guide to fix Unsafe containers.


