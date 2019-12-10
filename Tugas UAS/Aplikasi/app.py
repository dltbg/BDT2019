from flask import Flask
import mysql.connector
import json
from flask import jsonify, request
from datetime import datetime as dt


app = Flask(__name__)
app.secret_key = "tidb"
app.config['MYSQL_HOST'] = '192.168.16.42'
app.config['MYSQL_PORT'] = 4000
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'aplc'

db = mysql.connector.connect(
	host="192.168.16.42",
	user="root",
	passwd="",
	database="aplc",
	port=4000
)


@app.route('/aplc', methods=['GET'])
def get_aplc():
	csr = db.cursor()
	csr.execute("select * from aplc_data")
	data=[]
	for (id, name, email, age, phone) in csr:
		save = {}
		save["id"] = id;
		save["name"]=name;
		save["email"]=email;
		save["age"]=age;
		save["phone"]=phone;
		data.append(save)

	csr.close()
	response = json.dumps(data)
	return response

@app.route('/aplc', methods=['POST'])
def add_aplc():
	request_json = request.json
	aplc_id = request_json["id"]
	aplc_name = request_json["name"]
	aplc_email = request_json["email"]
	aplc_age = request_json["age"]
	aplc_phone = request_json["phone"]

	csr = db.cursor()
	csr.execute("insert into aplc_data (`id`,`name`,`email`,`age`,`phone`) values (%s, %s, %s, %s, %s);", (aplc_id,aplc_name,aplc_email,aplc_age,aplc_phone))
	db.commit()
	csr.close()
	response = jsonify('Data Added!')
	response.status_code = 200
	return response

@app.route('/aplc/<id>', methods=['PUT'])
def update_aplc(id):
    request_json = request.json
    aplc_name = request_json["name"]
    aplc_age = request_json["age"]

    csr = db.cursor()
    csr.execute("update aplc_data set name = %s, age = %s where id=%s", (aplc_name,aplc_age,id))
    db.commit()
    csr.close()

    response = jsonify('Data Updated')
    response.status_code = 200
    return response

@app.route('/aplc/<id>', methods=['DELETE'])
def delete_ufo(id):

	csr = db.cursor()
	csr.execute("delete from aplc_data where id="+str(id))
	db.commit()
	csr.close()
	response = jsonify('Data Deleted')
	response.status_code = 200
	return response

		
if __name__ == "__main__":
	app.run()