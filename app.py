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
    res=db.select("SELECT workshop.* FROM login,workshop WHERE login.user_type='pending' AND login.login_id=workshop.login_id ")
    return render_template('admin/view_pending_workshop.html',data=res)

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

@app.route('/View_rating')
def View_rating():
    db =Db()
    res=db.select("SELECT rating.*,workshop.shop_name,user.name FROM rating,workshop,USER,service_request WHERE rating.service_request_id=service_request.service_request_id AND service_request.user_id=user.login_id AND service_request.workshop_id=workshop.login_id ORDER BY rating.rating_id DESC")
    return render_template('admin/view rating.html',data=res)

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

@app.route('/delete_notification/<nid>')
def delete_notification(nid):
    db =Db()
    db.delete("DELETE FROM notification WHERE notification_id='"+nid+"'")
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
    db = Db()
    file_name = 'news_' + str(nid) + '.jpg'
    files.save(static_path + "news\\" + file_name)
    db.update("UPDATE news SET DATE=CURDATE(),news_title='"+title+"',news_description='"+discription+"',image='"+file_name+"' WHERE news_id='"+nid+"'")
    return '<script>alert("successfully updated");window.location="/view_news"</script>'

@app.route('/delete_news/<neid>')
def delete_news(neid):
    db =Db()
    db.delete("DELETE FROM news WHERE news_id='"+neid+"'")
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
    db =Db()
    lid = str(session['lid'])
    file_name = 'worckshop_' + str(lid) + '.jpg'
    files.save(static_path + "worckshop\\" + file_name)

    db.update("UPDATE  workshop SET shop_name='"+shop_name+"',place='"+place+"',city='"+city+"',district='"+district+"',pincode='"+pincode+"',email='"+emial+"',shop_lisence='"+file_name+"',phone='"+phone+"',lati='"+latitude+"',longi='"+longitude+"' WHERE login_id='"+lid+"'")
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
    return render_template('owner/gallery_management.html',data=res)

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
    res1 = db.select("SELECT services.*,service_request.*,user_service.* FROM services,service_request,user_service WHERE service_request.service_request_id='" + sid + "' AND service_request.service_request_id=user_service.service_request_id AND user_service.service_id=services.service_id")
    session['id']=sid
    return render_template('owner/update service status.html',data=res,data1=res1)

@app.route('/generate_invoice',methods=['post'])
def generate_invoice():
    amount=request.form.getlist('number')
    user_service_id = request.form.getlist('user_service_id')
    sid=session['id']
    db = Db()
    for k in range (len(user_service_id)):
        db.update("UPDATE user_service SET amount='"+amount[k]+"' WHERE user_service_id='"+user_service_id[k]+"'")
    # res=db.update("")
    print(amount)
    return 'ok'

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
    res1 = db.select("SELECT services.*,service_request.*,user_service.* FROM services,service_request,user_service WHERE service_request.service_request_id='" + sid + "' AND service_request.service_request_id=user_service.service_request_id AND user_service.service_id=services.service_id")
    return render_template('owner/view service history more info.html', data=res, data1=res1)


@app.route('/view_rating')
def view_rating():
    lid = str(session['lid'])
    db =Db()
    res=db.select("SELECT rating.*,user.name,user.place FROM rating,workshop,USER,service_request WHERE rating.service_request_id=service_request.service_request_id AND service_request.user_id=user.login_id AND service_request.workshop_id=workshop.login_id AND workshop.login_id='"+lid+"' ORDER BY rating.rating_id DESC")
    return render_template('owner/view rating.html',data=res)




if __name__ == '__main__':
    app.run()
