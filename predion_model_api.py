from  flask import Flask, render_template,request
import pickle


app = Flask (__name__)
filre = open('flight_rf.pkl','rb')
model = pickle.load(filre)
#result = model.predict([[1,20,1,2,20,2,20,2,0,0,0,0,0,1,0,1,0,1,0,0,0,0,1,0,0,0,1,1,0]])
dep_file = open('deep.pkl','rb')
#model1= pickle.load(dep_file)
#result1= model1.predict([1,20,1,2,20,2,20,2,0,0,0,0,0,1,0,1,0,1,0,0,0,0,1,0,0,0,1,1,0])
@app.route('/')
def home():
    return render_template("index.html")

@app.route('/perdict' , methods=['POST'])
def pred():
    soruce = request.form.get('src')
    destination= request.form.get('den')
    date = request.form.get('date_flight')
    departure_hour=int(request.form.get('dep_hour'))
    departure_min = int(request.form.get('dep_min'))
    arrival_hour = int(request.form.get('arrival_hour'))
    arrival_min = int(request.form.get('arrival_min'))
    airline = request.form.get('airline')
    number_of_stops= int(request.form.get('no_stops'))
    duration_hour = int(request.form.get('duration_hour'))
    duration_min = int(request.form.get('duration_min'))
    ''''Total_Stops', 'joureny of Day', 'joureny of month',
       'dep_hour', 'dep_min', 'Arrival_hour', 'Arrival_min', 'Duration_hours',
       'Duration_min', 'Destination_Cochin', 'Destination_Delhi',
       'Destination_Hyderabad', 'Destination_Kolkata', 'Destination_New Delhi',
       'Airline_Air India', 'Airline_GoAir', 'Airline_IndiGo',
       'Airline_Jet Airways', 'Airline_Jet Airways Business',
       'Airline_Multiple carriers',
       'Airline_Multiple carriers Premium economy', 'Airline_SpiceJet',
       'Airline_Trujet', 'Airline_Vistara', 'Airline_Vistara Premium economy',
       'Source_Chennai', 'Source_Delhi', 'Source_Kolkata', 'Source_Mumbai'''''
    date_joureny = date.split('-')
    day_of_joureny = date_joureny[2]
    month_of_joureny = date_joureny[1]
    _destination = {
        'COC':0,'DEl':0,'HYD':0,
        'KOL':0, 'NDEL':0
    }
    list_destination=['COC','DEL','HYD','KOL','NDEL']
    if destination in list_destination:
        _destination[destination] = 1

    _source = {
        'CHE':0, 'DEL':0,'KOL':0,'MUM':0
    }
    list_source =['CHE','DEL','KOL','MUM']
    if soruce in list_source:
        _source[soruce] = 1

    _airline ={
        'A_A_I':0,'A_G':0,'A_J_A':0,'A_J_A_P':0,'A_M_C':0,'A_M_C_E':0,'A_S':0,'A_I':0,'A_V':0,'A_V_P_E':0,'A_T':0
    }
    list_airline =['A_A_I','A_G','A_J_A','A_J_A_P','A_M_C','A_M_C_E','A_S','A_I','A_V','A_V_P_E','A_T']
    if airline in list_airline:
        _airline[airline]=1
    result = model.predict([[number_of_stops,day_of_joureny,month_of_joureny,departure_hour,departure_min,arrival_hour,arrival_min,duration_hour,duration_min,_destination['COC'],_destination['DEl']
    , _destination['HYD'],_destination['KOL'],_destination['NDEL'],_airline['A_A_I'],_airline['A_G'],_airline['A_I'],_airline['A_J_A'],_airline['A_J_A_P'],_airline['A_M_C'],_airline['A_M_C_E'],
    _airline['A_S'],_airline['A_S'],_airline['A_V'],_airline['A_V_P_E'],_source['CHE'],_source['DEL'],_source['KOL'],_source['MUM']]])
    return render_template('predict.html',res=result)
    

if __name__ == "__main__":
    app.run(debug=True)