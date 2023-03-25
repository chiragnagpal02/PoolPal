# call fuel api, get the distance between the 2 pairs of coordinates and caluculate the base price for the 
# journey. Return the base price. 






@app.route('/get_base_price/<float:start_lat>,<float:start_lng>/', methods=['GET'])