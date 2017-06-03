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
    return render_template(
        'index.html',
        showmenu=False,
    )

@app.route('/public')
def ep_public():
    return render_template(
        'itemlist.html',
        showmenu=True,
    )

@app.route('/ubq')
@app.route('/biblio')
def ep_webapp_placeholder():
    return jsonify({'temp':'should_point_to_webapp'})
