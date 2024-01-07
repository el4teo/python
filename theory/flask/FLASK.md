~~~ txt
  _____ __                 __    
_/ ____\  | _____    _____|  | __
\   __\|  | \__  \  /  ___/  |/ /
 |  |  |  |__/ __ \_\___ \|    < 
 |__|  |____(____  /____  >__|_ \
                 \/     \/     \/
~~~

[BACK](../THEORY.md)

- [Introduction](#introduction)
  - [Installing in venv](#installing-in-venv)
    - [Windows](#windows)
    - [Linux](#linux)
- [Using custom IP and PORT](#using-custom-ip-and-port)
- [Linode tutorial](#linode-tutorial)
  - [Rest](#rest)
  - [Installing Flask](#installing-flask)
  - [Create the List Endpoint in Flask](#create-the-list-endpoint-in-flask)
  - [Create the Detail Endpoint in Flask](#create-the-detail-endpoint-in-flask)
  - [Add Filters to the List Endpoint](#add-filters-to-the-list-endpoint)
  - [Build a Create Endpoint](#build-a-create-endpoint)
  - [Create the Update Endpoint](#create-the-update-endpoint)
  - [Create the Delete Record Endpoint](#create-the-delete-record-endpoint)

# Introduction


Flask is a Python micro-framework for building web applications and web APIs.

## Installing in venv

### Windows

From Command Promt

~~~ sh
cd project_dir
python.exe -m venv .venv

.\.venv\Scripts\activate.bat
# .\.venv\Scripts\Activate # PowerShell
echo %PATH%
# echo $env:PATH # PowerShell

pip install flask
deactivate # Optional
~~~

### Linux

~~~ sh
cd project_dir
python3 -m venv .venv

source .venv/bin/activate
which python3

pip install flask
deactivate # Optional
~~~

# Using custom IP and PORT

- Get your IP address

~~~ sh
# Linux
ifconfig

# Windows

~~~

- Instead of the default execution

~~~ sh
# Goto app directory
cd flask

# Start the app
export FLASK_APP=prog_lang_app.py
flask run
~~~

- Start the app from the `prog_lang_app.py` file with  `IP` and `PORT`

~~~ py
if __name__=='__main__':
  app.run(host='172.30.1.153', port=5000)
~~~

~~~ sh
(.venv) cal7x7@RD0204873:~/repos/mds-and-scripts/languages/python/flask$ python prog_lang_app.py 
 * Serving Flask app 'prog_lang_app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://172.30.1.153:5000
Press CTRL+C to quit
~~~


# Linode tutorial

[tutorial](https://www.linode.com/docs/guides/create-restful-api-using-python-and-flask/)

At the end of the guide, you have an API that allows clients to complete the following:

- `GET` all programming languages stored in the API
- `GET` a specific instance of a programming language
- Filter the programming language resources based on the publication year field
- `POST`, `PUT`, and `DELETE` a programming language instance

## Rest

- The REST protocol gives clients access to resources stored in a database and allows clients to perform operations on the stored data.
- The operations are known as CRUD operations (create, read, update, and delete). 
- The following sections show you how to create the CRUD operations for your Flask web API.

## Installing Flask

~~~ sh
# Move to the project directory
cd flask

# Create the venv (only the first time)
python3 -m venv .venv

# Activate the venv (each time)
source .venv/bin/activate

# Install the library (only the first time)
pip install flask

# Check it is well installed
python -m flask --version

# Deactivate the venv (optional)
deactivate
~~~

If there is a problem with the Scania proxy

~~~ sh
# This will solve the proxy problems FOR THE ROOT USER
sudo /usr/sbin/cntlm

# Use the .venv as root and 
sudo su

# Follow the installation steps ...
source .venv/bin/activate
pip install flask
python -m flask --version
~~~

## Create the List Endpoint in Flask

- RESTful services typically have two endpoints used to retrieve (GET) resources.
  - One endpoint lists all resources or filters them according to some criterion.
  - The second endpoint retrieves the details of a specific resource based on a unique identifier.
- In this section, you create two endpoints to GET resources from your API. This section may refer to these endpoints as the `list` and `details` endpoints.
- All the steps in this section edit the same file, `prog_lang_app.py`.

~~~ py
from flask import Flask

# Instance of Flask
app = Flask(__name__)

# Local "DB"
in_memory_datastore = {
   "COBOL" : {"name": "COBOL", "publication_year": 1960, "contribution": "record data"},
   "ALGOL" : {"name": "ALGOL", "publication_year": 1958, "contribution": "scoping and nested functions"},
   "APL" : {"name": "APL", "publication_year": 1962, "contribution": "array processing"},
}

# This endpoint fetches all the records in the datastore
@app.get('/programming_languages')
def list_programming_languages():
   return {"programming_languages":list(in_memory_datastore.values())}
~~~

- Start the app and send a GET

~~~ sh
# Goto app directory
cd flask

# Start the app
export FLASK_APP=prog_lang_app.py
flask run
~~~

- Open a browser and visit http://127.0.0.1:5000/ to access the app running locally on your computer.
- Visit http://127.0.0.1:5000/programming_languages in the browser to view the JSON object containing the contents of the datastore you created.

## Create the Detail Endpoint in Flask

- The `details` endpoint has an interpolated variable in the endpoint string called `programming_language_id`
  - This variable allows you to query for a specific item in your datastore.
  - The id refers to the index in the list related to a specific instance of a programming language resource.
  - This presents a problem once clients can delete items from the datastore. This is fixed in a later section.

- Add this code to the `prog_lang_app.py`

~~~ py
# The details endpoint has an interpolated variable called programming_language_id
@app.route('/programming_languages/<programming_language_name>')
def get_programming_language(programming_language_name):
   return in_memory_datastore[programming_language_name]
~~~

- Start the app and send a GET

~~~ sh
# Goto app directory
cd flask

# Start the app
export FLASK_APP=prog_lang_app.py
flask run
~~~

- Run the app and visit http://127.0.0.1:5000/programming_languages/COBOL in your browser. You should see a similar output returned by your API.

## Add Filters to the List Endpoint

- Update the `prog_lang_app.py` file’s in_memory_datastore dictionary with a few more programming language entries.

~~~ py
in_memory_datastore = {
   "COBOL": {"name": "COBOL", "publication_year": 1960, "contribution": "record data"},
   "ALGOL": {"name": "ALGOL", "publication_year": 1958, "contribution": "scoping and nested functions"},
   "APL": {"name": "APL", "publication_year": 1962, "contribution": "array processing"},
   "BASIC": {"name": "BASIC", "publication_year": 1964, "contribution": "runtime interpretation, office tooling"},
   "PL": {"name": "PL", "publication_year": 1966, "contribution": "constants, function overloading, pointers"},
   "SIMULA67": {"name": "SIMULA67", "publication_year": 1967,
                "contribution": "class/object split, subclassing, protected attributes"},
   "Pascal": {"name": "Pascal", "publication_year": 1970,
              "contribution": "modern unary, binary, and assignment operator syntax expectations"},
   "CLU": {"name": "CLU", "publication_year": 1975,
           "contribution": "iterators, abstract data types, generics, checked exceptions"},
}
~~~

- Now, you can add the code to allow clients to filter on the publication_year parameter.

~~~ py
from flask import Flask, request

# [...]

@app.get('/programming_languages')
def list_programming_languages():
   before_year = request.args.get('before_year') or '30000'
   after_year = request.args.get('after_year') or '0'
   qualifying_data = list(
       filter(
           lambda pl: int(before_year) > pl['publication_year'] > int(after_year),
           in_memory_datastore.values()
       )
   )

   return {"programming_languages": qualifying_data}
~~~

- Flask automatically treats all parameters passed to a routed function (besides interpolated path parameters) as query parameters.
  - If a client does not pass any query parameters, the default start year of 0 and the default end year of 30,000 automatically capture all languages.

~~~ sh
# Goto app directory
cd flask

# Start the app
export FLASK_APP=prog_lang_app.py
flask run
~~~

- Compare the GET requests:
  - http://127.0.0.1:5000/programming_languages
  - http://127.0.0.1:5000/programming_languages?after_year=1965
  - http://127.0.0.1:5000/programming_languages?before_year=1970
  - http://127.0.0.1:5000/programming_languages?after_year=1965&before_year=1970

## Build a Create Endpoint

- So far, all the endpoints expect clients to use the `GET` HTTP verb to make their requests. In this section, you write the code to support the `POST` HTTP verb.
- The `create` endpoint expects a `POST` verb as well as a request body.
- The request body is a payload of data that specifies the attributes of the new resource that the client wants to add.
  - In this case, those attributes are sent as a JSON object:
    - name
    - publication_year
    - contribution
- To use the same route in your API with different request verbs:
  - Write your code under the same annotation.
  - Then, use conditional logic to route the request to the correct place.

~~~ py
@app.route('/programming_languages', methods=['GET', 'POST'])
def programming_languages_route():
   if request.method == 'GET':
       return list_programming_languages()
   elif request.method == "POST":
       return create_programming_language(request.get_json(force=True))
~~~

- Now, add the new create_programming_language method below list_programming_languages() method:
- 
~~~ py
def create_programming_language(new_lang):
   language_name = new_lang['name']
   in_memory_datastore[language_name] = new_lang
   return new_lang
~~~

- Use the cURL to create a programming language on the command line:

~~~ sh
curl -X POST http://127.0.0.1:5000/programming_languages -H 'Content-Type: application/json' -d '{"name": "Java", "publication_year": 1995, "contribution": "Object-oriented programming language."}'
~~~

- Once you have created the new resource, make a GET request to 
  - From web browser
    - http://127.0.0.1:5000/programming_languages
  - From terminal
    - curl http://127.0.0.1:5000/programming_languages

## Create the Update Endpoint

- To update a resource, you send a `PUT` request with a request body to the URL of the record you want to update.
- Remove the @app.route annotation and the get_programming_language() function. Replace them with the following code:

~~~ py
@app.route('/programming_languages/<programming_language_name>', methods=['GET', 'PUT'])
def programming_language_route(programming_language_name):
   if request.method == 'GET':
       return get_programming_language(programming_language_name)
   elif request.method == "PUT":
       return update_programming_language(programming_language_name, request.get_json(force=True))
~~~

- Now add the `update_programming_language()` function:

~~~ py
def update_programming_language(lang_name, new_lang_attributes):
   lang_getting_update = in_memory_datastore[lang_name]
   lang_getting_update.update(new_lang_attributes)
   return lang_getting_update
~~~

- To test your new endpoint, send a request to it to update an existing resource. For example, send a request using Postman similar to the following:

~~~ sh
# PUT
curl -X PUT http://127.0.0.1:5000/programming_languages/Java -H 'Content-Type: application/json' -d '{"contribution": "The JVM"}'

# GET
curl http://127.0.0.1:5000/programming_languages
~~~

## Create the Delete Record Endpoint

- The endpoint to delete a record is similar to the update endpoint. The difference is the HTTP verb that you use. RESTful services conventionally use a `DELETE` verb for the delete endpoint.
- Update your @app.route annotation to include the DELETE method, as shown below:

~~~ py
...
@app.route('/programming_languages/<programming_language_name>', methods=['GET', 'PUT', 'DELETE'])
def programming_language_route(programming_language_name):
   if request.method == 'GET':
       return get_programming_language(programming_language_name)
   elif request.method == "PUT":
       return update_programming_language(programming_language_name, request.get_json(force=True))
   elif request.method == "DELETE":
       return delete_programming_language(programming_language_name)
~~~

- Next, add the `delete_programming_language()` function below the `update_programming_language()` function:

~~~ py
def delete_programming_language(lang_name):
   deleting_lang = in_memory_datastore[lang_name]
   del in_memory_datastore[lang_name]
   return deleting_lang

- To test your new endpoint, send a request to it to update an existing resource. For example, send a request using Postman similar to the following:

~~~ sh
# DELETE
curl -X DELETE http://127.0.0.1:5000/programming_languages/COBOL

# GET
curl http://127.0.0.1:5000/programming_languages
~~~