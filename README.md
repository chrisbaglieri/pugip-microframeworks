Princeton Python User Group Talk On Microframeworks
===================================================

This is a [showoff](http://github.com/schacon/showoff) presentation I shared with the Princeton Python User Group surveying a subset of the more popular microframeworks out there. You can view this presentation by installing the showoff gem (how devilish of me to force you to install ruby code to watch a presentation on Python microframeworks), cloning the repo, diving into the repo directory, issuing the command 'showoff serve', and opening [localhost:9090](http://localhost:9090) in your browser.

    $ gem install showoff
    $ git clone git://github.com/chrisbaglieri/pugip-microframeworks.git
    $ cd pugip-microframeworks
    $ showoff serve

Overview
--------

Given the varying levels of experience in the room, I start off grossly defining microframeworks and more importantly what they are not. From there, I dive in and cover [Flask](http://flask.pocoo.org), [Bottle](http://bottlepy.org), [web.py](http://webpy.org), and [cherry.py](http://cherrypy.org). Along the way I make note of other less popular but equally notable microframeworks, namely [Pesto](http://www.ollycope.com/software/pesto/), [Bobo](bobo.digicool.com), [itty](https://github.com/toastdriven/itty), and [aspen.io](http://aspen.io/). In each of the framework dedicated folders, you'll find markup for the showoff presentation as well as a basic implementation of an application or api using said framework.

Code
----

If you're interested in running any of the code examples, beyond installing the actual framework as described in the presentation, you'll need to install [MongoDB](http://mongodb.org) (brew install mongo if you're on OSX and use homebrew) and [MongoKit](http://namlook.github.com/mongokit/) (easy_install/pip install mongokit) which I employ in every example.