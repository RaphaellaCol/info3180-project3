"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/

This file creates your application.
"""

from app import app, db
from flask import render_template, request, redirect, url_for, session, flash, jsonify
from .forms import Additem, LoginForm, Register
from app.models import User, Item
import requests
import BeautifulSoup
import urlparse


app.secret_key = "Info3180"

def imgs(url):    
    url = "http://www.amazon.com/gp/product/1783551623"
    result = requests.get(url)
    soup = BeautifulSoup.BeautifulSoup(result.text)
    og_image = (soup.find('meta', property='og:image') or
                        soup.find('meta', attrs={'name': 'og:image'}))
                        
    if og_image and og_image['content']:
        print og_image['content']
    
    thumbnail_spec = soup.find('link', rel='image_src')
    if thumbnail_spec and thumbnail_spec['href']:
        print thumbnail_spec['href']
    
    def image_dem():
        image = """<img src="%s">"""
        for img in soup.findAll("img", src=True):
          if "sprite" not in img["src"]:
              print image % urlparse.urljoin(url, img["src"])
    
    image_dem()
    
@app.route('/api/thumbnail/process/', methods=["GET"])
def thumb_nail():
    url=request.form['url']
    return render_template('wishlist.html')    

@app.route('/api/wishlist/', methods=["GET"])
def wishlist():
    return render_template('wishlist.html')
   
# def img1(url):
#     pic = imgs ("http://" + url)[0]
#     if pic[0] == "/":
#         pic = "http://" + url + pic  #This creates a URL for the image
#     return "<img src=%s></img>" % pic  #Return the image in an HTML "img" tag
    
@app.route('/api/user/:id/wishlist/', methods=["GET","POST"])
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
     
         
@app.route('/api/user/login/', methods=["GET","POST"])
def login():
    """Render the website's profile page to add profile."""
    form = LoginForm(request.form)

    if request.method == "POST" and form.validate_on_submit():
        print "oh yeah"
        username= request.form['username']
        password= request.form['password']
        print "yeah"
        return redirect(url_for('register'))
    return render_template('login.html', form=form) 
    
@app.route('/api/user/register/', methods=["GET","POST"])
def register():
    """Render the website's profile page to add profile."""
    form = Register(request.form)

    if request.method == "POST" and form.validate_on_submit():
        print "oh yeah"
        username= request.form['username']
        email= request.form['email']
        password= request.form['password']
        info= User(username=username, email=email, password=password)
        db.session.add(info)
        db.session.commit()
        print "yeah"
       # return redirect(url_for('login'))
    return render_template('register.html', form=form)  

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
