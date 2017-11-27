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
from app.contentlib.contentlib import loadContents
from app.contentlib.menuItems import menuItems

from config import CONTENTS_DESCRIPTOR_DIRECTORY

from app.utilityEndpoints import ep_paroliere

@app.route('/')
@app.route('/index.html')
def ep_index():
    return render_template(
        'index.html',
        hidemenu=True,
        menuItems=menuItems,
    )

@app.route('/content/<fname>')
def ep_content(fname):
    #
    jsonName='%s.json' % fname
    contentStruct=loadContents(
        CONTENTS_DESCRIPTOR_DIRECTORY,
        jsonName,
    )
    #
    if contentStruct=={}:
        contentStruct={
            'title': 'Empty folder',
            'subtitle': 'The requested resource is empty or non-existing.',
        }
    #
    return render_template(
        'itemlist.html',
        contents=contentStruct,
        hidemenu=False,
        menuItems=menuItems,
    )

@app.route('/ubq')
def ep_webapp_ubq():
    return redirect('/ubq')

@app.route('/biblio')
def ep_webapp_biblio():
    return redirect('/biblio')
