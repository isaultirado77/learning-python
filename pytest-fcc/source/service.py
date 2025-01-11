database = {
	1: 'Alice', 
	2: 'Bob',
	3: 'Charlie'
}


def get_user_from_db(id: int): 
	return database.get(id)
