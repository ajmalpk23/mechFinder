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
        if username=='admin':
            return redirect(url_for('admin_home'))
        elif username=='owner':
            return redirect(url_for('owner_home'))

    else:
        return '<script>alert("invalid username or password");window.location="/"</script>'



###################admin###################

@app.route('/admin_home')
def admin_home():
    return render_template('admin/admin_home.html')

@app.route('/view_pending_workshop')
def view_pending_workshop():
    return render_template('admin/view_pending_workshop.html')

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
    return render_template('admin/view_Notification.html')

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
    return render_template('admin/view news.html')

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

@app.route('/view_services')
def view_services():
    return render_template('owner/view service.html')

@app.route('/add_services')
def add_services():
    return render_template('owner/add_service.html')

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
