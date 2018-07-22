from masonite.validator import Validator
from validator import Required, Pattern, In, Not, Length
from app.User import User

class RegisterValidator(Validator):
    
    def register(self):
        users = User.all()
        self.messages({
            'email': 'That email already exists',
            'username': 'That username already exists'
        })
        
        return self.validate({
            'username': [Required, Length(3, 10), Not(In(users.pluck('name')))],
            'email': [Required, Length(1), Not(In(users.pluck('email')))],
            'password': [Required]
        })

    def login(self):
        users = User.all()
        self.messages({
            'username': 'That email does not exist',
            'password': 'You forgot to enter a password!',
        })
        
        return self.validate({
            'username': [Required, Length(1), In(users.pluck('email'))],
            'password': [Required, Length(1)]
        })
