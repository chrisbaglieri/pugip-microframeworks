from mongokit import Connection, Document, ObjectId
from flask import Flask, redirect, render_template, request, url_for

MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017

app = Flask(__name__)
app.config.from_object(__name__)

connection = Connection(app.config['MONGODB_HOST'], app.config['MONGODB_PORT'])

@connection.register
class Topic(Document):
	__collection__ = 'topics'
	__database__ = 'teachme'
	structure = {
		'name': unicode,
		'description': unicode,
		'presenter': unicode
	}
	required_fields = ['name', 'description']
	use_dot_notation = True

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/topics')
def show_topics():
	topics = list(connection.Topic.find())
	return render_template('topics.html', topics=topics)
	
@app.route('/topics/<id>')
def show_topic(id):
	topic = connection.Topic.find_one({'_id': ObjectId(id)})
	return render_template('topic.html', topic=topic)
	
@app.route('/topics/new')
def new_topic():
	return render_template('new_topic.html')
	
@app.route('/topics', methods=['POST'])
def create_topic():
	topic = connection.Topic()
	topic.name = request.form['name']
	topic.description = request.form['description']
	topic.presenter = request.form['presenter']
	topic.save()
	return redirect(url_for('show_topics'))
	
@app.route('/topics/<id>/edit')
def edit_topic(id):
	topic = connection.Topic.find_one({'_id': ObjectId(id)})
	return render_template('edit_topic.html', topic=topic)
	
@app.route('/topics/<id>', methods=['POST'])
def update_topic(id):
	topic = connection.Topic.find_one({'_id': ObjectId(id)})
	topic.name = request.form['name']
	topic.description = request.form['description']
	topic.presenter = request.form['presenter']
	topic.save()
	return redirect(url_for('show_topics'))

@app.route('/topics/<id>/delete')
def delete_topic(id):
	topic = connection.Topic.find_one({'_id': ObjectId(id)})
	return render_template('delete_topic.html', topic=topic)

@app.route('/topics/<id>/delete', methods=['POST'])
def destroy_topic(id):
	topic = connection.Topic.find_one({'_id': ObjectId(id)})
	topic.delete()
	return redirect(url_for('show_topics'))

if __name__ == '__main__':
	app.debug = True
	app.run()