import sys
import requests

print ''
print "Getting topic %s" % sys.argv[1] + "..."
response = requests.get("http://localhost:8080/topics/%s" % sys.argv[1])
print response.content
print ''

print ''
print "Updating topic %s" % sys.argv[1] + "..."
params = dict()
params['name'] = "Microframeworks"
params['description'] = "A whirlwind tour of Python's ecosystem of microframeworks"
params['presenter'] = "Bags"
response = requests.put("http://localhost:8080/topics/%s" % sys.argv[1], params)
print response.content
print ''