import requests

print ''
print 'All topics...'
response = requests.get('http://localhost:8080/topics')
print response.content
print ''

print ''
print 'Create a new topic...'
params = dict()
params['name'] = "Microframeworks"
params['description'] = "A whirlwind tour of Python's ecosystem of microframeworks"
params['presenter'] = "Chris Baglieri"
response = requests.post('http://localhost:8080/topics', params)
print response.content
print ''