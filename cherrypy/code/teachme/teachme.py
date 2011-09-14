from random import randint
import cherrypy
from mongokit import Connection, Document
from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('templates'))

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

class Root:
	
	@cherrypy.expose
	def index(self):
		tmpl = env.get_template('index.html')
		return tmpl.render()

class Topics:
	
	@cherrypy.expose
	def index(self):
		topics = list(connection.Topic.find())
		tmpl = env.get_template('topics.html')
		return tmpl.render(topics=topics)
	
	@cherrypy.expose
	def new(self):
		tmpl = env.get_template('new_topic.html')
		return tmpl.render()
	
	@cherrypy.expose
	def create(self, name, description, presenter):
		topic = connection.Topic()
		topic._id = randint(1, 1000000)
		topic.name = name
		topic.description = description
		topic.presenter = presenter
		topic.save()
		raise cherrypy.HTTPRedirect('/topics')
	
	@cherrypy.expose
	def edit(self, id):
		topic = connection.Topic.find_one({'_id': int(id)})
		tmpl = env.get_template('edit_topic.html')
		return tmpl.render(topic=topic)
	
	@cherrypy.expose
	def update(self, id, name, description, presenter):
		topic = connection.Topic.find_one({'_id': int(id)})
		topic.name = name
		topic.description = description
		topic.presenter = presenter
		topic.save()
		raise cherrypy.HTTPRedirect('/topics')
	
	@cherrypy.expose
	def delete(self, id):
		topic = connection.Topic.find_one({'_id': int(id)})
		tmpl = env.get_template('delete_topic.html')
		return tmpl.render(topic=topic)
    
	@cherrypy.expose
	def destroy(self, id):
		topic = connection.Topic.find_one({'_id': int(id)})
		topic.delete()
		raise cherrypy.HTTPRedirect('/topics')
	
root = Root()
root.topics = Topics()
cherrypy.quickstart(root)