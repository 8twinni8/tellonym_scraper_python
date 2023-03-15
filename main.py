import Tellonym
from Tellonym.data_classes.user import User


if __name__ == '__main__':
    user: User = Tellonym.user(username='Tellonym', formatter=['username', 'id', 'followers'])
    user.info()
    user.followers()
    print(user)