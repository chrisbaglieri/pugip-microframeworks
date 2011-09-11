<!SLIDE bullets transition=fade>

# what else?

* sessions

<!SLIDE smaller transition=fade>

	@@@ python
	@app.route('/login', methods=['GET', 'POST'])
	def login():
		session['username'] = request.form['username']
		return redirect(url_for('index'))

	@app.route('/logout')
	def logout():
		session.pop('username', None)
		return redirect(url_for('index'))

<!SLIDE bullets transition=fade>

# what else?

* flash messaging

<!SLIDE smaller transition=fade>

	@@@ python
	# in your handler
	flash("Successfully created foo", category='success')

	# in your template
	{% for category, msg in get_flashed_messages() %}
	  <p class="{{ category }}">{{ msg }}</p>
	{% endfor %}

<!SLIDE bullets transition=fade>

# what else?

* logging

<!SLIDE smaller transition=fade>

	@@@ python
	app.logger.debug('A value for debugging')
	app.logger.warning('A warning occurred (%d apples)', 42)
	app.logger.error('An error occurred')

<!SLIDE bullets transition=fade>

# what else?

* hooking in WSGI middlewares

<!SLIDE smaller transition=fade>

	@@@ python
	# tornado
	from tornado.wsgi import WSGIContainer
	from tornado.httpserver import HTTPServer
	from tornado.ioloop import IOLoop
	from yourapplication import app

	http_server = HTTPServer(WSGIContainer(app))
	http_server.listen(5000)
	IOLoop.instance().start()
	
	# gevent
	from gevent.wsgi import WSGIServer
	from yourapplication import app

	http_server = WSGIServer(('', 5000), app)
	http_server.serve_forever()

	# gunicorn
	gunicorn teachme:app