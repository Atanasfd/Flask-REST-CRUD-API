from flask import render_template
from app import app
from app.models import db,Contact

#Create
@app.route('/create_Contact/<UserName>/<FirstName>/<SurName>/<phone>', methods=['POST','GET'])
def create_Contact(UserName,FirstName,SurName,phone):
    target=Contact(UserName=UserName,FirstName=FirstName,SurName=SurName,phone=phone)
    db.session.add(target)
    db.session.commit()


    return ("contact  "+target.UserName+" saved")

#Retrieve/Get
@app.route('/get_Contact/<UserName>', methods=['GET'])
def get_user(UserName):
    contact = Contact.query.filter_by(UserName=UserName).first()

    return ("First Name:\t"+str(contact.FirstName)+"\tphone:\t"+str(contact.phone))

#Update 
@app.route('/update_Contact/<UserName>/<phone>', methods=['GET','PUT'])
def update_task(UserName,phone):
    x=Contact.query.filter_by(UserName=UserName).first()
    x.phone=phone
    db.session.commit()
    
    return(str(x.phone))


#Delete
@app.route('/delete_Contact/<UserName>', methods=['GET','DELETE'])
def delete_task(UserName):
    Contact.query.filter_by(UserName=UserName).delete()
    db.session.commit()
    return (UserName+" has been deleted")
