import random
import string
from dataclasses import dataclass
from schema import UserLoginSchema
from repository import UserRepository

@dataclass
class UserService:
    user_repo: UserRepository

    def create_user(self, user_name: str, password: str) -> UserLoginSchema:
        access_token = self._generate_access_token()
        user = self.user_repo.create_user(user_name=user_name, password=password, access_token=access_token)
        return UserLoginSchema(user_id=user.id, access_token=user.access_token)

    @staticmethod
    def _generate_access_token() -> str:
        return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
