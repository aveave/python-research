import json
from flask import Flask, request

# начать с функции и __name__

# In Flask, the Flask class is used to create an instance of a web application. 
# The __name__ parameter that is passed to the Flask constructor is a special Python variable 
# that refers to the name of the current module.

# When you create a Flask application using the Flask(__name__) syntax, 
# you are creating an instance of the Flask class that is associated with the current module. 
# This instance is used to define the routes and other settings for your web application.
app = Flask(__name__)

# The @app.route('/') decorator is used to define a route that maps to the root URL of the application. 
# When a user visits the root URL (/), the index function is called, which returns the string "Hello, world!".

# This instance is assigned to the variable app, which is then used to define the routes for the application.

@app.route('/api/users', methods=['POST'])
def mock_create_user():
    print('create user')
    data = request.get_json()
    print(data)
    return '', 200

@app.route('/api/users', methods=['GET'])
def mock_get_user():
    print('Get users')
    return read_data_from_file('data/users.json')

@app.route('/api/users/<id>', methods=['GET'])
def mock_get_user_by_id(id):
    print(f"Get user by id {id}")
    return read_data_from_file('data/user_by_id.json')

def read_data_from_file(filename):
    with open(filename, 'r') as file:
        return json.load(file)

if __name__ == '__main__':
    app.run(debug=True)

# In Python, __name__ is a special built-in variable that stores the name of the current module. 
# When a Python script is executed, its __name__ attribute is set to '__main__' 
# if it is the main script being run, or to the name of the module if it is being imported as a module into another script.

# The line if __name__ == '__main__': is a common idiom used in Python scripts to check whether the script 
# is being run as the main program or being imported as a module. 
# This line essentially means that the code following the if statement will only be executed 
# if the script is being run as the main program, and not if it is being imported as a module.