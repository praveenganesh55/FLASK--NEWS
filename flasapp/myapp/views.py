from myapp import app
from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from flask_mysqldb import MySQL
from passlib.hash import sha256_crypt
from newsapi import NewsApiClient
from .models import RegisterForm
@app.route('/')
def index():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

mysql=MySQL(app)
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        name = form.name.data
        email = form.email.data
        username = form.username.data
        password = sha256_crypt.encrypt(str(form.password.data))

        cur = mysql.connection.cursor()

        cur.execute("INSERT INTO users(name, email, username, password) VALUES( %s, %s, %s, %s)",
                    (name, email, username, password))

        mysql.connection.commit()

        cur.close()

        flash('REGISTERED SUCESSFULLY', 'success')

    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password_candidate = request.form['password']

        cur =mysql.connection.cursor()

        result = cur.execute("SELECT * FROM users WHERE username = %s", [username])

        if result > 0:
            data = cur.fetchone()
            password = data['password']

            if sha256_crypt.verify(password_candidate, password):
                app.logger.info('password matched')
                session['logged_in'] = True
                session['username'] = username

                flash('You are now logged in', 'success')
                return redirect(url_for('dashboard'))
            else:
                error = 'wrong password'
                return render_template('login.html', error=error)
            cur.close()
        else:
            error = 'username not found'
            return render_template('login.html', error=error)
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('you are now logged out','success')
    return redirect(url_for('login'))

@app.route('/dashboard')
def dashboard():
    newsapi = NewsApiClient(api_key='ead22b56ea9548bb962ea7a6806a3ba0')

    top_headlines = newsapi.get_top_headlines(sources='bbc-news,the-verge,abc-news,abc-news-au,aftenposten,al-jazeera-english,ansa,ars-technica,ary-news,associated-press')

    articles = top_headlines['articles']

    desc=[]
    news=[]
    img=[]
    link=[]

    for i in range(len(articles)):
        myarticle= articles[i]
        news.append(myarticle['title'])
        desc.append(myarticle['description'])
        img.append(myarticle['urlToImage'])
        link.append(myarticle['url'])

        mylist=zip(news,desc,img,link)
    return render_template('dashboard.html',context=mylist)

@app.route('/sports')
def sports():
    newsapi = NewsApiClient(api_key='ead22b56ea9548bb962ea7a6806a3ba0')

    top_headlines = newsapi.get_top_headlines(category='sports',language='en',country='in')

    articles = top_headlines['articles']

    desc = []
    news = []
    img = []
    link = []

    for i in range(len(articles)):
        myarticle = articles[i]
        news.append(myarticle['title'])
        desc.append(myarticle['description'])
        img.append(myarticle['urlToImage'])
        link.append(myarticle['url'])

        mylist = zip(news, desc, img, link)
    return render_template('all.html', context=mylist)

@app.route('/business')
def business():
    newsapi = NewsApiClient(api_key='ead22b56ea9548bb962ea7a6806a3ba0')

    top_headlines = newsapi.get_top_headlines(category='business',language='en',country='in')

    articles = top_headlines['articles']

    desc = []
    news = []
    img = []
    link = []

    for i in range(len(articles)):
        myarticle = articles[i]
        news.append(myarticle['title'])
        desc.append(myarticle['description'])
        img.append(myarticle['urlToImage'])
        link.append(myarticle['url'])

        mylist = zip(news, desc, img, link)
    return render_template('all.html', context=mylist)

@app.route('/entertainment')
def entertainment():
    newsapi = NewsApiClient(api_key='ead22b56ea9548bb962ea7a6806a3ba0')

    top_headlines = newsapi.get_top_headlines(category='entertainment',language='en',country='in')

    articles = top_headlines['articles']

    desc = []
    news = []
    img = []
    link = []

    for i in range(len(articles)):
        myarticle = articles[i]
        news.append(myarticle['title'])
        desc.append(myarticle['description'])
        img.append(myarticle['urlToImage'])
        link.append(myarticle['url'])

        mylist = zip(news, desc, img, link)
    return render_template('all.html', context=mylist)

@app.route('/technology')
def technology():
    newsapi = NewsApiClient(api_key='ead22b56ea9548bb962ea7a6806a3ba0')

    top_headlines = newsapi.get_top_headlines(category='technology',language='en',country='in')

    articles = top_headlines['articles']

    desc = []
    news = []
    img = []
    link = []

    for i in range(len(articles)):
        myarticle = articles[i]
        news.append(myarticle['title'])
        desc.append(myarticle['description'])
        img.append(myarticle['urlToImage'])
        link.append(myarticle['url'])

        mylist = zip(news, desc, img, link)
    return render_template('all.html', context=mylist)

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/search',methods=['POST'])
def result():
    text = request.form['u']
    newsapi = NewsApiClient(api_key='ead22b56ea9548bb962ea7a6806a3ba0')
    all_articles = newsapi.get_top_headlines(language='en')

    articles = all_articles["articles"]

    desc = []
    news = []
    img = []
    link = []

    count = 0
    for i in range(len(articles)):
        myarticle = articles[i]
        mystring = myarticle['description']
        if text in mystring :
            count=count+1
            news.append(myarticle['title'])
            desc.append(myarticle['description'])
            img.append(myarticle['urlToImage'])
            link.append(myarticle['url'])

            mylist=zip(news, desc, img, link)

            return render_template('all.html',context=mylist)
    if count<1:
        return render_template('result.html')