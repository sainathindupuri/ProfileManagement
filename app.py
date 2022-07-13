from locale import currency
from flask import Flask, render_template
 
# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__, template_folder="templates")
import pyodbc
server = 'adbsai.database.windows.net'
database = 'adb'
username = 'sainath'
password = 'Shiro@2018' 
driver= '{ODBC Driver 17 for SQL Server}'


connection = pyodbc.connect('DRIVER= '+ driver + '; SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)


#connection = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server}';'Server=tcp:adbsai.database.windows.net,1433';'Database=adb';'Uid=adb';'Pwd=Shiro@2018';'Encrypt=yes';'TrustServerCertificate=no';'Connection Timeout=30')



# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def landingRoute():
    return render_template("landing.html")
 

@app.route('/ShowAllRecords')
def showAllRecords():
    cursor = connection.cursor()
    cursor.execute("Select * from people")
    data = cursor.fetchall()
    
    return render_template('ShowAllRecords.html',data=data)
# main driver function
if __name__ == '__main__':
 
    # run() method of Flask class runs the application
    # on the local development server.
    app.run()


