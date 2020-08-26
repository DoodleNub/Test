import flask
from flask import jsonify,request
import ret_dat

app=flask.Flask('__name__')
app.config["DEBUG"]=True

@app.route('/api/v1/test',methods=['GET'])
def try_return():
    if 'id' in request.args:
        id=int(request.args['id'])
    else:
        print("ERROR : No id passed")
    data=ret_dat.test(id)
    return jsonify(data)

if __name__=='__main__':
    app.run()
