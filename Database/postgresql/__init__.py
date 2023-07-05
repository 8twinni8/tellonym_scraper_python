import json
import os

from .model.tellmodel import save_tells as save_tells_model
from .model.usermodel import save_user as save_user_model
from .model.usersocialmediamodel import save_usersocialmedia as save_usersocialmedia_model
import psycopg2

from Tellonym.data_classes.tell import Tell
from Tellonym.data_classes.user import User

with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'config.json'), 'r') as f:
    config: dict = json.load(f)

conn = psycopg2.connect(**config)
cur = conn.cursor()

def save_user(user: User) -> bool:
    save_user_model(user)
    pass

def save_tells(tells: list[Tell]) -> bool:
    save_tells_model(tells)
    pass

def save_usersocialmedia(socialmedia: list[dict]) -> bool:
    save_usersocialmedia_model(socialmedia)
    pass