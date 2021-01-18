from flask import Flask,render_template,session,request,redirect,url_for
from flask_mail import Mail, Message
import demjson
from DBConnection import Db
app = Flask(__name__)
app.secret_key ="mech"
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'mechfinder4@gmail.com'  # enter your email here
app.config['MAIL_DEFAULT_SENDER'] = 'mechfinder4@gmail.com' # enter your email here
app.config['MAIL_PASSWORD'] = 'mech1234' # enter your password here
mail = Mail(app)
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

@app.route('/forgot_password')
def forgot_password():
    return render_template('forgot_password.html')

@app.route('/forgot_password_post',methods=['post'])
def forgot_password_post():
    email = request.form['mail']
    db =Db()
    res = db.selectOne("SELECT * FROM login WHERE username='"+email+"'")
    if res is not None:
        msg = Message(subject="My Password",
                      sender=app.config.get("mechfinder4@gmail.com"),
                      recipients=[email],
                      body="account password " + res['password'])
        mail.send(msg)
        return '<script>alert("password send sussfuly");window.location="/"</script>'

    else:
        return '<script>alert("Check your email");window.location="/forgot_password"</script>'
    return 'ok'


###################admin###################

@app.route('/admin_home')
def admin_home():
    return render_template('admin/admin_home.html')

@app.route('/view_pending_workshop')
def view_pending_workshop():
    db =Db()
    res=db.select("SELECT workshop.* FROM login,workshop WHERE login.user_type='pending' AND login.login_id=workshop.login_id ")
    return render_template('admin/view_pending_workshop.html',data=res)

@app.route('/searcch_pending_workshop',methods=['post'])
def searcch_pending_workshop():
    search = request.form['search']

    db = Db()
    res = db.select("SELECT workshop.* FROM login,workshop WHERE login.user_type='pending' AND login.login_id=workshop.login_id AND (shop_name like '%"+search+"%' or place like '%"+search+"%')")
    return render_template('admin/view_pending_workshop.html', data=res)


@app.route('/approve_workshop/<wid>')
def approve_workshop(wid):
    db=Db()
    res=db.selectOne("SELECT workshop.* FROM workshop WHERE  workshop.login_id='"+wid+"'")
    session['wlid']=wid
    return render_template('admin/approve_worckshop.html',data=res)




@app.route('/approve_workshop_post',methods=['post'])
def approve_workshop_post():
    db = Db()
    wid=session['wlid']
    db.update("UPDATE login SET user_type='owner' WHERE login_id='"+wid+"'")
    return '<script>alert("successfully approved");window.location="/view_pending_workshop"</script>'


@app.route('/view_approved_workshop')
def view_approved_workshop():
    db = Db()
    res = db.select(
        "SELECT workshop.* FROM login,workshop WHERE login.user_type='owner' AND login.login_id=workshop.login_id ")
    return render_template('admin/view_approved_workshop.html',data=res)

@app.route('/search_approved_workshop',methods=['post'])
def search_approved_workshop():
    search = request.form['search']
    db = Db()
    res = db.select("SELECT workshop.* FROM login,workshop WHERE login.user_type='owner' AND login.login_id=workshop.login_id  AND (shop_name like '%"+search+"%' or place like '%"+search+"%')")
    return render_template('admin/view_approved_workshop.html', data=res)


@app.route('/more_info/<wid>')
def more_info(wid):
    db = Db()
    res=db.selectOne("SELECT workshop.* FROM workshop WHERE  workshop.login_id='"+wid+"' ")
    res2=db.select("SELECT * FROM services WHERE shop_id='"+wid+"'")
    session['ad']=wid
    return  render_template('admin/more_info.html',data=res,data2=res2)

@app.route('/block_workshop',methods=['post'])
def block_workshop():
    wid=session['ad']
    db =Db()
    db.update("UPDATE login SET user_type='rejected' WHERE login_id='"+wid+"'")
    return '<script>alert("successfully rejected");window.location="/view_approved_workshop"</script>'




@app.route('/view_rejected_workshop')
def view_rejected_workshop():
    db = Db()
    res = db.select(
        "SELECT workshop.* FROM login,workshop WHERE login.user_type='rejected' AND login.login_id=workshop.login_id ")
    return render_template('admin/rejected_workshop.html',data=res)

@app.route('/search_rejected_workshop',methods=['post'])
def search_rejected_workshop():
    search = request.form['search']
    db = Db()
    res = db.select("SELECT workshop.* FROM login,workshop WHERE login.user_type='rejected' AND login.login_id=workshop.login_id AND (shop_name like '%"+search+"%' or place like '%"+search+"%')")
    return render_template('admin/rejected_workshop.html', data=res)

@app.route('/verify_reject/<wid>')
def verify_reject(wid):
    db = Db()
    res = db.selectOne("SELECT workshop.* FROM workshop WHERE  workshop.login_id='" + wid + "' ")
    res2 = db.select("SELECT * FROM services WHERE shop_id='" + wid + "'")
    session['ad'] = wid
    return render_template('admin/verify_reject.html', data=res, data2=res2)



@app.route('/approve_rejected_workshop',methods=['post'])
def approve_rejected_workshop():
    wid = session['ad']
    db = Db()
    db.update("UPDATE login SET user_type='owner' WHERE login_id='" + wid + "'")
    return '<script>alert("successfully approved");window.location="/view_rejected_workshop"</script>'


@app.route('/delete_rejected_workshop/<qid>')
def delete_rejected_workshop(qid):
    db = Db()
    db.delete("DELETE FROM login WHERE login_id='"+qid+"'")
    db.delete("DELETE FROM workshop WHERE login_id='"+qid+"'")
    return '<script>alert("successfully deleted");window.location="/view_rejected_workshop"</script>'

@app.route('/Manage_complaints')
def Manage_complaints():
    db = Db()
    res=db.select("SELECT complaint.*,user.name FROM complaint,USER WHERE complaint.user_id=user.login_id ORDER BY complaint.complaint_id DESC")
    return render_template('admin/view_complaints.html',data=res)

@app.route('/search_complaints',methods=['post'])
def search_complaints():
    search = request.form['search']
    db = Db()
    res = db.select(
        "SELECT complaint.*,user.name FROM complaint,USER WHERE complaint.user_id=user.login_id AND (name like '%"+search+"%' or complaint like '%"+search+"%')")
    return render_template('admin/view_complaints.html', data=res)


@app.route('/send_reply/<cid>')
def send_reply(cid):
    
    session['id']=cid
    return render_template('admin/send reply.html')

@app.route('/send_reply_post',methods=['post'])
def send_replay():
    reply=request.form['reply']
    cid=session['id']
    db = Db()
    db.update("UPDATE complaint SET replay='"+reply+"',replay_date=CURDATE() WHERE complaint_id='"+cid+"'")
    return '<script>alert("successfully sent");window.location="/Manage_complaints"</script>'


@app.route('/View_feedback')
def View_feedback():
    db = Db()
    res=db.select("SELECT feedback.*,user.name FROM USER,feedback  WHERE feedback.user_id=user.user_id ORDER BY feedback.feedback_id DESC")
    return render_template('admin/view_feedback.html',data=res)

@app.route('/search_feedback',methods=['post'])
def search_feedback():
    search = request.form['search']
    db = Db()
    res = db.select(
        "SELECT feedback.*,user.name FROM USER,feedback  WHERE feedback.user_id=user.user_id AND (name like '%"+search+"%' or feedback like '%"+search+"%')")
    return render_template('admin/view_feedback.html', data=res)



@app.route('/View_rating')
def View_rating():
    db =Db()
    res=db.select("SELECT rating.*,workshop.shop_name,user.name FROM rating,workshop,USER,service_request WHERE rating.service_request_id=service_request.service_request_id AND service_request.user_id=user.login_id AND service_request.workshop_id=workshop.login_id ORDER BY rating.rating_id DESC")
    return render_template('admin/view rating.html',data=res)

@app.route('/search_rating',methods=['post'])
def search_rating():
    search = request.form['search']
    db = Db()
    res = db.select(
        "SELECT rating.*,workshop.shop_name,user.name FROM rating,workshop,USER,service_request WHERE rating.service_request_id=service_request.service_request_id AND service_request.user_id=user.login_id AND service_request.workshop_id=workshop.login_id AND (name like '%"+search+"%' or shop_name like '%"+search+"%' or rating like '%"+search+"%')")
    return render_template('admin/view rating.html', data=res)

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
    res=db.select("SELECT * FROM notification ORDER BY notification.notification_id desc ")
    return render_template('admin/view_Notification.html',data=res)

@app.route('/search_notification',methods=['post'])
def search_notification():
    search = request.form['search']
    db = Db()
    res = db.select("SELECT * FROM notification WHERE (subject like '%"+search+"%' or date like '%"+search+"%') ")
    return render_template('admin/view_Notification.html', data=res)


@app.route('/delete_notification/<nid>')
def delete_notification(nid):
    db =Db()
    db.delete("DELETE FROM notification WHERE notification_id='"+nid+"'")
    import os
    file_name = "notification_"+nid+".jpg"
    os.remove(static_path + "notification\\" + file_name)
    return '<script>alert("notification deleted");window.location="/View_Notification"</script>'

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
    res=db.select("SELECT * FROM news ORDER BY news.news_id desc ")
    return render_template('admin/view news.html',data=res)

@app.route('/search_news',methods=['post'])
def search_news():
    search = request.form['search']
    db = Db()
    res = db.select("SELECT * FROM news WHERE (date like '%"+search+"%' or news_title like '%"+search+"%' ) ")
    return render_template('admin/view news.html', data=res)


@app.route('/edit_news/<nid>')
def edit_news(nid):
    db=Db()
    res=db.selectOne("SELECT * FROM news WHERE news_id='"+nid+"'")
    session['neid']=nid
    return render_template('admin/edit news.html',data=res)

@app.route('/edit_news_post',methods=['post'])
def edit_news_post():
    title = request.form['textfield']
    discription = request.form['textarea']
    files = request.files['fileField']
    nid = session['neid']
    if files is not None:
        fn=files.filename
        if fn != '':
            file_name = 'news_' + str(nid) + '.jpg'
            files.save(static_path + "news\\" + file_name)
    db = Db()

    db.update("UPDATE news SET DATE=CURDATE(),news_title='"+title+"',news_description='"+discription+"' WHERE news_id='"+nid+"'")
    return '<script>alert("successfully updated");window.location="/view_news"</script>'

@app.route('/delete_news/<neid>')
def delete_news(neid):
    db =Db()
    db.delete("DELETE FROM news WHERE news_id='"+neid+"'")
    import os
    file_name = "news_"+neid+".jpg"
    os.remove(static_path + "news\\" + file_name)
    return '<script>alert("successfully deleted");window.location="/view_news"</script>'


@app.route('/change_password')
def change_password():
    return render_template('admin/change_password.html')

@app.route('/change_password_post',methods=['post'])
def change_password_post():
    cr_pass=request.form['password']
    new_pass=request.form['password2']
    lid = str(session['lid'])
    db =Db()
    res = db.selectOne("SELECT * FROM login WHERE login_id='" + lid + "' AND password='" + cr_pass + "'")
    if res is not None:
        db.update("UPDATE login SET password='" + new_pass + "' WHERE login_id='" + lid + "'")
        return '<script>alert("successfully updated");window.location="/"</script>'
    else:
        return '<script>alert("invalid current password");window.location="/change_password"</script>'

@app.route('/logout_admin')
def logout_admin():
    session.pop('lid')
    return redirect(url_for('hello_world'))

###############owner###############
@app.route('/owner_home')
def owner_home():
    return render_template('owner/owner_home.html')

@app.route('/view_profile')
def view_profile():
    db = Db()
    lid =str(session['lid'])
    res=db.selectOne("SELECT * FROM  workshop WHERE login_id='"+lid+"'")
    return render_template('owner/view profile.html',data=res)

@app.route('/update_view_profile/',methods=['post'])
def update_view_profile():
    shop_name = request.form['textfield5']
    place = request.form['textfield2']
    city = request.form['textfield3']
    district = request.form['textfield4']
    pincode = request.form['number']
    emial = request.form['email']
    files = request.files['file']
    phone = request.form['number2']
    latitude = request.form['latitude']
    longitude = request.form['longitude']
    lid = str(session['lid'])
    if files is not None:
        fn=files.filename
        if fn != '':
            file_name = 'worckshop_' + str(lid) + '.jpg'
            files.save(static_path + "worckshop\\" + file_name)
    db =Db()

    db.update("UPDATE  workshop SET shop_name='"+shop_name+"',place='"+place+"',city='"+city+"',district='"+district+"',pincode='"+pincode+"',email='"+emial+"',phone='"+phone+"',lati='"+latitude+"',longi='"+longitude+"' WHERE login_id='"+lid+"'")
    db.update("UPDATE login SET username='"+emial+"' WHERE login_id='"+lid+"'")
    return '<script>alert("updated successfully");window.location="/view_profile"</script>'


@app.route('/change_owner_password')
def change_owner_password():
    return render_template('owner/change_owner_password.html')
@app.route('/change_owner_password_post',methods=['post'])
def change_owner_password_post():
    cr_pass=request.form['password']
    new_pass=request.form['password2']
    lid = str(session['lid'])
    db =Db()
    res = db.selectOne("SELECT * FROM login WHERE login_id='" + lid + "' AND password='" + cr_pass + "'")
    if res is not None:
        db.update("UPDATE login SET password='" + new_pass + "' WHERE login_id='" + lid + "'")
        return '<script>alert("successfully updated");window.location="/"</script>'
    else:
        return '<script>alert("invalid current password");window.location="/change_owner_password"</script>'


@app.route('/gallery_management')
def gallery_management():
    db =Db()
    lid = str(session['lid'])
    res=db.select("SELECT * FROM gallery WHERE shop_id='"+lid+"'")
    lent=len(res)
    for_loop=0
    if lent>0:
        for_loop=int(lent/3)
        if lent%3!=0:
            for_loop=for_loop+1
    return render_template('owner/gallery_management.html',data=res,lp=for_loop)

@app.route('/gallery_delete/<id>')
def gallery_delete(id):
    db = Db()
    db.delete("DELETE FROM gallery WHERE gallery_id='"+id+"'")
    import os
    file_name="gallery_"+id+".jpg"
    os.remove(static_path+"gallery\\"+file_name)
    return '<script>alert("successfully deleted");window.location="/gallery_management"</script>'



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
    db = Db()
    lid = str(session['lid'])
    res=db.select("SELECT * FROM  services WHERE shop_id='"+lid+"' ORDER BY services.service_id DESC")
    return render_template('owner/view service.html',data=res)

@app.route("/edit_service/<sid>")
def edit_service(sid):
    db = Db()
    res=db.selectOne("SELECT * FROM services WHERE service_id='"+sid+"'")
    session['ab']=sid
    return render_template('owner/edit service.html',data=res)

@app.route('/edit_service_post',methods=['post'])
def edit_service_post():
    db = Db()
    service = request.form.get('filde')
    vehicle_type = request.form.get('service')
    price = request.form['price']

    sid=str(session['ab'])
    db.update("UPDATE services SET service='"+service+"',vehichle_type='"+vehicle_type+"',amount='"+price+"' WHERE service_id='"+sid+"'")
    return '<script>alert("successfully updated");window.location="/view_services"</script>'

@app.route('/delete_service/<seid>')
def delete_service(seid):
    db= Db()
    db.delete("DELETE FROM services WHERE service_id='"+seid+"' ")
    return '<script>alert("successfully deleted");window.location="/view_services"</script>'


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
    lid = str(session['lid'])
    db =Db()
    res=db.select("SELECT service_request.*,user.* FROM workshop,USER,service_request WHERE service_request.user_id=user.login_id AND service_request.workshop_id=workshop.login_id AND workshop.login_id='"+lid+"' AND service_request.status='pending' ORDER BY service_request.service_request_id DESC")
    return render_template('owner/view pending requests.html',data=res)

@app.route('/more_info_pending_request/<sid>')
def more_info_pending_request(sid):
    db =Db()
    res=db.selectOne("SELECT  service_request.*,vehicle.*,user.* FROM service_request,vehicle,USER WHERE service_request.service_request_id='"+sid+"' AND service_request.user_id=user.login_id AND service_request.vehichle_id=vehicle.vehicle_id")
    res1=db.select("SELECT services.*,service_request.*,user_service.* FROM services,service_request,user_service WHERE service_request.service_request_id='"+sid+"' AND service_request.service_request_id=user_service.service_request_id AND user_service.service_id=services.service_id")
    session['id']=sid
    return render_template('owner/service request more info.html',data=res,data1=res1)

@app.route('/accepet_reject_service_request',methods=['post'])
def accepet_reject_service_request():
    db =Db()
    sid=session['id']
    submit = request.form['submit']
    if submit =='Accept':
        db.update("UPDATE service_request SET STATUS='approved' WHERE service_request_id='"+sid+"'")
        return '<script>alert("request approved");window.location="/pending_service_requestes"</script>'
    else:
        db.update("UPDATE service_request SET STATUS='rejected' WHERE service_request_id='"+sid+"'")
        return '<script>alert("request rejected");window.location="/pending_service_requestes"</script>'


@app.route('/approved_service_requestes')
def approved_service_requestes():
    lid = str(session['lid'])
    db =Db()
    res=db.select("SELECT service_request.*,user.* FROM workshop,USER,service_request WHERE service_request.user_id=user.login_id AND service_request.workshop_id=workshop.login_id AND workshop.login_id='"+lid+"' AND service_request.status='approved' ORDER BY service_request.service_request_id DESC")
    return render_template('owner/view approved service requests.html',data=res)

@app.route('/upadte_service_status/<sid>')
def upadte_service_status(sid):
    db =Db()
    res = db.selectOne("SELECT  service_request.*,vehicle.*,user.* FROM service_request,vehicle,USER WHERE service_request.service_request_id='" + sid + "' AND service_request.user_id=user.login_id AND service_request.vehichle_id=vehicle.vehicle_id")
    res1 = db.select("SELECT services.*,service_request.*,user_service.*,user_service.amount as uamount FROM services,service_request,user_service WHERE service_request.service_request_id='" + sid + "' AND service_request.service_request_id=user_service.service_request_id AND user_service.service_id=services.service_id")
    session['id']=sid
    return render_template('owner/update service status.html',data=res,data1=res1)

@app.route('/generate_invoice',methods=['post'])
def generate_invoice():
    amount=request.form.getlist('number')
    user_service_id = request.form.getlist('user_service_id')
    sid=session['id']
    db = Db()
    sum =0;
    for k in range (len(user_service_id)):
        db.update("UPDATE user_service SET amount='"+amount[k]+"' WHERE user_service_id='"+user_service_id[k]+"'")
        sum=sum+float(amount[k]);
    parts = request.form['part']
    discount = request.form['dis']

    total_amount= sum+float(parts)-float(discount);
    db.update("UPDATE service_request SET parts='" + parts + "',discount='" + discount + "',payment='"+str(total_amount)+"',STATUS='done' WHERE service_request_id='" + sid + "'")



    return '<script>alert(" done");window.location="/approved_service_requestes"</script>'

@app.route('/service_request_history')
def service_request_history():
    lid = str(session['lid'])
    db = Db()
    res=db.select("SELECT service_request.*,user.* FROM workshop,USER,service_request WHERE service_request.user_id=user.login_id AND service_request.workshop_id=workshop.login_id AND workshop.login_id='"+lid+"' AND service_request.status='done' ORDER BY service_request.service_request_id DESC")
    return render_template('owner/view service requests history.html',data=res)

@app.route('/service_history_more_info/<sid>')
def service_history_more_info(sid):
    db = Db()
    res = db.selectOne("SELECT  service_request.*,vehicle.*,user.* FROM service_request,vehicle,USER WHERE service_request.service_request_id='" + sid + "' AND service_request.user_id=user.login_id AND service_request.vehichle_id=vehicle.vehicle_id")
    res1 = db.select("SELECT services.*,service_request.*,user_service.*,user_service.amount as uamount FROM services,service_request,user_service WHERE service_request.service_request_id='" + sid + "' AND service_request.service_request_id=user_service.service_request_id AND user_service.service_id=services.service_id")
    return render_template('owner/view service history more info.html', data=res, data1=res1)


@app.route('/view_rating')
def view_rating():
    lid = str(session['lid'])
    db =Db()
    res=db.select("SELECT rating.*,user.name,user.place FROM rating,workshop,USER,service_request WHERE rating.service_request_id=service_request.service_request_id AND service_request.user_id=user.login_id AND service_request.workshop_id=workshop.login_id AND workshop.login_id='"+lid+"' ORDER BY rating.rating_id DESC")
    return render_template('owner/view rating.html',data=res)

@app.route('/logout_shop')
def logout_shop():
    session.pop('lid')
    return redirect(url_for('hello_world'))



################android
@app.route('/and_login',methods=['post'])
def and_login():
    username=request.form['username']
    password=request.form['password']
    db = Db()
    k={}
    res = db.selectOne("SELECT * FROM login WHERE username='" + username + "' AND PASSWORD='" + password + "' and user_type='user'")
    if res is not None:
        k['status']='valid'
        k['lid'] = res['login_id']

    else:
        k['status']='invalid'
    return demjson.encode(k)


@app.route('/and_singup',methods=['post'])
def and_singup():
    name=request.form['name']
    password=request.form['password']
    email=request.form['email']
    phone=request.form['phone']
    files = request.files['fileField']
    db=Db()
    k={}
    lid = db.insert("INSERT INTO login(username,PASSWORD,user_type) VALUE ('" + email + "','" +password+ "','user')")
    login_id = str(lid)

    res=db.insert("INSERT INTO USER(login_id,NAME,email,phone)VALUE ('"+login_id+"','"+name+"','"+name+"','"+phone+"')")

    file_name='profile_'+str(lid)+'.jpg'
    files.save(static_path+"user\\profile\\"+file_name)
    db.update("update user set user_image='"+file_name+"' where user_id='"+str(res)+"'")
    if res is not None:
        k['status']='ok'
        k['lid']=login_id
    else:
        k['status']='missing'
    return demjson.encode(k)

@app.route('/and_sinup_locations',methods=['post'])
def and_sinup_locations():
    place=request.form['place']
    city=request.form['city']
    district=request.form['district']
    pincode=request.form['pincode']

    lid=request.form['lid']
    db=Db()
    k = {}
    res=db.update("update user set place='" + place + "',city='" + city + "',district='" + district + "',pincode='" + pincode + "'where login_id='" + lid + "'")
    if res is not None:
        k['status']='ok'
        k['lid'] = lid

    else:
        k['status']='missing'
    return demjson.encode(k)

@app.route('/and_home',methods=['post'])
def and_home():
    lid=request.form['login_id']

    db=Db()
    vehicle = db.selectOne("SELECT company,model,image FROM vehicle WHERE user_id='"+lid+"'")
    news=db.select("SELECT * FROM news order by desc ")
    k={}
    if vehicle is not None:
        k['v_status']="1"
        k['v_data']=vehicle
    else:
        k['v_status']='0'
    if len(news)>0:
        k['n_status']="1"
        k['n_data']=news
    else:
        k['n_status'] = '0'
    return demjson.encode(k)
@app.route('/and_notification')
def and_notification():
    db=Db()
    notification=db.select("SELECT * FROM notification")
    k={}
    if  len(notification)>0:
        k['not_status'] = "1"
        k['not_data'] = notification

    else:
        k['not_status'] = '0'
    return demjson.encode(k)

@app.route('/and_services',methods=['post'])
def and_services():
    db=Db()
    service=request.form['service']
    services=db.select("SELECT services.*,workshop.shop_name,workshop.place,workshop.phone FROM services,workshop WHERE service='"+service+"' AND services.shop_id=workshop.shop_id")
    k={}
    if  len(services)>0:
        k['ser_status'] = "1"
        k['ser_data'] = services

    else:
        k['ser_status'] = '0'
    return demjson.encode(k)

@app.route('/and_workshop',methods=['post'])
def and_workshop():
    db=Db()
    shop_id=request.form['shop_id']
    workshop=db.select("SELECT * FROM workshop WHERE workshop.shop_id='"+shop_id+"'")
    services=db.select("SELECT * FROM services WHERE services.shop_id='"+shop_id+"'")
    gallery=db.select("SELECT * FROM gallery WHERE gallery.shop_id='"+shop_id+"'")
    k = {}
    if len(workshop) > 0:
        k['shop_status'] = "1"
        k['shop_data'] = workshop

    else:
        k['shop_status'] = '0'
    if len(gallery) > 0:
        k['gall_status'] = "1"
        k['gall_data'] = gallery

    else:
        k['gall_status'] = '0'
    k = {}
    if len(services) > 0:
        k['ser_status'] = "1"
        k['ser_data'] = services

    else:
        k['ser_status'] = '0'
    return demjson.encode(k)

@app.route('/and_reviews',methods=['post'])
def and_reviews():
    db=Db()
    shop_id = request.form['shop_id']
    service_request_id=request.form['service_request_id']
    feedback=request.form['review']
    rating = request.form['rating']
    reviews=db.select("SELECT rating.*,service_request.*,user.name FROM rating,service_request,`user` WHERE rating.service_request_id=service_request.service_request_id AND service_request.workshop_id='"+shop_id+"' AND service_request.user_id=user.login_id")
    add_review=db.insert("INSERT INTO rating (service_request_id,rating,DATE,feedback) VALUE ('"+service_request_id+"','"+rating+"',CURDATE(),'"+feedback+"')")
    k = {}
    if len(reviews) > 0:
        k['ser_status'] = "1"
        k['ser_data'] = reviews

    else:
        k['ser_status'] = '0'
    if add_review is not None:
        k['adr_status'] = 'ok'
        k['adr_lid'] = add_review['rating_id']

    else:
        k['adr_status'] = 'missing'
    return demjson.encode(k)


@app.route('/and_checkout',methods=['post'])
def and_checkout():
    db=Db()
    user_id=request.form['login_id']
    vehicle_id=request.form['vehicle_id']
    shop_id=request.form['shop_id']
    sid=db.insert("INSERT INTO service_request (user_id,vehicle_id,request_date,STATUS,workshop_id)VALUE('"+user_id+"','"+vehicle_id+"',CURDATE(),'pending','"+shop_id+"')")
    service_id=request.form['service_id']
    amount=request.form['amount']
    user_ser=db.insert("INSERT INTO user_service (service_request_id,service_id,amount)VALUE ('"+sid+"','"+service_id+"','"+amount+"')")
    k={}
    if sid is not None:
        k['sid_status']='ok'
        k['sid_vlid'] = sid['login_id']

    else:
        k['sid_status']='missing'
    if user_ser is not None:
        k['user_ser_status']='ok'
        k['user_ser_vlid'] = user_ser['login_id']

    else:
        k['user_ser_status']='missing'
    return demjson.encode(k)



@app.route('/and_vehicle',methods=['post'])
def and_vehicle():
    db=Db()
    login_id = request.form['login_id']
    vehicle=db.select("SELECT * FROM vehicle WHERE vehicle.user_id='"+login_id+"'")
    k = {}
    if len(vehicle) > 0:
        k['veh_status'] = "1"
        k['veh_data'] = vehicle

    else:
        k['veh_status'] = '0'
    return demjson.encode(k)
@app.route('/and_add_vehicle',methods=['post'])
def and_add_vehicle():
    db=Db()
    login_id = request.form['lid']
    vehicle_type=request.form['type']
    company=request.form['company']
    model=request.form['model']
    manfctr_year=request.form['year']
    regno=request.form['regno']
    add_vechle=db.insert("INSERT INTO vehicle(user_id,vehicle_type,company,model,manfctr_year,regno)VALUE('"+login_id+"','"+vehicle_type+"','"+company+"','"+model+"','"+manfctr_year+"','"+regno+"')")
    files = request.files['fileField']

    file_name = 'vehicle_' + str(add_vechle) + '.jpg'
    files.save(static_path + "user\\vehicle\\" + file_name)
    db.update("update vehicle set image='" + file_name + "' where vehicle_id='" + str(add_vechle) + "'")
    k ={}
    if add_vechle is not None:
        k['status']='ok'

    else:
        k['addv_status']='missing'
    return demjson.encode(k)
@app.route('/and_profile',methods=['post'])
def and_profile():
    db=Db()
    login_id = request.form['lid']
    profile=db.selectOne("SELECT user.name,user.email,user.phone,user.user_image FROM USER WHERE user_id='"+login_id+"'")
    k = {}
    if profile is not None:
        k['profile_status'] = 'ok'
        k['profile_vlid'] = profile

    else:
        k['profile_status'] = 'missing'
    return demjson.encode(k)
@app.route('/and_edit_profile',methods=['post'])
def and_edit_profile():
    db=Db()
    login_id = request.form['lid']
    name=request.form['name']
    email=request.form['email']
    phone=request.form['phone']
    files = request.files['fileField']
    file_name = 'profile_' + str(login_id) + '.jpg'
    files.save(static_path + "user\\profile\\" + file_name)
    edt_profile=db.update("UPDATE USER SET NAME='"+name+"',email='"+email+"',phone='"+phone+"',user_image='" + file_name + "' WHERE user_id='"+login_id+"'")
    k = {}
    if edt_profile is not None:
        k['edt_profile_status'] = 'ok'
    else:
        k['edt_profile_status'] = 'missing'
    return demjson.encode(k)

@app.route('/and_edit_profile_without_image',methods=['post'])
def and_edit_profile_without_image():
    db=Db()
    login_id = request.form['lid']
    name=request.form['name']
    email=request.form['email']
    phone=request.form['phone']
    edt_profile=db.update("UPDATE USER SET NAME='"+name+"',email='"+email+"',phone='"+phone+"' WHERE user_id='"+login_id+"'")
    k = {}
    if edt_profile is not None:
        k['edt_profile_status'] = 'ok'
    else:
        k['edt_profile_status'] = 'missing'
    return demjson.encode(k)

@app.route('/and_profile_loc',methods=['post'])
def and_profile_loc():
    db=Db()
    login_id = request.form['lid']

    profile_loc=db.selectOne("SELECT user.place,user.city,user.district,user.pincode FROM USER WHERE user_id='"+login_id+"'")
    k = {}
    if profile_loc is not None:
        k['profile_loc_status'] = 'ok'
        k['profile_loc_vlid'] = profile_loc

    else:
        k['profile_loc_status'] = 'missing'
    return demjson.encode(k)

@app.route('/and_edit_profile_loc',methods=['post'])
def and_edit_profile_loc():
    db=Db()
    login_id = request.form['lid']
    place = request.form['place']
    city = request.form['city']
    district = request.form['district']
    pincode = request.form['pincode']
    edt_profile_loc=db.update("UPDATE USER SET place='"+place+"',city='"+city+"',district='"+district+"',pincode='"+pincode+"' WHERE user_id='"+login_id+"'")
    k = {}
    if edt_profile_loc is not None:
        k['edt_profile_loc_status'] = 'ok'

    else:
        k['edt_profile_loc_status'] = 'missing'
    return demjson.encode(k)
@app.route('/and_order_history',methods=['post'])
def and_order_history():
    db=Db()
    login_id = request.form['login_id']
    order_history=db.select("SELECT * FROM service_request,vehicle,services,user_service WHERE service_request.vehichle_id=vehicle.vehicle_id AND service_request.service_request_id=user_service.service_request_id AND user_service.service_id=services.service_id AND service_request.user_id='"+login_id+"'")
    k = {}
    if len(order_history) > 0:
        k['order_history_status'] = "1"
        k['order_history_data'] = order_history

    else:
        k['order_history_status'] = '0'
    return demjson.encode(k)
@app.route('/and_invoice',methods=['post'])
def and_invoice():
    db=Db()
    login_id = request.form['login_id']
    invoice=db.select("SELECT * FROM service_request,vehicle,services,user_service,USER WHERE service_request.vehichle_id=vehicle.vehicle_id AND service_request.service_request_id=user_service.service_request_id AND user_service.service_id=services.service_id AND service_request.user_id=user.login_id AND service_request.user_id='"+login_id+"'")
    k = {}
    if len(invoice) > 0:
        k['invoice_status'] = "1"
        k['invoice_data'] = invoice

    else:
        k['invoice_status'] = '0'
    return demjson.encode(k)

@app.route('/and_app_feedback',methods=['post'])
def and_app_feedback():
    db=Db()
    login_id = request.form['lid']
    feedback=request.form['feedback']
    feedback=db.insert("INSERT INTO feedback (user_id,feedback,feedback_date) VALUE('"+login_id+"','"+feedback+"',CURDATE())")
    k = {}
    if len(feedback) > 0:
        k['feedback_status'] = "1"
        k['feedback_data'] = feedback

    else:
        k['feedback_status'] = '0'
    return demjson.encode(k)


@app.route('/and_compalint',methods=['post'])
def and_compalint():
    db=Db()
    login_id = request.form['lid']
    complaint_f=request.form['complaint']

    add_complaint=db.update("INSERT INTO complaint (user_id,complaint,complaint_date)VALUE('"+login_id+"','"+complaint_f+"',CURDATE())")
    k = {}

    if add_complaint is not None:
        k['add_complaint_status']='ok'

    else:
        k['add_complaint_status']='missing'
    return demjson.encode(k)
@app.route('/and_change_passsword',methods=['post'])
def and_change_passsword():
    db=Db()
    k = {}
    login_id = request.form['lid']
    password=request.form['newpass']
    current_password=request.form['currentpass']
    curr_db=db.selectOne("SELECT PASSWORD FROM login WHERE login_id='"+login_id+"' and password='"+current_password+"'")
    if curr_db is not None:
        change_password = db.update("UPDATE login SET PASSWORD='" + password + "' WHERE login_id='" + login_id + "'")
        k['change_password_status'] = 'ok'
    else:
        error='incorrect password'
        k['change_password_status'] = 'missing'

    return demjson.encode(k)

@app.route('/and_view_compalint',methods=['post'])
def and_view_compalint():
    db=Db()
    login_id = request.form['lid']
    compalint = db.select("SELECT * FROM complaint WHERE user_id='" + login_id + "'")
    k = {}
    if len(compalint) > 0:
        k['compalint_status'] = "1"
        k['compalint_data'] = compalint

    else:
        k['compalint_status'] = '0'
    return demjson.encode(k)

@app.route('/and_vehicle_select_type',methods=['post'])
def and_vehicle_select_type():
    db=Db()

    vehicle_type=db.select("SELECT DISTINCT vehicle_type FROM vehicledb")
    k ={}
    if len (vehicle_type) > 0:
        k['vehicle_type_status'] = "1"
        k['vehicle_type_data'] = vehicle_type

    else:
        k['vehicle_type_status'] = '0'
    return demjson.encode(k)
@app.route('/and_vehicle_select_company',methods=['post'])
def and_vehicle_select_company():
    db=Db()
    vehicle_type=request.form['type']
    vehicle_company=db.select("SELECT DISTINCT company FROM vehicledb WHERE vehicle_type='"+vehicle_type+"'")

    k = {}
    if len(vehicle_company) > 0:
        k['vehicle_company_status'] = "1"
        k['vehicle_company_data'] = vehicle_company

    else:
        k['vehicle_company_status'] = '0'
    return demjson.encode(k)

@app.route('/and_vehicle_select_model',methods=['post'])
def and_vehicle_select_model():
    db=Db()
    vehicle_type=request.form['type']
    vehicle_company=request.form['company']
    vehicle_model=db.select("SELECT DISTINCT model FROM vehicledb WHERE vehicle_type='"+vehicle_type+"' AND company='"+vehicle_company+"'")
    k = {}
    if len(vehicle_model) > 0:
        k['vehicle_model_status'] = "1"
        k['vehicle_model_data'] = vehicle_model

    else:
        k['vehicle_model_status'] = '0'
    return demjson.encode(k)



if __name__ == '__main__':
    app.run(host='0.0.0.0')
