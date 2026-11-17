#почитать историю создания nginx
#Fast CGI
#WSGI(Web Server Gateway Interface)
#МВЦ Model View Controller
#Прочитать про вэбсерверы -Django, -ganicorn, -uWSGI
#проблема с 10к
#прочитать про состояние гонки

from wsgiref.simple_server import make_server

def app(environ, start_response):
    status = '200 OK'
    headers = [
        ('Content-Type', 'text/plain; charset=utf-8'),
    ]
    start_response(status, headers)
    return [b'hello_world']

if __name__ == '__main__':
    with make_server('', 8000, app) as httpd:
        print("Сервер запущен на http://localhost:8000")
        httpd.serve_forever()