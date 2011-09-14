<!SLIDE bullets transition=fade>

# what else?

* error pages

<!SLIDE smaller transition=fade>

	@@@ python
	@error(404)
	def error404(error):
	    return 'Nothing here, sorry'

<!SLIDE bullets transition=fade>

# what else?

* lightweight templating engine

<!SLIDE smaller transition=fade>

	@@@ html
	<html>
	<head>
	  <title>{{title or 'No title'}}</title>
	</head>
	<body>
	  %include
	</body>
	</html>

<!SLIDE bullets transition=fade>

# what else?

* hooking in WSGI middlewares

<!SLIDE smaller transition=fade>

	@@@ python
	bottle.run(server='[server name]')

	""" 
	supported servers:
		flup
		gae
		cherrypy
		paste
		rocket
		gunicorn
		tornado
		twisted
		diesel
	"""