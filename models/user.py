from unratedwriting import typewrite
from uuid import uuid4

class User:
    users = []

    @classmethod
    def get(cls,**kwargs):
        if len(kwargs) > 1:
            raise LookupError(f'The <User.get> method expects only one argument {len(kwargs)} given')
        key = list(kwargs.keys())[0]
        try:
            result = list(filter(lambda x: getattr(x,key) == kwargs[key],User.users))
            return result
        except Exception as e:
            raise AttributeError(f'User does not have the requested data <error> : {e}')
        
            
    def __init__(self, **kwargs):
        try:
            self.id = str(uuid4())
            self.balance = 0
            self.username = kwargs["username"]
            self.age = int(kwargs["age"])
            self.country = kwargs["country"]
        except Exception as e:
            raise AttributeError(f'Cannot create user, missing required params<error>: {e}')
        for key, value in kwargs.items():
            setattr(self,key,value)
        User.users.append(self)
    def __repr__(self) -> str:
        return f'<User {self.id}>'
