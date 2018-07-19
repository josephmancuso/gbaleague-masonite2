''' A UserResource API Resource '''
from entry.api.Resource import Resource
from entry.api.JsonSerialize import JsonSerialize
from entry.api.auth import EncryptedTokenAuthentication
from entry.api.auth import OAuth2
from entry.api import RateLimit
from app.User import User


class UserResource(Resource, JsonSerialize, EncryptedTokenAuthentication):
    model = User
    data_wrap = False
    scopes = ['user:read', 'user:post']
    exclude = ['remember_token', 'password', 'customer_id', 'plan_id']
    methods = ['read', 'create']
