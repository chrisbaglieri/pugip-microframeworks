<!SLIDE center>

![bottle](bottle.png)

<!SLIDE bullets transition=fade>

# bottle at a high level

* source at [github.com/defnull/bottle](https://github.com/defnull/bottle)
* the readme on github is abysmal
* however the site at [bottlepy.org](http://bottlepy.org) is stellar
* one of the lightest of the bunch @ 2697 lines

<!SLIDE smaller transition=fade>

	@@@ python
	from bottle import route, run

	@route('/hello/:name')
	def index(name='World'):
		return '<b>Hello %s!</b>' % name

	run(host='localhost', port=8080)

<!SLIDE bullets transition=fade>

# less talk more action

* pip install bottle
* mkdir teachme_api
* cd teachme_api