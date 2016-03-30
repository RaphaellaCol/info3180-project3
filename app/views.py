"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/

This file creates your application.
"""

from app import app, db
from flask import render_template, request, redirect, url_for, session, flash, jsonify
from .forms import Additem, LoginForm
from app.models import User, Item

app.secret_key = "Info3180"
###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')

@app.route('/wishlist/')
def wishlist():
    return render_template('wishlist.html')
    
@app.route('/add/', methods=["GET","POST"])
def add():
    """Render the website's profile page to add profile."""
    form = Additem(request.form)

    if request.method == "POST" and form.validate_on_submit():
        print "oh yeah"
        url= request.form['url']
        title= request.form['title']
        description= request.form['description']
        item= Item(url=url, title=title, description=description)
        db.session.add(item)
        db.session.commit()
        print "yeah"
        return redirect(url_for('wishlist'))
    return render_template('add.html', form=form)
    
@app.route('/login/', methods=["GET","POST"])
def login():
    """Render the website's profile page to add profile."""
    form = LoginForm(request.form)

    if request.method == "POST" and form.validate_on_submit():
        print "oh yeah"
        username= request.form['username']
        password= request.form['password']
        print "yeah"
        return redirect(url_for('wishlist'))
    return render_template('login.html', form=form) 
    
@app.route('/signup/', methods=["GET","POST"])
def signup():
    """Render the website's profile page to add profile."""
    form = LoginForm(request.form)

    if request.method == "POST" and form.validate_on_submit():
        print "oh yeah"
        username= request.form['username']
        email= request.form['email']
        password= request.form['password']
        info= User(username=username, email=email,password=password)
        db.session.add(info)
        db.session.commit()
        print "yeah"
        return redirect(url_for('login'))
    return render_template('signup.html', form=form)  

###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8888")
