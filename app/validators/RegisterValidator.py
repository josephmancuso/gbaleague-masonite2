from masonite.validator import Validator
from validator import Required, Pattern, In, Not, Length
from app.User import User

class RegisterValidator(Validator):
    
    def register(self):
        users = User.all()
        self.messages({
            'email': 'That email already exists',
            'username': 'Usernames should be between 3 and 20 characters long'
        })

        return self.validate({
            'username': [Required, Length(3, 20)],
            'email': [Required, Length(1), Not(In(users.pluck('email')))],
            'password': [Required]
        })


    def check_exists(self):
        users = User.all()
        self.messages({
            'username': 'Username already exists'
        })
        self.request.request_variables['username'] = self.request.request_variables['username'].lower()
        return self.validate({
            'username': [Required, Not(In(users.pluck('name').map(lambda item: item.lower())))]
        })

    def login(self):
        users = User.all()
        self.request.request_variables['username'] = self.request.request_variables['username'].lower()
        self.messages({
            'username': 'That email does not exist',
            'password': 'You forgot to enter a password!',
        })
        
        return self.validate({
            'username': [Required, Length(1), In(users.pluck('name').map(lambda item: item.lower()))],
            'password': [Required, Length(1)]
        })
