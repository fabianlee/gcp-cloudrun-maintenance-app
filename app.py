import flask
import main


app = flask.Flask(__name__)

@app.route('/json')
def show_json():
    return main.show_json(flask.request)

# catch-all
@app.route('/', defaults={'path':''})
@app.route('/<path:path>')
def show_default(path):
    return main.show_html(flask.request)

if __name__ == '__main__':
    app.run(host='0.0.0.0')

