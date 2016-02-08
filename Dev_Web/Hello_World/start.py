from bottle import route, run, view, request, static_file


@route('/static/<filename:path>')
def server_static(filename):
    return static_file(filename, root='./static')


@route('/hello', method='get')
@view('static/template/hello')
def hello():
    if request.query.name == '':
        request.query.name = 'GLMF'

    values = {
      'title' : 'Test de Bottle',
      'name'  : request.query.name
    }
    return values

run(host='localhost', port=8080, debug=True)
