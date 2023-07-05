import json
import os

from neo4j import GraphDatabase

from Tellonym.data_classes.user import User

with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'config.json'), 'r') as f:
    config: dict = json.load(f)

driver = GraphDatabase.driver(**config)

def save_connections(user: User) -> bool:
    pass