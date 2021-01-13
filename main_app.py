from flask import Flask, render_template, Response, json, request
import random

app = Flask(__name__)

##-------------------------------------------------------------
# utility functions
##-------------------------------------------------------------

def get_data_beer():
	with open('data_beers.json') as f:
		data = json.load(f)

	return data

def get_data_cont():
	with open('data_containers.json') as f:
		data = json.load(f)

	return data

def get_random_cont_temp():
	data_cont = get_data_cont()
	data_beer = get_data_beer()

	for x in data_cont:
		rand_no = random.randint(3,9)
		x["current_temp"] = rand_no

		try:
			x["safe_range"] = str(data_beer[x["beer_id"]]["min_temp"]) + "-" + str(data_beer[x["beer_id"]]["max_temp"])

			if rand_no>= data_beer[x["beer_id"]]["min_temp"] and rand_no <= data_beer[x["beer_id"]]["max_temp"]:
				x["status"] = "Safe"
			else:
				x["status"] = "UnSafe"
		except KeyError as e:
			x["safe_range"] = "unknown"
			x["status"] = "Alert!"
			x["current_temp"] = "unknown"
			x["beer_type"] = "unknown"

	return data_cont

##-------------------------------------------------------------
# API functions
##-------------------------------------------------------------

@app.route("/get_data_current",methods=["GET"])
def fun_data_currents():
	data=get_random_cont_temp()

	resp = Response(
		response = json.dumps(data,sort_keys=False,indent=2),
		status = 200,
		mimetype = "application/json",
		headers = {
			'Access-Control-Allow-Origin' :'*'
		}
	)

	return resp

@app.route("/get_data_containers",methods=["GET"])
def fun_data_containers():
	data=get_data_cont()

	resp = Response(
		response = json.dumps(data,sort_keys=False,indent=2),
		status = 200,
		mimetype = "application/json",
		headers = {
			'Access-Control-Allow-Origin' :'*'
		}
	)

	return resp

@app.route("/get_data_beers",methods=["GET"])
def fun_data_beers():
	data=get_data_beer()

	resp = Response(
		response = json.dumps(data,sort_keys=False,indent=2),
		status = 200,
		mimetype = "application/json",
		headers = {
			'Access-Control-Allow-Origin' :'*'
		}
	)

	return resp

@app.route("/create_new_beer",methods=["POST"])
def fun_create_beer():
	data=get_data_beer()
	new_id = "b"+str(len(data)+1)
	new_data = {
		new_id:{
			"name": request.form['b_name'],
	        "min_temp":int(request.form['b_min_tmp']),
	        "max_temp":int(request.form['b_max_tmp'])
		}
	}
	data.update(new_data)
	with open("data_beers.json", 'w') as json_file:
		json_file.write(json.dumps(data,sort_keys=False,indent=4))

	resp = Response(
		response = "Success, Beer addeed.",
		status = 200
	)

	return resp

@app.route("/create_new_container",methods=["POST"])
def fun_create_cont():
	data=get_data_cont()
	new_id = len(data)+1
	new_data = {
		"id" : new_id,
		"name" : request.form['c_name'],
        "beer_type" : request.form['b_type'],
        "beer_id" : request.form['b_id']
	}
	data.append(new_data)
	with open("data_containers.json", 'w') as json_file:
		json_file.write(json.dumps(data,sort_keys=False,indent=4))

	resp = Response(
		response = "Success, Container addeed.",
		status = 200
	)

	return resp

##-------------------------------------------------------------
# Main routing functions
##-------------------------------------------------------------

@app.route('/', methods=['GET'])
def home():
	all_data = get_data_cont()
	beer_data = get_data_beer()
	return render_template("index.html", result = all_data, all_beer = beer_data, len_result = len(all_data))

##-------------------------------------------------------------
# To run the File 
##-------------------------------------------------------------

if __name__ == "__main__":
	app.run(debug=True)