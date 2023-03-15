from .data_classes.user import User


def user(username: str, formatter: list[str]) -> User:
    return User(username=username, formatter=formatter)
