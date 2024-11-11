from flask import Flask , render_template, request , url_for, redirect
from model import *
import os



current_dir = os.path.abspath(os.path.dirname(__file__))


app =Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.path.join(current_dir, 'data_base.sqlite3')

db.init_app(app)
app.app_context().push()


@app.route('/', methods=['GET']) # http://127.0.0.1:5000/ = /
def home():
    return render_template('home.html')

@app.route('/page1', methods=['GET']) 
def page1():
    return render_template('page1.html')

@app.route('/page2', methods=['GET']) 
def page2():
    return render_template('page2.html')

@app.route('/page3', methods=['GET']) 
def page3():
    return render_template('page3.html')

@app.route('/signup_enduser', methods=['GET','POST']) 
def signup_enduser():
    if request.method == 'POST':
        form_username = request.form['username']
        form_email = request.form['Email']
        form_password = request.form['Password']
        form_type = request.form['type']
        

        print('''




''')
        print( form_username)
        print(form_password)
        print(form_email)
        print('''




        ''')  

        new_data = user(username=form_username , email= form_email,  password= form_password, user_type =  form_type)
        db.session.add(new_data)
        db.session.commit()

        return redirect(url_for('home'))




    return render_template('usersignup.html')


@app.route('/demoquery', methods=['GET'])
def demo():
    print('''
          
          
          
          
          
          
          ''')
    # data = user.query.all()
    # for i in data:
    #     print(i.username, i.user_type)

#     data = user.query.filter_by(user_type = 'artis').all()
#     for i in data:
#         print(i.username, i.user_type)
    
#     print(''' 
# difference between all and first 

# ''')
#     data2 = user.query.filter_by(user_type = 'artis').first()
#     print(data2.username , data2.user_type)

#     print('''
          
          
          
          
          
          
#           ''')

    # query= 'S%'
    # data = user.query.filter(user.username.like(query)).all()
    # for i in data:
    #     print(i.username)



    #add data to data base:

    new_data = user(username=' vipin ', email= 'vp1@email.com',  password= 1234, user_type = 'enduser')
    db.session.add(new_data)
    db.session.commit()


    return "look in to the vs code terminal for results "



if __name__ == "__main__":
    db.create_all()
    app.debug = True
    app.run()