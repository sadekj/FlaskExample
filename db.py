import dataset

db = dataset.connect('sqlite:///wecode')

def tempdata():
	table = db['users']
	table.insert(dict(name='John Doe', age=37))
	table.insert(dict(name='Jane Doe', age=34, gender='female'))

def search(keyword):
	table = db['users']
	john = table.find_one(name=keyword)
	return john

#tempdata()