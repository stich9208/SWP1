
from cgi import parse_qs
from template import html

def application(environ, start_response):
	q = parse_qs(environ['QUERY_STRING'])
	a = q.get('a', [''])[0]
	b = q.get('b', [''])[0]
	plus, time = 0, 0	

	try:
		a, b = int(a), int(b)	
		plus = a + b
		time = a * b

	except ValueError:
		plus = - 1
		time = - 1	
	
	response_body = html % {'plus':plus, 'time':time}
	start_response('200 OK', [
		('Content-Type', 'text/html'),
		('Content-Length', str(len(response_body)))
	])
	
	return [response_body]  
