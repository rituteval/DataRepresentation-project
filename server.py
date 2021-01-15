from flask import Flask, url_for, request, redirect, abort, jsonify
import travelagencyDAO 
app = Flask(__name__, static_url_path='', static_folder='staticpages')

@app.route('/')
def index():
    return "hello"
#get all

@app.route('/travelagency')
def getAll():
    return jsonify(travelagencyDAO.getAll())
# find By id

@app.route('/travelagency/<int:ID>')
def findById(ID):
    
    return jsonify({})

# create
# curl -X POST -d "{\"fullname\":\"test\", \"firmname\":\"some guy\", \"email\":\"abcd@gmail.com"}" http://127.0.0.1:5000/travelagency
@app.route('/travelagency', methods=['POST'])
def create():

    if not request.json:
        abort(400)
    
    travelagency = {
        "ID": request.json["ID"],
        "fullname": request.json["fullname"],
        "firmname": request.json["firmname"],
        "email": request.json["emal"]
    }
    
    return jsonify(travelagencyDAO(travelagency))


    return "served by Create "

#update
# curl -X PUT -d "{\"ID\":\"new ID\", \"email\":\new email"}" -H "content-type:application/json" http://127.0.0.1:5000/travelagency/1
@app.route('/travelagency/<int:ID>', methods=['PUT'])
def update(ID):
    foundTravelagency=travelagencyDAO.findById(ID)
    print(foundTravelagency)
    if foundTravelagency == {}:
        return jsonify({}), 404
    currentTravelagency = foundTravelagency
    if 'fullname' in request.json:
        currentTravelagency['fullname'] = request.json['fullname']
    if 'firmname' in request.json:
        currentTravelagency['fimname'] = request.json['firmname']
    if 'email' in request.json:
        currentTravelagency['email'] = request.json['email']
    travelagencyDAO.update(currentTravelagency)

    return jsonify(currentTravelagency)


#delete
# curl -X DELETE http://127.0.0.1:5000/travelagency/1
@app.route('/travelagencies/<int:ID>', methods=['DELETE'])
def delete(ID):
    travelagencyDAO.delete(ID)
    
    return jsonify({"done": True})


if __name__ == "__main__" :
    app.run(debug=True)