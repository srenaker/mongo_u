import bottle
import pymongo

@bottle.route('/')	
def homepage():
	
	connection = pymongo.MongoClient('localhost', 27017)

    # attach to test database
	db = connection.test
	things = db.things
	item = things.find_one()
	
	mythings = item['mythings']
	return bottle.template('hello_world', {'username': 'srenaker', 'things': mythings})

@bottle.post('/favorite_sport')
def favorite_sport():
	sport = bottle.request.forms.get('sport')
	if (sport == None or sport == ''):
		sport = "No sport selected"
	
	#return bottle.template('favorite_sport.tpl', {'sport': sport})
	bottle.response.set_cookie("sport", sport)
	bottle.redirect('/show_sport')
	
@bottle.route('/show_sport')
def show_sport():
	sport = bottle.request.get_cookie('sport')
	return bottle.template('show_sport', {'sport': sport})
		

bottle.debug(True)
bottle.run(host='localhost', port=8080)