from random import randint
from mongokit import Connection, Document

MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017

connection = Connection(MONGODB_HOST, MONGODB_PORT)

@connection.register
class Topic(Document):
	__collection__ = 'topics'
	__database__ = 'teachme'
	structure = {
		'_id': int,
		'name': unicode,
		'description': unicode,
		'presenter': unicode
	}
	required_fields = ['name', 'description']
	use_dot_notation = True


def get_topics():
	return list(connection.Topic.find())

def get_topic(id):
	return connection.Topic.find_one({'_id': int(id)})

def create_topic(name, description, presenter):
	topic = connection.Topic()
	topic._id = randint(1, 1000000)
	topic.name = unicode(name)
	topic.description = unicode(description)
	topic.presenter = unicode(presenter)
	topic.save()
	return topic

def update_topic(id, name, description, presenter):
	topic = connection.Topic()
	topic._id = int(id)
	topic.name = unicode(name)
	topic.description = unicode(description)
	topic.presenter = unicode(presenter)
	topic.save()
	return topic

def delete_topic(id):
	topic = connection.Topic.find_one({'_id': int(id)})
	topic.delete()
	return True