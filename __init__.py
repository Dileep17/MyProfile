from flask import Flask, render_template
import yaml
import os.path

app = Flask(__name__)


@app.route('/')
def homepage():
    return "Hi there, how ya doin?"

@app.route('/search')
def home():
    return render_template('search.html')

@app.route('/about')
@app.route('/about/<name>')
def about(name=None):
    if name is not None and os.path.isfile('data/'+name+'.yaml'):
        profile = yaml.load(open('data/'+name+'.yaml', 'r'))
    else:
        profile = {}
    return render_template('profile_display.html', data=profile)



if __name__ == "__main__":
    app.run(debug=True)
