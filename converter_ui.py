from string import ascii_letters
from random import choice, randint
import webview
import dominate
import converter
from dominate.tags import *
from bottle import route, run, template

bootstrap = 'https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/'
bootswatch = 'https://maxcdn.bootstrapcdn.com/bootswatch/3.3.6/'

doc = dominate.document()

with doc.head:
    link(rel='stylesheet',
        href=bootstrap + 'css/bootstrap.min.css')
    link(rel='stylesheet',
        href=bootswatch + 'paper/bootstrap.min.css')
script(src='https://code.jquery.com/jquery-2.1.1.min.js')
[script(src=bootstrap + 'js/' + x)
    for x in ['bootstrap.min.js', 'bootstrap-dropdown.js']]


@route('/')
def root():
    word = lambda: ''.join(
        choice(ascii_letters) for i in range(randint(2, 10)))
    nih_lorem = ' '.join(word() for i in range(50))
    _html = html()
    _head, _body = _html.add(head(title('Simple Document Tree')), body())
    names = ['header', 'content', 'footer']
    header = _body.add(div(id=names[0]))
    _button = _body.add(button('Evaluate', cls='btn btn-primary', onclick='self.location.href="http://localhost:8080/myFunction"'))
    print(_html)
    return  template(str(_html))

@route('/myFunction')
def myFunction():
    print 'button click'
    image = converter.import_image('sample_images/isaax.jpg')
    ascii_image = converter.do_convert(image, int(120), 127, int(0), '.')
    print ascii_image
    _html = html()
    _head, _body = _html.add(head(title('Simple Document Tree')), body())
    header = _body.add(div(id='header'))
    #for line in ascii_image.split('\n'):
    _body.add(pre(ascii_image))
    print _html
    return template(str(_html))

if __name__ == '__main__':
    import threading
    thread = threading.Thread(target=run, kwargs=dict(host='localhost', port=8080))
    thread.start()
    webview.create_window("Not a browser, honest!", "http://localhost:8080", width=800, height=600, resizable=True)