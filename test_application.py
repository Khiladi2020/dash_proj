from main_app import app

def test_response_code():
	response = app.test_client().get("/get_data_current")
	assert response.status_code == 200

def test_valid_beer_cont():
	response = app.test_client().get("/get_data_current").get_json()
	beer_data = app.test_client().get("/get_data_beers").get_json()
	response_beer_id = set()
	actual_beer_id = set()
	for x in response: response_beer_id.add(x["beer_id"])
	for x in beer_data: actual_beer_id.add(x)

	assert actual_beer_id.issuperset(response_beer_id) == True

def test_valid_status():
	response = app.test_client().get("/get_data_current").get_json()
	beer_data = app.test_client().get("/get_data_beers").get_json()

	actual_safe = 0; actual_unsafe = 0
	curr_safe = 0; curr_unsafe = 0

	for x in response:
		#for ideal/actual status
		if x["status"] != "Alert!":
			if x["current_temp"] < beer_data[x["beer_id"]]["min_temp"] or x["current_temp"] > beer_data[x["beer_id"]]["max_temp"]:
				actual_unsafe+=1
			else:
				actual_safe+=1
		#for current status
		if x["status"] == "UnSafe": curr_unsafe+=1
		elif x["status"] == "Safe": curr_safe+=1

	print((actual_safe,actual_unsafe),(curr_safe,curr_unsafe))
	assert (actual_safe,actual_unsafe) == (curr_safe,curr_unsafe)

def test_all_endpoints():
	urls = ["/get_data_current","/get_data_containers","/get_data_beers","/"]
	total_ok_response = 0

	for url in urls: 
		res = app.test_client().get(url)
		if res.status_code == 200:
			total_ok_response+=1
	
	assert total_ok_response == len(urls)