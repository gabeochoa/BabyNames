#!/usr/bin/env python
from flask import Flask, render_template, make_response, session, request, redirect, url_for
import os
import urllib
import base64
from urllib2 import Request, urlopen, URLError
import json 


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/research/<name>')
def res():
    return render_template('res.html')

@app.route("/simple.png")
def simple():
    import datetime
    import StringIO
    import random

    from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
    from matplotlib.figure import Figure
    from matplotlib.dates import DateFormatter

    fig=Figure()
    ax=fig.add_subplot(111)
    x=[]
    y=[]
    now=datetime.datetime.now()
    delta=datetime.timedelta(days=1)
    for i in range(10):
        x.append(now)
        now+=delta
        y.append(random.randint(0, 1000))
    ax.plot_date(x, y, '-')
    ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))
    fig.autofmt_xdate()
    canvas=FigureCanvas(fig)
    png_output = StringIO.StringIO()
    canvas.print_png(png_output)
    response=make_response(png_output.getvalue())
    response.headers['Content-Type'] = 'image/png'
    return response

port = int(os.environ.get('PORT', 5000))
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True,port=port)























