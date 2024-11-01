from core.entities import User
from core.exceptions import IncorrectPasswordError, LoginNotExistsError
from core.services import PasswordService, UserService


class LoginUserUseCase:
    def __init__(self, user_service: UserService, password_service: PasswordService) -> None:
        self._user_repo = user_service
        self._password_service = password_service

    async def login(self, login: str, password: str) -> User:
        user = await self._user_repo.find_by_login(login=login)
        if not user:
            raise LoginNotExistsError(login=login)
        password_hash = self._password_service.hash_password(password)
        if not self._password_service.check_password(password=password, password_hash=password_hash):
            raise IncorrectPasswordError
        return user
