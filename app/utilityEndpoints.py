'''
    utilityEndpoints.py
'''

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

from app.contentlib.menuItems import menuItems
from app.utils.paroliere import deal

@app.route('/paroliere')
def ep_paroliere():
    user=g.user
    letters=[
        let if let!='Q' else 'Qu'
        for let in deal()
    ]
    letpack=[
        letters[i*4:(i+1)*4]
        for i in range(0,4)
    ]
    return render_template(
        'paroliere.html',
        title='Paroliere',
        caption='Play with this!',
        letpack=letpack,
        hidemenu=False,
        menuItems=menuItems,
        user=user,
        contents={
            'title': 'Paroliere',
            'subtitle': 'Gioca a Paroliere online',
        },
    )
