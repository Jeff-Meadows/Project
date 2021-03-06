from flask import Flask, render_template, request, jsonify 
import pdb #python debugger
#pdb.set_trace()  #python debugger - pauses at this line.  type lat and it will show you, continue leave pause
import json
import combine_galleries_wineries as yelp
import pprint


app = Flask (__name__)
#pdb.set_trace
@app.route('/', methods=["GET"])
def home_page():
    address = request.args.get("address")
    if not address:   
        address = "1807 Telegraph Avenue"
        #pdb.set_trace()
    print "THIS IS THE ADDRESS! WOOHOO!", address
    return render_template("index.html", address=address)

@app.route('/get_nearby_businesses', methods=["GET"])
def get_nearby_points():
    latitude = float(request.args.get("lat"))
    print latitude 
    longitude = float(request.args.get("lng"))
    print longitude
    #points = jsonify(latitude=lat, longitude=lng)  
    yelp_call_results = yelp.yelp_api_calls(latitude, longitude)
    yelp_call_results_json = json.dumps(yelp_call_results)
    return yelp_call_results_json
    
    #return render_template("test.html", lat = latitude, lng = longitude) #orange = html

#access yelp_api_galleries
#insert lat lng params into function
  
   
@app.route('/js/mapping.js')
def mapping_js():
    return app.send_static_file('js/mapping.js')


if __name__ == "__main__":
    app.run(debug=True)
