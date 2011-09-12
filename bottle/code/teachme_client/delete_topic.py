import sys
import requests

print ''
print "Getting topic %s" % sys.argv[1] + "..."
response = requests.get("http://localhost:8080/topics/%s" % sys.argv[1])
print response.content
print ''

print ''
print "Deleting topic %s" % sys.argv[1] + "..."
response = requests.delete("http://localhost:8080/topics/%s" % sys.argv[1])
print response.content
print ''

print ''
print "Getting topic %s" % sys.argv[1] + "..."
response = requests.get("http://localhost:8080/topics/%s" % sys.argv[1])
print response.content
print ''