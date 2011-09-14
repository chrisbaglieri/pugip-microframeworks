<!SLIDE center>

![cherrypy](cherrypy.jpg)

<!SLIDE bullets transition=fade>

# cherry.py at a high level

* source available at [cherrypy.org/browser](http://www.cherrypy.org/browser); someone tell them about gituhub
* the site at [cherrypy.org](http://cherrypy.org) is so-so
* support for rest is not obvious
* weighs in @ 27768 lines

<!SLIDE smaller transition=fade>

# code

	@@@ python
	import cherrypy

	class HelloWorld(object):
		def index(self):
			return "Hello World!"
		index.exposed = True

	cherrypy.quickstart(HelloWorld())

<!SLIDE bullets transition=fade>

# less talk more action

* pip install cherrypy
* pip install jinja2
* mkdir teachme
* cd teachme