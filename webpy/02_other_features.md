<!SLIDE bullets transition=fade>

# what else?

* lightweight (thought not terribly pretty) templating engine

<!SLIDE smaller transition=fade>

	@@@ html
	$def with (name)

	$if name:
	    I just wanted to say <em>hello</em> to $name.
	$else:
	    <em>Hello</em>, world!