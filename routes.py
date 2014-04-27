from flask import Flask, request, jsonify
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://CarAccess:Cars_Data@localhost/CarsScraper'

class Listing(db.Model):
	__tablename__ = 'tbl_CarsRawData'
	Manufacturer = db.Column(db.String(45))
	Year = db.Column(db.DateTime)
	Make = db.Column(db.String(100))
	Model = db.Column(db.String(45))
	Engine = db.Column(db.String(45))
	Transmission = db.Column(db.String(45))
	km = db.Column(db.Integer)
	GuideID = db.Column(db.String(45), primary_key = True)
	seller = db.Column(db.String(45))
	link = db.Column(db.String(1500))
	Price = db.Column(db.Integer)
	source = db.Column(db.String(128))
	timestamp = db.Column(db.DateTime)

@app.route('/listings/', methods=['GET'])
def listings():
	if request.method == 'GET':
		results = Listing.query.all()
		
		json_results = []
		for result in results:
			d = {'Manuf': result.Manufacturer,
				 'Year': result.Year,
				 'Make': result.Make,
				 'Model': result.Model,
				 'Engine': result.Engine,
				 'Transmission': result.Transmission,
				 'km': result.km,
				 'GuideID': result.GuideID,
				 'seller': result.seller,
				 'link': result.link,
				 'Price': result.Price,
				 'source': result.source,
				 'timestamp': result.timestamp}
			json_results.append(d)

	return jsonify(items=json_results)

if __name__ == '__main__':
  app.run(debug=True)
