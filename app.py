from flask import Flask, jsonify, request
from flask_socketio import SocketIO
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


users = [
 	{
 			'id':2,
 			'name':'Anne',
 			'age':23


 	}, 
 	{	
 			'id':1,
 			'name': 'Cathy',
 			'age':44



 	},
 	{
 			'id':3,
 			'name': 'Amanda',
 			'age':21



 	},



 ]

@socketio.on('msg')
def handleMsg(data):
	socketio.emit('push', data, broadcast = True, include_self=False)

@app.route('/users')
def getusers():
	return jsonify(users)

@app.route('/')
def index():
 	return app.send_static_file('index.html')

# /users/sort?field=age or name or id
@app.route('/users/sort')
def getUsersSorted():
 	field = request.args.get('field')
 	usersSorted = sorted(users, key=lambda u: u[field])
 	return jsonify(usersSorted)



@app.route('/users/<id>')
def getuser(id):
 	user = list(filter(lambda u: str(u['id']) == id, users))
 	return jsonify(user)
if __name__ == "__main__":
	app.run()



if __name__ == '__main__':
  socketio.run(app)   # users = [
# 	{
# 			'id':2,
# 			'name':'Anne',
# 			'age':23


# 	}, 
# 	{	
# 			'id':1,
# 			'name': 'Cathy',
# 			'age':44



# 	},
# 	{
# 			'id':3,
# 			'name': 'Amanda',
# 			'age':21



# 	},



# ]



# @app.route('/users')
# def getusers():
# 	return jsonify(users)


# @app.route('/')
# def index():
# 	return app.send_static_file('index.html')


# # /users/sort?field=age or name or id
# @app.route('/users/sort')
# def getUsersSorted():
# 	field = request.args.get('field')
# 	usersSorted = sorted(users, key=lambda u: u[field])
# 	return jsonify(usersSorted)



# @app.route('/users/<id>')
# def getuser(id):
# 	user = list(filter(lambda u: str(u['id']) == id, users))
# 	return jsonify(user)
# if __name__ == "__main__":
# 	app.run()