class Tell:
    def __init__(self, tell: dict) -> None:
        for key, value in tell.items():
            setattr(self, key, value)
        pass

    def __repr__(self) -> str:
        return str(vars(self))