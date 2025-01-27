# main routes and endpoints

# Create Read Update Delete: CRUD

#create: 
    # - first_name
    # - last_name
    # - email
    
    
# request is anything that we send to a server. 
# frontend sends the request, backend sends the response. 
# status 200 : success

from flask import request, jsonify
from config import app, db
from models import Contact


    
@app.route("/contacts", methods=["GET"]) # this is a 'decorator'
def get_contacts():
    # mapping each item in contacts with to_json() function
    contacts = Contact.query.all()
    # mapping each item in contacts with to_json() function
    json_contacts = list(map(lambda x: x.to_json(), contacts))
    # mapping each item in contacts with to_json() function
    return jsonify({"contacts": json_contacts})
    # the 200 means successful reqyest, and it is the default. 


@app.route("/contacts", methods =["POST"]) # post route defiition for /contacts to post a contact
def create_contact():  # POST to "/contacts"
    first_name = request.json.get("firstName")
    last_name = request.json.get("lastName")
    email = request.json.get("email")
    
    if not (first_name or last_name or email): 
        return ( # response has a status and a message JSON. 
                # 400 status code means that server cannot process the request
            jsonify({"message": "You must include a first name, last name and email"}),
            400,
        )
        
    # else, post request was a valid format. 
    new_contact = Contact(first_name=first_name, last_name=last_name, email=email)
    
    try: 
        db.session.add(new_contact)
        db.session.commit()
    except Exception as e:
        return jsonify({"message" : str(e)}), 400 # status cod3 400 means server cannot process request
    
    
    # if reaches here means successful post to the db. 
    
    return jsonify({
        "message" : 
            str("new contact created!", first_name,
                " ", last_name, "; email: ", email) }), 201
        
    
    
@app.route("/update_contact/<int:user_id>", methods = ["PATCH"])
def update_user(user_id): 
        contact = Contact.query.get(user_id) #gettiung this cotact
        
        if not contact: 
            return jsonify( {"message" : "no contact with that id found."}), 404 
        
        
        data = request.json
        
        contact.first_name = data.get("firstName", contact.first_name)
        contact.last_name = data.get("lastName", contact.last_name)
        contact.email= data.get("email", contact.email)
        
        db.session.commit()  # making changes permanent
        
        return jsonify({"message" : "contact updated succesfully"}), 201
        
      
      
@app.route("/delete_contact/<int:user_id>", methods =['DELETE'])
def delete_user(user_id): 
    contact = contact.query.get(user_id)
    
    if not contact: 
        return jsonify({"message" : "no user with that id found to delete"}), 400
    
    db.session.delete(contact)
    db.session.commit() # to make the changes permanent 
    
    return jsonify({"message" : "user deleted"}), 200
    


if __name__ == "__main__":
    
    with app.app_context():
        db.create_all() # create all the different models we need to find??
        
    
    app.run(debug=True)

    
