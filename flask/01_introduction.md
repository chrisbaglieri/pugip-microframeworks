<!SLIDE center>

![flask](flask.png)

<!SLIDE bullets incremental transition=fade>

# flask at a high level

* maintained by [Team Pocoo](http://pocoo.org/)
* source at [github.com/mitsuhiko/flask](https://github.com/mitsuhiko/flask)
* the readme on github is abysmal
* however the site at [flask.pocoo.org](http://flask.pocoo.org/) is stellar
* the heaviest of the bunch

<!SLIDE bullets incremental transition=fade>

# what makes up flask

* routing engine
* lightweight templating engine (jinja2)
* excellent request/response handling
* session management
* logging & built in debugger
* message flashing

<!SLIDE transition=fade>

	@@@ python
	from flask import Flask
	app = Flask(__name__)

	@app.route('/')
	def hello_world():
		return 'Hello World!'

	if __name__ == '__main__':
		app.run()

<!SLIDE bullets incremental transition=fade>

# less talk more action

* pip install flask (includes Werkzeug & Jinja2)
* mkdir teachme
* cd teachme