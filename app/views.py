"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/

This file creates your application.
"""

from app import app, db
from flask import render_template, request, redirect, url_for, session, flash, json, jsonify
from .forms import Additem, LoginForm, Register
from app.models import User, Item
import requests
import BeautifulSoup
import urlparse
from passlib.hash import sha256_crypt



app.secret_key = "Info3180"


    
@app.route('/api/thumbnail/process/', methods=["GET"])
def imgs():    
    url = request.args.get('url')
    imagelist = []
    print url
    soup = BeautifulSoup.BeautifulSoup(requests.get(url).text)
    og_image = (soup.find('meta', property='og:image') or
                        soup.find('meta', attrs={'name': 'og:image'}))
                        
    if og_image and og_image['content']:
        print og_image['content']
    
    thumbnail_spec = soup.find('link', rel='image_src')
    if thumbnail_spec and thumbnail_spec['href']:
        print thumbnail_spec['href']
    
    def image_dem():
        # image = """<img src="%s">"""
        for img in soup.findAll("img"):
          if "sprite" not in img["src"]:
              imagelist.append(urlparse.urljoin(url,img['src']))
            #   imageitem = image % urlparse.urljoin(url, img["src"])
    
    image_dem()
    print imagelist
    if(len(imagelist)==0):
        response = jsonify({"error": "null", "data":{},"message":"Unable to extract thumbnails"})
    else:
        response = jsonify({"error": "1", "data":{"thumbnails":imagelist},"message":"Success"})  
    return response
    
"""return user wishlist"""
@app.route('/api/user/<userid>/wishlist/', methods=["GET"])
def api_wishlist(userid):

     if request.method =="GET":
        user = db.session.query(User).filter_by(id=userid).first()
        items = db.session.query(Item).filter_by(userid=user.id).all()
        itemlist = []
        for item in items:
            itemlist.append({'title':item.title,'url':item.url,'thumbnail':item.thumbnail,'description':item.description})
        if(len(itemlist)==0):
            response = jsonify({"error": "null", "data":{},"message":"Request failed"})
        else:
            response = jsonify({"error": "1", "data":{"items":itemlist},"message":"Success"})
            return response
     return render_template('wishlist.html', wishlist=items, userid=userid)
     
"""add items to wishlist"""   
@app.route('/user/<userid>/wishlist/new/', methods=["GET","POST"])
def wishlist_add(userid):
    form = Additem(request.form)
   
    if request.method == "POST":
        url= request.form['url']
        thumbnail = request.form['thumbnail']
        title= request.form['title']
        description= request.form['description']
        user = db.session.query(User).filter_by(id=userid).first()
        item= Item(url=url, thumbnail=thumbnail, title=title, description=description,userid=user.id)
        if item:
            db.session.add(item)
            db.session.commit()
            response = jsonify({"error": "null", 'data':{'url':url,'thumbnail':thumbnail,'title':title,'description':description,'user':userid},'message':'success'})
            return redirect(url_for('wishlist', userid=user.id))
        else:
            response = jsonify({"error": "1", 'data':{},'message':'Request failed'})
            return response
    return render_template('add.html', form=form, userid=userid)

@app.route('/user/<userid>/wishlist/', methods=["GET","POST"])
def wishlist(userid):
    if request.method =="GET":
        user = db.session.query(User).filter_by(id=userid).first()
        items = db.session.query(Item).filter_by(userid=user.id).all()

    return render_template('wishlist.html', wishlist=items, userid=userid) 

@app.route('/api/user/login/', methods=["GET","POST"])
def login():
    form = LoginForm(request.form)
    if request.method == "POST":
        email= request.form['email']
        password= request.form['password']
        user = db.session.query(User).filter_by(email=form.email.data, password=form.password.data).first()
        if user:
            response = jsonify({"error": "null", 'data':{'email':email,'password':password},'message':'logged in'})
            session['logged_in'] = True
            return redirect(url_for('wishlist', userid=user.id))
        else:
            response = jsonify({"error": "1", 'data':{},'message':'Error- Not logged in'})
            flash( 'Invalid credentials, try again') 
            return redirect(url_for('login'))
    return render_template('login.html', form=form) 
   
    
@app.route('/api/user/register/', methods=["GET",'POST'])
def register():
    form = Register(request.form)
    if request.method == 'POST':
        username= request.form['username']
        email= request.form['email']
        password=request.form['password']
        info= User(username=username, email=email, password=password)
        if info:
            db.session.add(info)
            db.session.commit()
            response = jsonify({"error": "null", 'data':{"username":username,"email":email,"password":password},'message':'Success'})
            return redirect(url_for('login'))
        else:
          response = jsonify({"error": "1", 'data':{},'message':'User already registered'})
          db.session.close()
          
    return render_template ('register.html', form=form)
       
        
@app.route('/api/user/logout/')
def logout():
      session.pop('logged_in', None)
      flash('You were logged out')
      return redirect(url_for('login'))
      
# @app.route('/api/send/<userid>', methods=["GET", "POST"])
# def send():
#     if request.method == "POST":
        # user = db.session.query(User).filter_by(id=userid).first()
#         Email= request.form['email']
#         Subject= request.form['subj']
#         Message =request.form['msg']
#         email(Name,Email,Subject,Message)
#     # return render_template('contact.html')

# def email(names,email,subj,msg):
#     fromname = names
#     toaddr = 'raphycol.info3180@gmail.com'
#     toname = 'Me'
#     fromaddr  = email
#     subject = subj
#     message = "From: {} <{}>\r\nTo: {}<{}>\r\nSubject : {}\r\n{}"
#     msg = msg
#     messagetosend = message.format(
#                                  fromname,
#                                  fromaddr,
#                                  toname,
#                                  toaddr,
#                                  subject,
#                                  msg)
    
#     # Credentials (if needed)
#     username = 'raphycol.info3180@gmail.com'
#     password = 'maehrmyaqvjrxutw'
    
#     # The actual mail send
#     server = smtplib.SMTP('smtp.gmail.com:587')
#     server.starttls()
#     server.login(username,password)
#     server.sendmail(fromaddr, toaddr, messagetosend)
#     server.quit()
                
     

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
