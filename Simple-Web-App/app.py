from flask import Flask, render_template,request,redirect, make_response,jsonify
import csv, json


# source venv/bin/activate is used in terminal to activiate virtual enviromenet for flask app

# creates the application object
app = Flask(__name__)


@app.route('/') # this is used for mapping a specific url to the function
def home():
    return render_template("homepage.html") # generating output on this speicfic html file onto local host in browser


@app.route('/formtest') 
def form(): # this is the output html file for the form test
    return render_template('formtest.html')
 
@app.route('/verify', methods = ['POST', 'GET']) # uses post and get methods
def verify():
    if request.method == 'POST': # if the request is post then 
        name = request.form['Name'] # it gets the name from the form
        if name == '': # if the name is empty 
            name = 'Stranger' # puts it as default to Stranger
      
    return redirect(f"/user/{name}")
 
@app.route('/user/<name>')
def user(name): # this is used in the verify function once the name variable has been assigned a string
    if name == 'Stranger':
        return f"Hello {name}"
    else:
        return f"Your name is {name}"
 
@app.route('/allegiances')
def allegiances():

    data = []
    with open('allegiance.csv') as f: # opens csv file
        for row in csv.DictReader(f): # reading data
            data.append(row) # appending data to data list
    json_data = json.dumps(data) # used for converting python object into json string
    return json_data # returning data s a json file
    
@app.route('/allegiancedashboard')
def api():
    return render_template('api_call.html') # prinitng this data out in a table in the /allegiancedashboard file

if __name__ == '__main__':
    app.run(debug=True) # this is used so that we can see our changes updated immediately in the browser
