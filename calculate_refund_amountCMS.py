# calculate the price + initiate refund from stripe payment

#takes in the CPID + coordinates of where the person gets off -> calls the carpool MS for the total coordinates

'''
get <start_lat>,<start_long>/<end_lat>,<end_long> from carpool MS by inputting MS

this for total distance of carpool 
@app.route("/api/v1/calculate_price_between_points/<start_lat>,<start_long>/<end_lat>,<end_long>", methods=['GET'])
def get_price_between_points(start_lat, start_long, end_lat, end_long):
    return a = calculate_distance(start_lat, start_long, end_lat, end_long)

this is travelled distance before refund
@app.route("/api/v1/calculate_price_between_points/<start_lat>,<start_long>/<end_lat_of_pass>,<end_long_of_pass>", methods=['GET'])
def get_price_between_points(start_lat, start_long, end_lat, end_long):
    return b = calculate_distance(start_lat, start_long, end_lat, end_long)

also need to get passenger_price from carpool MS 

refunded_price = (b/a)*passenger_price

return refunded_price


# SEPERATE MS - 
call the refund payments once in payments MS and give intent ID + amount which you get from here. 
'''



