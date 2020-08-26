import flask
from flask import jsonify,request
import ret_dat

app=flask.Flask('__name__')
app.config["DEBUG"]=True

@app.route('/test',methods=['GET'])
def home():
    return(jsonify("THIS IS A TEST!"))
if __name__=='__main__':
    app.run()
