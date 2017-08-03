#!/usr/bin/python
def app(environ, start_response):
    data = ''
    for j in environ['QUERY_STRING'].split('&'):
        data = data + j + '\n'
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return [data]
