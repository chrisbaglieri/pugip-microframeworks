<!SLIDE center>

![web.py](webpy.jpg)

<!SLIDE bullets transition=fade>

# web.py at a high level

* source at [github.com/webpy/webpy](https://github.com/webpy/webpy)
* the readme on github is abysmal
* the site at [webpy.org](http://webpy.org) is so-so
* middle of the pack @ 10198 lines

<!SLIDE smaller transition=fade>

	@@@ python
	import web
	import view, config
	from view import render

	urls = (
		'/', 'index'
	)

	class index:
		def GET(self):
			return render.base(view.listing())

	if __name__ == "__main__":
		app = web.application(urls, globals())
		app.internalerror = web.debugerror
		app.run()

<!SLIDE bullets transition=fade>

# less talk more action

* pip install web.py
* mkdir teachme
* cd teachme