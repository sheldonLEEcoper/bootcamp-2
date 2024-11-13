from flask import Flask , render_template, request , url_for, redirect
from model import *
import os



current_dir = os.path.abspath(os.path.dirname(__file__))


app =Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.path.join(current_dir, 'data_base.sqlite3')

db.init_app(app)
app.app_context().push()


@app.route('/', methods=['GET', 'POST']) # http://127.0.0.1:5000/ = /
def home():
    if request.method == 'POST':
        
        form_email = request.form['Email']
        form_password = request.form['Password']

        check_user= user.query.filter_by(email=form_email).first()

        if check_user:
        
            if check_user.password == form_password:
                if check_user.user_type  =='admin':
                    return redirect(url_for('admin_dashbord'))
                elif check_user.user_type  =='enduser':
                    return redirect(url_for('user_dashbord'))
                elif check_user.user_type  =='artis':
                    check_status = artist.query.filter_by(artist_user_id=check_user.id).first()
                    
                    if check_status.status == False:
                        return "you are not verified"
                    else:
                        return redirect(url_for('artist_dashbord', id=check_user.id))
        else:
            return "User dosn\'t exists "
    





    return render_template('home.html')

@app.route('/user_dashbord', methods=['GET']) 
def user_dashbord():
    return render_template('page1.html')

@app.route('/artist_dashbord/<id>/', methods=['GET']) 
def artist_dashbord(id):
    user_details= user.query.filter_by(id=id).first()
    
    return render_template('page2.html' , username=user_details.username)


@app.route('/admin_dashbord', methods=['GET', 'POST']) 
def admin_dashbord():
    if request.method == "POST":
        form_id = request.form['id']
        form_status = request.form['status']

        artist_ = artist.query.filter_by(artist_user_id=form_id).first()
        if form_status == "T":
            artist_.status= True
            db.session.commit()


    data = artist.query.filter_by(status = False).all()

    return render_template('page3.html' , data=  data )


@app.route('/artist_signup', methods=['GET', 'POST']) 
def artist_signup():
    if request.method == 'POST':
        form_username = request.form['username']
        form_email = request.form['Email']
        form_password = request.form['Password']
      
        check_user= user.query.filter_by(email=form_email).first()

        if check_user:
            return "Email already in use please use a different email"
        else:
            new_data = user(username=form_username , email= form_email,  password= form_password, user_type = 'artis')
            db.session.add(new_data)
            db.session.commit()

            status = artist(artist_user_id=new_data.id)
            db.session.add(status)
            db.session.commit()

        return redirect(url_for('home'))
    return render_template('artist_signup.html')

@app.route('/signup_enduser', methods=['GET','POST']) 
def signup_enduser():
    if request.method == 'POST':
        form_username = request.form['username']
        form_email = request.form['Email']
        form_password = request.form['Password']
        form_type = request.form['type']
        

        new_data = user(username=form_username , email= form_email,  password= form_password, user_type =  form_type)
        db.session.add(new_data)
        db.session.commit()

        return redirect(url_for('home'))

    # get 
    # post - new data
    # put - updatin
    # delet 


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




