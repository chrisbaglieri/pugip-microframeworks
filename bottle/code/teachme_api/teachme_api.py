from random import randint
from mongokit import Connection, Document
from bottle import get, post, put, delete, run, request

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

@get('/topics')
def show_topics():
	topics = dict()
	for topic in list(connection.Topic.find()):
		topics[topic._id] = topic
	return topics

@get('/topics/:id')
def show_topic(id):
	topic = connection.Topic.find_one({'_id': int(id)})
	return topic

@post('/topics')
def create_topic():
	topic = connection.Topic()
	topic._id = randint(1, 1000000)
	topic.name = unicode(request.params['name'])
	topic.description = unicode(request.params['description'])
	topic.presenter = unicode(request.params['presenter'])
	topic.save()
	return topic

@put('/topics/:id')
def update_topic(id):
	topic = connection.Topic.find_one({'_id': int(id)})
	topic.name = unicode(request.params['name'])
	topic.description = unicode(request.params['description'])
	topic.presenter = unicode(request.params['presenter'])
	topic.save()
	return topic

@delete('/topics/:id')
def destroy_topic(id):
	topic = connection.Topic.find_one({'_id': int(id)})
	if topic is not None:
		topic.delete()
	return {'status':'success'}

run(host='localhost', port=8080, reloader=True)