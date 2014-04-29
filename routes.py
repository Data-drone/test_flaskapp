from flask import Flask, request, jsonify, render_template
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://CarAccess:Cars_Data@localhost/CarsScraper'

class ManufCounts(db.Model):
	__tablename__ = 'vw_CarCounts'
	Manufacturer = db.Column(db.String(45), primary_key = True)
	Number = db.Column(db.Integer)

class TableData(db.Model):
	__tablename__ = 'vw_LatestDataTable'
	Manufacturer = db.Column(db.String(45))
	Year = db.Column(db.DateTime)
	Make = db.Column(db.String(100))
	Model = db.Column(db.String(45))
	Transmission = db.Column(db.String(45))
	km = db.Column(db.Integer)
	seller = db.Column(db.String(45))
	Price = db.Column(db.Integer)
	source = db.Column(db.String(128))
	GuideID = db.Column(db.String(45), primary_key = True)	

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

@app.route('/TblData/', methods=['GET'])
def TblData():
	if request.method == 'GET':
		results = TableData.query.all()
		
		json_results = []
		for result in results:
			d = {'Manuf': result.Manufacturer,
				 'Year': result.Year,
				 'Make': result.Make,
				 'Model': result.Model,
				 'Transmission': result.Transmission,
				 'km': result.km,
				 'seller': result.seller,
				 'Price': result.Price,
				 'source': result.source}
			json_results.append(d)

	return jsonify(items=json_results)

@app.route('/')
def home():
	return render_template('base.html')

@app.route('/app1/')
def app1():
	return render_template('app_bar1.html')

@app.route('/app1/vis1/')
def app1_vis1():
	return render_template('vis1.html')

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

@app.route('/counts/', methods=['GET'])
def carcount():
	if request.method == 'GET':
		results = ManufCounts.query.all()
		
		json_results = []
		for result in results:
			d = {'Manuf': result.Manufacturer,
				'Number': result.Number}
			json_results.append(d)

	return jsonify(values=json_results)


if __name__ == '__main__':
  app.run(debug=True)
