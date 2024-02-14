from unratedwriting import typewrite
from models.user import User
def create_user():
    while True:
        username = input('Username: ')
        if User.get(username=username):
            typewrite('User exists with such username')
        else:
            break

    while True:
        try:
            age = int(input('Age: '))
            if age < 18:
                raise PermissionError('You are too young to play AGBEROBET')
            break
        except ValueError:
            typewrite('Please input a number')
            
    country = input('Country: ')
    currency = "Naira" if country.lower() == 'nigeria' else None
    try:
        a = User(username=username, age=age, country=country,currency=currency)
    except Exception as e:
        print(e)
    return a
