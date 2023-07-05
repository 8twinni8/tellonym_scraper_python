from Tellonym.data_classes.user import User
import Database.neo4j as neo4j
import Database.postgresql as postgresql

def save(user: User) -> bool:
    # postgresql.save_user(user)
    # postgresql.save_tells(user.tells)
    # postgresql.save_usersocialmedia(user.linkData)
    neo4j.save_connections(user)
    return False