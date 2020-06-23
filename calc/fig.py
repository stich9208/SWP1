
from cgi import parse_qs
from template import html

def application(environ, start_response):
	q = parse_qs(environ['QUERY_STRING'])
	a = q.get('a', [''])[0]
	b = q.get('b', [''])[0]
	
	plus = q.get('plus', [''])[0]	
	time = q.get('time', [''])[0]	

	if '' not in[a, b]:
		a, b = int(a), int(b)	
		plus = a + b
		time = a * b

	
	response_body = html 
	start_response('200 OK', [
		('Content-Type', 'text/html'),
		('Content-Length', str(len(response_body)))
	])
	
	return [response_body]  
