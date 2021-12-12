from flask import Flask, render_template, request
import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    # Fuel_Type_Diesel=0
    if request.method == 'POST':
        Area = int(request.form['Area'])

        Bed = int(request.form['Bedroom'])

        Maintenance_staff =request.form['maintenance']
        if(Maintenance_staff =='Yes'):
                Maintenance_staff = 1
        else:
            Maintenance_staff = 0

        Gym =request.form['gym']
        if(Gym == 'Yes'):
                Gym = 1
        else:
                Gym = 0

        Swimming_Pool =request.form['swimming_pool']
        if(Swimming_Pool =='Yes'):
                Swimming_Pool = 1
        else:
                Swimming_Pool = 0

        Landscape =request.form['landscape']
        if(Landscape =='Yes'):
                Landscape = 1
        else:
                Landscape = 0


        School =request.form['School']
        if(School =='Yes'):
                School = 1
        else:
                School = 0
        
        Parking =request.form['Parking']
        if(Parking =='Yes'):
                Parking = 1
        else:
                Parking = 0

        Hospital =request.form['Hospital']
        if(Hospital =='Yes'):
                Hospital = 1
        else:
                Hospital = 0

        gas_station =request.form['gas_station']
        if(gas_station =='Yes'):
                gas_station = 1
        else:
                gas_station = 0

        Lift =request.form['Lift']
        if(Lift =='Yes'):
                Lift = 1
        else:
                Lift = 0

        prediction=model.predict([[Area, Bed, Maintenance_staff, Gym, Swimming_Pool, Landscape, School, Parking, Hospital, gas_station, Lift]])
        output=round(prediction[0],2)
        if output<0:
            return render_template('index.html',Rs="Sorry, You might have entered some wrong values. Please enter the correct details again")
        else:
            return render_template('index.html',Rs="You Can Sell The Real Estate at Rs. {}".format(output))
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)
