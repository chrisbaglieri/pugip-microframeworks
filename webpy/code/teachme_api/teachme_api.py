import json
import web
import model

urls = (
	'/topics', 'topics',
	'/topics/(\d+)', 'topic'
)

class topics:
	
	def GET(self):
		topics = dict()
		for topic in list(model.get_topics()):
			topics[topic._id] = topic
		web.header('Content-Type', 'application/json')
		return json.dumps(topics)
	
	def POST(self):
		data = web.data()
		params = dict()
		for namevalue in data.split('&'):
			params[namevalue.split('=')[0]] = str(namevalue.split('=')[1].replace('+', ' '))
		topic = model.create_topic(params["name"], params["description"], params["presenter"])
		return json.dumps(topic)

class topic:
	
	def GET(self, id):
		topic = model.get_topic(id)
		web.header('Content-Type', 'application/json')
		return json.dumps(topic)
	
	def PUT(self, id):
		data = web.data()
		params = dict()
		for namevalue in data.split('&'):
			params[namevalue.split('=')[0]] = namevalue.split('=')[1].replace('+', ' ')
		topic = model.update_topic(id, params["name"], params["description"], params["presenter"])
		return json.dumps(topic)

	def DELETE(self, id):
		model.delete_topic(id)
		web.header('Content-Type', 'application/json')
		return json.dumps({'status':'success'})
    
app = web.application(urls, globals())

if __name__ == '__main__':
	app.run()