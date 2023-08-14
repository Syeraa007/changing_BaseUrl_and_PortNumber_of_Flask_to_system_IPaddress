from flask import Flask,render_template

# Application instance
FAI = Flask(__name__)

# Creation of route for view
@FAI.route('/baseUrl') 

# creation of View functions
def baseUrl():
    return render_template('baseUrl.html',name='SYERAA',id='007')

# Running server
if __name__=='__main__':
    # FAI.run(debug=True)
    FAI.run(debug=True,host='192.168.1.21',port=5050)