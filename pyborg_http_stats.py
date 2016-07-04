import bottle
import baker
from bottle import request
from pyborg.pyborg import pyborg

our_pyborg = pyborg()


@bottle.route("/")
def index():
    msg = "<h1>Welcome to Pyborg Stats!</h1>\n"
    try:
        msg += "pyborg words = " + `our_pyborg.settings.num_words`
    except Exception as e:
        msg += str(e)
    return msg


if __name__ == '__main__':
    bottle.run(host="0.0.0.0", port=8085, reloader=True)
#    our_pyborg.save_all()
