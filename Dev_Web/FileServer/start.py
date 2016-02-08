from bottle import route, run, view, request, static_file, error

@route('/static/<filename:path>')
def server_static(filename):
    return static_file(filename, root='./static')

@route('/giveme', method='get')
def sendFile():
    return static_file(request.query.key + '.wav', root='./files')

@error(404)
@view('static/template/404')
def error404(error):
    return None

run(host='localhost', port=8080, debug=True)
