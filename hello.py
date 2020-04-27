def app(environ, start_response):
    """Returns splited QUERY_STRING"""
    data = []
    for i in environ['QUERY_STRING'].split('&'):
        i += '\n'
        data.append(bytes(i, 'utf8'))

    status = '200 OK'
    response_headers = [
        ('Content-type', 'text/plain')
    ]

    start_response(status, response_headers)
    return data