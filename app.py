from flask import Flask,render_template,session,request,redirect,url_for
from DBConnection import Db
app = Flask(__name__)
app.secret_key ="mech"
static_path="C:\\Users\\ajmal\\PycharmProjects\\mechfinder\\static\\"


@app.route('/')
def hello_world():
    return render_template('login.html')
@app.route('/login_check' ,methods=['post'])
def login_check():
    username=request.form['Username']
    password=request.form['password']
    db=Db()
    res=db.selectOne("SELECT * FROM login WHERE username='"+username+"' AND PASSWORD='"+password+"'")
    if res is not None:
        session['lid'] = res['login_id']
        user_type=res['user_type']
        if user_type=='admin':
            return redirect(url_for('admin_home'))
        elif user_type=='owner':
            return redirect(url_for('owner_home'))
        else:
            return '<script>alert("invalid username or password");window.location="/"</script>'
    else:
        return '<script>alert("invalid username or password");window.location="/"</script>'


@app.route('/singup')
def singup():
    return render_template('owner/signup.html')
@app.route('/sinup_post',methods=['post'])
def sinup_post():

    shop_name = request.form['textfield5']
    place = request.form['textfield2']
    city = request.form['textfield3']
    district = request.form['textfield4']
    pincode = request.form['number']
    emial = request.form['email']
    files = request.files['file']
    Phone = request.form['number2']
    latitude = request.form['latitude']
    longitude = request.form['longitude']
    password = request.form['password']
    db =Db()
    lid=db.insert("INSERT INTO login(username,PASSWORD,user_type) VALUE ('"+emial+"','"+password+"','pending')")
    login_id = str(lid)
    res=db.insert("INSERT INTO workshop(login_id,shop_name,place,city,district,pincode,email,shop_lisence,phone,lati,longi) VALUES ('"+login_id+"','"+shop_name+"','"+place+"','"+city+"','"+district+"','"+pincode+"','"+emial+"','','"+Phone+"','"+latitude+"','"+longitude+"')")


    file_name = 'worckshop_' + str(res) + '.jpg'
    files.save(static_path + "worckshop\\" + file_name)
    db.update("update workshop set shop_lisence='" + file_name + "' where shop_id='" + str(res) + "'")
    return '<script>alert("DONE");window.location="/"</script>'


###################admin###################

@app.route('/admin_home')
def admin_home():
    return render_template('admin/admin_home.html')

@app.route('/view_pending_workshop')
def view_pending_workshop():
    db =Db()
    res=db.select("SELECT `workshop`.*,`login`.username FROM `workshop`,`login` WHERE `workshop`.shop_id=`login`.login_id AND user_type='pending'")
    return render_template('admin/view_pending_workshop.html',data=res)

@app.route('/view_approved_workshop')
def view_approved_workshop():
    return render_template('admin/view_approved_workshop.html')

@app.route('/view_rejected_workshop')
def view_rejected_workshop():
    return render_template('admin/rejected_workshop.html')

@app.route('/Manage_complaints')
def Manage_complaints():
    return render_template('admin/view_complaints.html')

@app.route('/View_feedback')
def View_feedback():
    return render_template('admin/view_feedback.html')

@app.route('/View_rating')
def View_rating():
    return render_template('admin/view rating.html')

@app.route('/Add_Notification')
def Add_Notification():
    return render_template('admin/add_Notification.html')
@app.route('/Add_Notification_post',methods=['post'])
def Add_Notification_post():
    subject=request.form['textfield']
    content=request.form['textarea']
    files=request.files['fileField']
    db=Db()
    res=db.insert("INSERT INTO notification(DATE,SUBJECT,description,image) VALUES (CURDATE(),'"+subject+"','"+content+"','')")
    file_name='notification_'+str(res)+'.jpg'
    files.save(static_path+"notification\\"+file_name)
    db.update("update notification set image='"+file_name+"' where notification_id='"+str(res)+"'")
    return '<script>alert("notification adedd");window.location="/Add_Notification"</script>'

@app.route('/View_Notification')
def View_Notification():
    db=Db()
    res=db.select("SELECT * FROM notification ORDER BY notification.notification_id DESC")
    return render_template('admin/view_Notification.html',data=res)

@app.route('/Add_news')
def Add_news():
    return render_template('admin/add news.html')

@app.route('/Add_news_post',methods=['post'])
def Add_news_post():
    title=request.form['textfield']
    discription=request.form['textarea']
    files = request.files['fileField']
    db = Db()
    res = db.insert("INSERT INTO news(DATE,news_title,news_description,image) VALUES (CURDATE(),'"+title+"','"+discription+"','')")
    file_name = 'news_' + str(res) + '.jpg'
    files.save(static_path + "news\\" + file_name)
    db.update("update news set image='" + file_name + "' where news_id='" + str(res) + "'")
    return '<script>alert("news added");window.location="/Add_news"</script>'

@app.route('/view_news')
def view_news():
    db=Db()
    res=db.select("SELECT * FROM news ORDER BY news.news_id DESC")
    return render_template('admin/view news.html',data=res)

@app.route('/change_password')
def change_password():
    return render_template('admin/change_password.html')


###############owner###############
@app.route('/owner_home')
def owner_home():
    return render_template('owner/owner_home.html')

@app.route('/view_profile')
def view_profile():
    return render_template('owner/view profile.html')

@app.route('/change_owner_password')
def change_owner_password():
    return render_template('owner/change_owner_password.html')

@app.route('/gallery_management')
def gallery_management():
    return render_template('owner/gallery_management.html')

@app.route('/add_photo')
def add_photo():
    return render_template('owner/add_photo.html')

@app.route('/add_photo_post',methods=['post'])
def add_photo_post():
    files = request.files['file']
    shop_id = str(session['lid'])
    db = Db()
    res = db.insert("INSERT INTO gallery(shop_id,image,DATE) VALUES ('"+shop_id+"','',CURDATE())")

    file_name = 'gallery_' + str(res) + '.jpg'
    files.save(static_path + "gallery\\" + file_name)
    db.update("update gallery set image='" + file_name + "' where gallery_id='" + str(res) + "'")
    return '<script>alert("photo added");window.location="/add_photo"</script>'

@app.route('/view_services')
def view_services():
    return render_template('owner/view service.html')

@app.route('/add_services')
def add_services():
    return render_template('owner/add_service.html')

@app.route('/add_services_post',methods=['post'])
def add_services_post():
    shop_id = str(session['lid'])
    service = request.form.get('filed')
    Vehicle_type = request.form.get('service')
    price = request.form['price']

    db = Db()
    res = db.insert("INSERT INTO services(shop_id,service,vehichle_type,amount) VALUES('"+shop_id+"','"+service+"','"+Vehicle_type+"','"+price+"')")


    return '<script>alert("service added");window.location="/add_services"</script>'


@app.route('/pending_service_requestes')
def pending_service_requestes():
    return render_template('owner/view pending requests.html')

@app.route('/approved_service_requestes')
def approved_service_requestes():
    return render_template('owner/view approved service requests.html')

@app.route('/service_request_history')
def service_request_history():
    return render_template('owner/view service requests history.html')

@app.route('/view_rating')
def view_rating():
    return render_template('owner/view rating.html')



if __name__ == '__main__':
    app.run()
