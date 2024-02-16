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
        
    
    
    def __init__(self,from_dict : dict=None, **kwargs):
        if not from_dict:
            try:
                self.username = kwargs["username"]
                self.age = int(kwargs["age"])
                self.country = kwargs["country"]
            except Exception as e:
                raise AttributeError(f'Cannot create user, missing required params<error>: {e}')
            for key, value in kwargs.items():
                setattr(self,key,value)
        else:
            if not isinstance(from_dict,dict):
                raise TypeError(f'Pass in a dictionary to from_dict param')
            keys = ['username','age','country']
            if not all(key in from_dict for key in keys):
                raise KeyError('Missing required key')
            for i,j in from_dict.items():
                setattr(self,i,j)
        self.id = str(uuid4())
        self.balance = 0
        User.users.append(self)
    def __repr__(self) -> str:
        return f'<User {self.id}>'
