from pymongo import MongoClient
from bson.objectid import ObjectId

print("this has started")

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username=None, password=None):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections. 
        if (username == "aacuser" and password == "password"):
            self.client = MongoClient('mongodb://%s:%s@localhost:50566/AAC' % (username, password))
            print("aacuser has logged in")
        else:
            print("Generic user logged in")
            self.client = MongoClient('mongodb://localhost:50566')
        self.database = self.client['AAC']

# Create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            insert = self.database.animal.insert(data)  # data should be dictionary 
            print("this has been added")
            if insert!=0:
                return True
            else:
                return False           
        else:
            raise Exception("Nothing to save, because data parameter is empty")
            
        


# Create method to implement the R in CRUD.
    def read(self,criteria=None):

        # criteria is not None then this find will return all rows which matches the criteria
        if criteria:
         # {'_id':False} just omits the unique ID of each row        
            
            data = self.database.animal.find(criteria,{"_id":False})
            print("criteria has been found:")
            
        else:
        #if there is no search criteria then all the rows will be return  
            
            data = self.database.animal.find( {} , {"_id":False})
            print("criteria hasnt been found:")
            
        return data
    
#Update method in implement the U in CRUD.
    def update(self,criteria=None,updatingCriteria=None):
        
        
                    
        data = self.database.animal.update(criteria,{"$set":updatingCriteria})
        print(criteria, " has been update to : ", updatingCriteria) 
            
        return data
        
#Update method in implement the U in CRUD.           
    def delete(self,criteria=None):
            
          # criteria is not None then this find will return all rows which matches the criteria
        if criteria:
         # {'_id':False} just omits the unique ID of each row        
            
            data = self.database.animal.remove(criteria)
            print(criteria, " has been deleted:")
            
        else:
        #if there is no search criteria then all the rows will be return  
            
            
            print("criteria hasnt been found:")
            
        return data