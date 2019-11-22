from flask import Flask
from flask_pymongo import PyMongo
from flask import jsonify, request
from bson.json_util import dumps
from bson.objectid import ObjectId


app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://mongo-admin:password@192.168.16.44:27017/ufo?authSource=admin"
mongo = PyMongo(app, retryWrites=False)

@app.route('/ufo', methods = ['GET'])
def get_ufo():
    ufo = mongo.db.ufoCollection.find().limit(2)
    response = dumps(ufo)
    return response

@app.route('/ufo/<id>', methods = ['GET'])
def gets_ufo(id):
    ufo = mongo.db.ufoCollection.find({ '_id' : ObjectId(id) })
    response = dumps(ufo)
    return response

@app.route('/ufo', methods=['POST'])
def add_ufo():
	request_json = request.json
	ufo_url = request_json['URL']
	ufo_id = request_json['ID']
	ufo_name = request_json['Name']
	ufo_subtitle = request_json['Subtitle']
	ufo_icon_url = request_json["Icon URL"]
	ufo_average_user_rating = request_json["Average User Rating"]
	ufo_user_rating_count = request_json["User Rating Count"]
	ufo_price = request_json["Price"]
	ufo_in_app_purchases = request_json["In-app Purchases"]
	ufo_description = request_json["Description"]
	ufo_developer = request_json["Developer"]
	ufo_age_rating = request_json["Age Rating"]
	ufo_languages = request_json["Languages"]
	ufo_size = request_json["Size"]
	ufo_primary_genre = request_json["Primary Genre"]
	ufo_genres = request_json["Genres"]
	ufo_original_release_date = request_json["Original Release Date"]
	ufo_current_version_release_date = request_json["Current Version Release Date"]


	ufo_insert = mongo.db.ufoCollection.insert({
    	'URL':ufo_url,
        'ID':ufo_id,
        'Name':ufo_name,
        'Subtitle':ufo_subtitle,
        'Icon URL':ufo_icon_url,
        'Average User Rating':ufo_average_user_rating,
        'User Rating Count':ufo_user_rating_count,
        'Price':ufo_price,
        'In-app Purchases':ufo_in_app_purchases,
        'Description':ufo_description,
        'Developer':ufo_developer,
        'Age Rating':ufo_age_rating,
        'Languages':ufo_languages,
        'Size':ufo_size,
        'Primary Genre':ufo_primary_genre,
        'Genres':ufo_genres,
        'Original Release Date':ufo_original_release_date,
        'Current Version Release Date':ufo_current_version_release_date
    	})

	response = jsonify('Ufo Added! new id ={}'.format(ufo_insert))
	response.status_code = 200
	return response

@app.route('/ufo/<id>', methods=['PUT'])
def update_ufo(id):
	request_json = request.json
	ufo_iid = request_json['_id']
	ufo_url = request_json['URL']
	ufo_id = request_json['ID']
	ufo_name = request_json['Name']
	ufo_subtitle = request_json['Subtitle']
	ufo_icon_url = request_json["Icon URL"]
	ufo_average_user_rating = request_json["Average User Rating"]
	ufo_user_rating_count = request_json["User Rating Count"]
	ufo_price = request_json["Price"]
	ufo_in_app_purchases = request_json["In-app Purchases"]
	ufo_description = request_json["Description"]
	ufo_developer = request_json["Developer"]
	ufo_age_rating = request_json["Age Rating"]
	ufo_languages = request_json["Languages"]
	ufo_size = request_json["Size"]
	ufo_primary_genre = request_json["Primary Genre"]
	ufo_genres = request_json["Genres"]
	ufo_original_release_date = request_json["Original Release Date"]
	ufo_current_version_release_date = request_json["Current Version Release Date"]

	mongo.db.ufoCollection.update_one(
		{'_id': ObjectId(ufo_iid['$oid']) if '$oid' in ufo_iid else ObjectId(ufo_iid)},
		{
			'$set' : {
				'URL':ufo_url,
				'ID':ufo_id,
				'Name':ufo_name,
				'Subtitle':ufo_subtitle,
				'Icon URL':ufo_icon_url,
				'Average User Rating':ufo_average_user_rating,
				'User Rating Count':ufo_user_rating_count,
				'Price':ufo_price,
				'In-app Purchases':ufo_in_app_purchases,
				'Description':ufo_description,
				'Developer':ufo_developer,
				'Age Rating':ufo_age_rating,
				'Languages':ufo_languages,
				'Size':ufo_size,
				'Primary Genre':ufo_primary_genre,
				'Genres':ufo_genres,
				'Original Release Date':ufo_original_release_date,
				'Current Version Release Date':ufo_current_version_release_date
			}
		}
	)

	response = jsonify('Data diupdate. ID = {}'.format(ufo_iid))
	response.status_code = 200
	return response

@app.route('/ufo/<id>', methods=['DELETE'])
def delete_ufo(id):
	mongo.db.ufoCollection.delete_one({'_id' : ObjectId(id)})
	response = jsonify('Data terhapus. ID ={}'.format(id))
	response.status_code = 200
	return response

@app.route('/ufo/count', methods=['GET'])
def count():
	count_ufo = mongo.db.ufoCollection.aggregate([
		{
			"$group": {
			"_id":"$Primary Genre",
			"count":{"$sum":1}
			}
		}
	])
	response = dumps(count_ufo)
	return response

@app.route('/ufo/max', methods=["GET"])
def max():
	max_ufo = mongo.db.ufoCollection.aggregate([
		{
			"$group": {
			"_id":"$Primary Genre",
			"Price":{"$max":"$Price"}
			}
		}
	])
	response = dumps(max_ufo)
	return response
		
if __name__ == "__main__":
	app.run()