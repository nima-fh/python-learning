class SearchList(list["User"]):
    def search(self,userName:str)->list["User"]:
        match_user:list["User"]=[]
        for user in self:
            if userName in user.UserName:
                match_user.append(user)
        return match_user
        
        
class User:
    AllUsers=[]
    def __init__(self,UserName:str,email:str,password:str)->None:   
        self.UserName=UserName
        self.password=password     
        self.email=email
        User.AllUsers.append(self)
    def __str__(self):
        return f"{self.UserName} {self.email}"
    
    def __repr__(self):
        return f"User(UserName='{self.UserName}', email='{self.email}')"
 

class Seller(User):
    def order(self,order):
        print(f"Dear {self.UserName} from your products,{order} was sold!")
        
class Buyer(User):
    def __init__(self, UserName, email, password,phone):
        super().__init__(UserName, email, password)   
        self.phone=phone  
    
    
nima=User("nima fakhimi","n1384.fakhimi@gmail.com","n8413fakhimi")
buyer=Buyer("nima fakhimi","n1384.fakhimi@gmail.com","n8413fakhimi","09301275197")
seller1=Seller("nima fakhimi","n1384.fakhimi@gmail.com","n8413fakhimi")
print(seller1.UserName)
seller1.order("iphone 17")
print((buyer.phone))