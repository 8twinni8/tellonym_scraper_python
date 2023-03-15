class UserIdMissingException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(f'ID argument could not be found on user. Try calling .info() first!')

class UserNameMissingException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(f'Username is not present!')