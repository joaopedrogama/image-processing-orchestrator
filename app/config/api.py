from ninja_jwt.controller import NinjaJWTDefaultController
from ninja_extra import NinjaExtraAPI
from ninja.security import HttpBearer

class GlobalAuth(HttpBearer):
    def authenticate(self, request, token):
        if token == "supersecret": # TODO: Change this to a real token
            return token

api = NinjaExtraAPI(
    # auth=GlobalAuth(),
)
api.register_controllers(NinjaJWTDefaultController)
api.auto_discover_controllers()
