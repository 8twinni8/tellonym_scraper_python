import Tellonym
import Database

if __name__ == '__main__':
    user: Tellonym.User = Tellonym.User(username='this.weinstein', formatter=['username', 'id', 'followers'])
    user.info()
    user.followers()
    Database.save(user)