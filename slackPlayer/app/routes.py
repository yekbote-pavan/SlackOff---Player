from app import app
from string import Template
from flask import request

HTML_TEMPLATE = Template("""
      <h2>
        YouTube video link: 
        <a href="{youtube_link}">
        </a>
      </h2>
      <iframe src="${youtube_link}" width="853" height="480" frameborder="0" allowfullscreen></iframe>""")


@app.route('/', methods=['GET', 'POST', 'PUT'])
def index():
    if request.method == 'GET':
        return render_template('index.html', yt='request.args.get("yt")')