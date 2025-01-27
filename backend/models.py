# contains all of our database models, and how we use SQLAlchemy to interract with the database. 
from config import db


class Contact(db.Model): 
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(80), unique = False, nullable = False)
    # max length is 80, not all unique values, and you cannot pass a NULL value
    last_name = db.Column(db.String(80), unique = False, nullable = False)
    email = db.Column(db.String(120), unique = True, nullable = False)
    # no two people should have the same email id. 
    
    
    
    
    def to_json(self): 
        # this is a function that can take this object and convert it into a 
        # python dictionary, which we can then convert into a JSON, which 
        # is something we can pass with our api
        # JSON = JavaScript Object Notation
        
        # json convention is camel case. snake case is convention for python. 
        
        return {
            "id": self.id,
            "firstName": self.first_name,
            "lastName": self.last_name,
            "email": self.email,
        }
        
        
        
    
   
