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
from flask_login import  (
    login_user,
    logout_user,
    current_user,
    login_required,
)
from markupsafe import Markup

from app import app, lm
from app.contentlib.contentlib import loadContents
from app.contentlib.menuItems import menuItems

from app.userspace.models import (
    User,
)
from app.userspace.forms import (
    LoginForm,
)
from app.userspace.dbtools import (
    dbGetUser,
    dbOpenDatabase,
)

import config

from app.utilityEndpoints import ep_paroliere

@app.before_request
def before_request():
    g.user = current_user

@lm.user_loader
def load_user(id):
    db=dbOpenDatabase(config.dbFullName)
    return dbGetUser(db,id)

def flashMessage(msgHeading,msgBody):
    '''
        Enqueues a flashed structured message for use by the render template
        
            'msgType' can be: critical, error, warning, info
    '''
    flash(Markup('<strong>%s: </strong> %s' % (escape(msgHeading),escape(msgBody))))

@app.route('/<int:hidemenu>')
@app.route('/')
@app.route('/index/<int:hidemenu>')
@app.route('/index')
@app.route('/index.html')
def ep_index(hidemenu=1):
    user=g.user
    return render_template(
        'index.html',
        hidemenu=bool(hidemenu),
        menuItems=menuItems,
        user=user,
    )

@app.route('/logout')
@login_required
def ep_logout():
    if g.user is not None and g.user.is_authenticated:
        flashMessage('Logged out','farewell')
        logout_user()
    return redirect(url_for('ep_index',hidemenu=0))        

@app.route('/login',methods=['GET','POST'])
def ep_login():
    user=g.user
    if user is not None and user.is_authenticated:
        return redirect(url_for('ep_index',hidemenu=0))
    form = LoginForm()
    if form.validate_on_submit():
        db=dbOpenDatabase(config.dbFullName)
        qUser=dbGetUser(db, form.username.data)
        if qUser and qUser.checkPassword(form.password.data):
            login_user(qUser)
            #
            flashMessage('Login successful', 'welcome, %s!' % (
                qUser.fullname,
            ))
            #
            return redirect(url_for('ep_index',hidemenu=0))
        else:
            flashMessage('Login error','invalid username or password')
            return redirect(url_for('ep_index',hidemenu=0))
    return render_template(
        'login.html', 
        hidemenu=False,
        menuItems=menuItems,
        form=form,
        user=user,
        contents={
            'title': 'Login',
            'subtitle': 'Enter the restricted area',
        },
    )

@app.route('/content/<fname>')
def ep_content(fname):
    user=g.user
    #
    jsonName='%s.json' % fname
    contentStruct=loadContents(
        config.CONTENTS_DESCRIPTOR_DIRECTORY,
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
        user=user,
        menuItems=menuItems,
    )

@app.route('/ubq')
def ep_webapp_ubq():
    return redirect('/ubq')

@app.route('/biblio')
def ep_webapp_biblio():
    return redirect('/biblio')
