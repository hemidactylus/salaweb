from flask import (
    render_template,
    flash,
    redirect,
    session,
    url_for,
    request,
    g,
    abort,
    escape,
    make_response,
    jsonify,
)

from app import app, lm

@app.route('/')
@app.route('/index.html')
def ep_index():
    return render_template('index.html')

@app.route('/a.html')
def ep_test_ep():
    return jsonify({'ciao':"pirla"})

