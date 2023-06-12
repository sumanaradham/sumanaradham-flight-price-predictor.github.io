from flask import Flask, request, render_template
from flask_cors import cross_origin
import sklearn
import pickle
import pandas as pd

app = Flask(__name__)
model = pickle.load(open("flight_rf_pred1.pkl", "rb"))



@app.route("/")
@cross_origin()
def home():
    return render_template("FE.html")




@app.route("/predict", methods = ["GET", "POST"])
# @cross_origin()
def predict():
    if request.method == "POST":

        # Date_of_Journey
        date_dep = request.form["Departure Time"]
        Date_of_Journey = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").day)
        Month_of_Journey = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").month)

        # Departure
        Dep_hour = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").hour)
        Dep_min = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").minute)

        # Arrival
        date_arr = request.form["Arrival Time"]
        Arr_hour = int(pd.to_datetime(date_arr, format ="%Y-%m-%dT%H:%M").hour)
        Arr_min = int(pd.to_datetime(date_arr, format ="%Y-%m-%dT%H:%M").minute)
        #Arr_min = request.form["Arrival_min"]


        # Total Stops
        No_of_Stops = int(request.form["No.of Stops"])


        # Airline
        # AIR ASIA = 0 (not in column)
        airline=request.form['Airline']
        if(airline=='Jet Airways'):
            Airline_Jet_Airways = 1
            Airline_Air_Asia=0
            Airline_IndiGo = 0
            Airline_Air_India = 0
            Airline_Multiple_carriers = 0
            Airline_SpiceJet = 0
            Airline_Vistara = 0
            Airline_GoAir = 0
            Airline_Multiple_carriers_Premium_economy = 0
            Airline_Jet_Airways_Business = 0
            Airline_Vistara_Premium_economy = 0
            Airline_Trujet = 0 

        elif (airline=='IndiGo'):
            Airline_Jet_Airways = 0
            Airline_Air_Asia=0
            Airline_IndiGo = 1
            Airline_Air_India = 0
            Airline_Multiple_carriers = 0
            Airline_SpiceJet = 0
            Airline_Vistara = 0
            Airline_GoAir = 0
            Airline_Multiple_carriers_Premium_economy = 0
            Airline_Jet_Airways_Business = 0
            Airline_Vistara_Premium_economy = 0
            Airline_Trujet = 0 

        elif (airline=='Air India'):
            Airline_Jet_Airways = 0
            Airline_Air_Asia=0
            Airline_IndiGo = 0
            Airline_Air_India = 1
            Airline_Multiple_carriers = 0
            Airline_SpiceJet = 0
            Airline_Vistara = 0
            Airline_GoAir = 0
            Airline_Multiple_carriers_Premium_economy = 0
            Airline_Jet_Airways_Business = 0
            Airline_Vistara_Premium_economy = 0
            Airline_Trujet = 0 
            
        elif (airline=='Multiple carriers'):
            Airline_Jet_Airways = 0
            Airline_Air_Asia=0
            Airline_IndiGo = 0
            Airline_Air_India = 0
            Airline_Multiple_carriers = 1
            Airline_SpiceJet = 0
            Airline_Vistara = 0
            Airline_GoAir = 0
            Airline_Multiple_carriers_Premium_economy = 0
            Airline_Jet_Airways_Business = 0
            Airline_Vistara_Premium_economy = 0
            Airline_Trujet = 0 
            
        elif (airline=='SpiceJet'):
            Airline_Jet_Airways = 0
            Airline_Air_Asia=0
            Airline_IndiGo = 0
            Airline_Air_India = 0
            Airline_Multiple_carriers = 0
            Airline_SpiceJet = 1
            Airline_Vistara = 0
            Airline_GoAir = 0
            Airline_Multiple_carriers_Premium_economy = 0
            Airline_Jet_Airways_Business = 0
            Airline_Vistara_Premium_economy = 0
            Airline_Trujet = 0 
            
        elif (airline=='Vistara'):
            Airline_Jet_Airways = 0
            Airline_Air_Asia=0
            Airline_IndiGo = 0
            Airline_Air_India = 0
            Airline_Multiple_carriers = 0
            Airline_SpiceJet = 0
            Airline_Vistara = 1
            Airline_GoAir = 0
            Airline_Multiple_carriers_Premium_economy = 0
            Airline_Jet_Airways_Business = 0
            Airline_Vistara_Premium_economy = 0
            Airline_Trujet = 0 

        elif (airline=='GoAir'):
            Airline_Jet_Airways = 0
            Airline_Air_Asia=0
            Airline_IndiGo = 0
            Airline_Air_India = 0
            Airline_Multiple_carriers = 0
            Airline_SpiceJet = 0
            Airline_Vistara = 0
            Airline_GoAir = 1
            Airline_Multiple_carriers_Premium_economy = 0
            Airline_Jet_Airways_Business = 0
            Airline_Vistara_Premium_economy = 0
            Airline_Trujet = 0 

        elif (airline=='Multiple carriers Premium economy'):
            Airline_Jet_Airways = 0
            Airline_Air_Asia=0
            Airline_IndiGo = 0
            Airline_Air_India = 0
            Airline_Multiple_carriers = 0
            Airline_SpiceJet = 0
            Airline_Vistara = 0
            Airline_GoAir = 0
            Airline_Multiple_carriers_Premium_economy = 1
            Airline_Jet_Airways_Business = 0
            Airline_Vistara_Premium_economy = 0
            Airline_Trujet = 0 

        elif (airline=='Jet Airways Business'):
            Airline_Jet_Airways = 0
            Airline_Air_Asia=0
            Airline_IndiGo = 0
            Airline_Air_India = 0
            Airline_Multiple_carriers = 0
            Airline_SpiceJet = 0
            Airline_Vistara = 0
            Airline_GoAir = 0
            Airline_Multiple_carriers_Premium_economy = 0
            Airline_Jet_Airways_Business = 1
            Airline_Vistara_Premium_economy = 0
            Airline_Trujet = 0 

        elif (airline=='Vistara Premium economy'):
            Airline_Jet_Airways = 0
            Airline_Air_Asia=0
            Airline_IndiGo = 0
            Airline_Air_India = 0
            Airline_Multiple_carriers = 0
            Airline_SpiceJet = 0
            Airline_Vistara = 0
            Airline_GoAir = 0
            Airline_Multiple_carriers_Premium_economy = 1
            Airline_Jet_Airways_Business = 0
            Airline_Vistara_Premium_economy = 0
            Airline_Trujet = 0 
            
        elif (airline=='Trujet'):
            Airline_Jet_Airways = 0
            Airline_Air_Asia=0
            Airline_IndiGo = 0
            Airline_Air_India = 0
            Airline_Multiple_carriers = 0
            Airline_SpiceJet = 0
            Airline_Vistara = 0
            Airline_GoAir = 0
            Airline_Multiple_carriers_Premium_economy = 0
            Airline_Jet_Airways_Business = 0
            Airline_Vistara_Premium_economy = 0
            Airline_Trujet = 1

        elif (airline=='Air_Asia'):
            Airline_Jet_Airways = 0
            Airline_Air_Asia=1
            Airline_IndiGo = 0
            Airline_Air_India = 0
            Airline_Multiple_carriers = 0
            Airline_SpiceJet = 0
            Airline_Vistara = 0
            Airline_GoAir = 0
            Airline_Multiple_carriers_Premium_economy = 0
            Airline_Jet_Airways_Business = 0
            Airline_Vistara_Premium_economy = 0
            Airline_Trujet = 0

        else:
            Airline_Jet_Airways = 0
            Airline_Air_Asia=0
            Airline_IndiGo = 0
            Airline_Air_India = 0
            Airline_Multiple_carriers = 0
            Airline_SpiceJet = 0
            Airline_Vistara = 0
            Airline_GoAir = 0
            Airline_Multiple_carriers_Premium_economy = 0
            Airline_Jet_Airways_Business = 0
            Airline_Vistara_Premium_economy = 0
            Airline_Trujet = 0


        # Source
        # Banglore = 0 (not in column)
        Source = request.form["Source"]
        if (Source == 'Delhi'):
            Source_Delhi = 1
            Source_Kolkata = 0
            Source_Mumbai = 0
            Source_Chennai = 0
            Source_Banglore=0

        elif (Source == 'Kolkata'):
            Source_Delhi = 0
            Source_Kolkata = 1
            Source_Mumbai = 0
            Source_Chennai = 0
            Source_Banglore=0
        elif (Source == 'Mumbai'):
            Source_Delhi = 0
            Source_Kolkata = 0
            Source_Mumbai = 1
            Source_Chennai = 0
            Source_Banglore=0

        elif (Source == 'Chennai'):
            Source_Delhi = 0
            Source_Kolkata = 0
            Source_Mumbai = 0
            Source_Chennai = 1
            Source_Banglore=0

        elif (Source == 'Banglore'):
            Source_Delhi = 0
            Source_Kolkata = 0
            Source_Mumbai = 0
            Source_Chennai = 1
            Source_Banglore=0

        else:
            Source_Delhi = 0
            Source_Kolkata = 0
            Source_Mumbai = 0
            Source_Chennai = 0
            Source_Banglore=0

        # print(s_Delhi,
        #     s_Kolkata,
        #     s_Mumbai,
        #     s_Chennai)

        # Destination
        # Banglore = 0 (not in column)
        Destination = request.form["Destination"]
        if (Destination == 'Cochin'):
            Destination_Cochin = 1
            Destination_Delhi = 0
            Destination_New_Delhi = 0
            Destination_Hyderabad = 0
            Destination_Kolkata = 0
            Destination_Banglore=0
        
        elif (Destination == 'Delhi'):
            Destination_Cochin = 0
            Destination_Delhi = 1
            Destination_New_Delhi = 0
            Destination_Hyderabad = 0
            Destination_Kolkata = 0
            Destination_Banglore=0
        elif (Destination == 'Banglore'):
            Destination_Cochin = 0
            Destination_Delhi = 0
            Destination_New_Delhi = 0
            Destination_Hyderabad = 0
            Destination_Kolkata = 0
            Destination_Banglore=1

        elif (Destination == 'New Delhi'):
            Destination_Cochin = 0
            Destination_Delhi = 0
            Destination_New_Delhi = 1
            Destination_Hyderabad = 0
            Destination_Kolkata = 0
            Destination_Banglore=0

        elif (Destination == 'Hyderabad'):
            Destination_Cochin = 0
            Destination_Delhi = 0
            Destination_New_Delhi = 0
            Destination_Hyderabad = 1
            Destination_Kolkata = 0
            Destination_Banglore=0

        elif (Destination == 'Kolkata'):
            Destination_Cochin = 0
            Destination_Delhi = 0
            Destination_New_Delhi = 0
            Destination_Hyderabad = 0
            Destination_Kolkata = 1
            Destination_Banglore=0

        else:
            Destination_Cochin = 0
            Destination_Delhi = 0
            Destination_New_Delhi = 0
            Destination_Hyderabad = 0
            Destination_Kolkata = 0
            Destination_Banglore=0
  
        """Time_of_Arrival = request.form["Time of Arrival"]
        if (Time_of_Arrival == 'Afternoon'):
            Time_of_Arrival_Aft = 1
            Time_of_Arrival_mrg = 0
            Time_of_Arrival_n8 = 0
        
        elif (Time_of_Arrival == 'Morning'):
            Time_of_Arrival_Aft = 0
            Time_of_Arrival_mrg = 1
            Time_of_Arrival_n8 = 0

        elif (Time_of_Arrival == 'Night'):
            Time_of_Arrival_Aft = 0
            Time_of_Arrival_mrg = 0
            Time_of_Arrival_n8 = 1
        
        else:
            Time_of_Arrival_Aft = 0
            Time_of_Arrival_mrg = 0
            Time_of_Arrival_n8 = 0
        
        Type_of_flight=request.form=["Type of Flight"] """



        
        prediction=model.predict([[
            No_of_Stops,
            Date_of_Journey,
            Month_of_Journey,
            Arr_min,
            Arr_hour,
            Dep_hour, 
            Dep_min, 
            Airline_Air_Asia, 
            Airline_Air_India, 
            Airline_GoAir,
            Airline_IndiGo, 
            Airline_Jet_Airways,
            Airline_Jet_Airways_Business,
            Airline_Multiple_carriers,
            Airline_Multiple_carriers_Premium_economy,
            Airline_SpiceJet,
            Airline_Trujet, 
            Airline_Vistara,
            Airline_Vistara_Premium_economy,
            Source_Banglore,
            Source_Chennai, 
            Source_Delhi, 
            Source_Kolkata,
            Source_Mumbai,
            Destination_Banglore,
            Destination_Cochin,
            Destination_Delhi,
            Destination_Hyderabad,
            Destination_Kolkata,
            Destination_New_Delhi
            
        ]])
        output = {}
        output['predicted_result'] = round(prediction[0],2)
        output['source'] = Source
        output['destination'] = Destination
        output['stops'] = No_of_Stops


        return render_template('result.html', value=output)





        # output=round(prediction[0],2)
        # return render_template('result.html', value=output)
       # return render_template('FE.html',prediction_text="Your Flight price is Rs. {}".format(output))
@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r



if __name__ == "__main__":
    app.run(debug=True)