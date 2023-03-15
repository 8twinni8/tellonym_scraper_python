import os

from typing import TypeVar
from .tell import Tell
from ..request.urls import *
from ..request.requests import Request
from ..exceptions.exceptions import *

User = TypeVar('User')

class User:
    def __init__(self, username: str = "", user_dict: dict = {}, formatter: list[str] = None) -> None:
        """
        Initialize a new User object with the given username, user dictionary, and formatter.

        Parameters:
        - username (str): The username of the user.
        - user_dict (dict): A dictionary containing user information.
        - formatter (list[str]): A list of keys to include when formatting the user as a string.
        """
        self.username: str = username
        self.formatter = formatter

        for key, value in user_dict.items():
            setattr(self, key, value)
        
        if not (hasattr(self, 'username') and self.username):
            raise UserNameMissingException()
        pass

    def info(self) -> dict:
        """
        Get user information from the Tellonym API and return it as a dictionary.

        Returns:
        - A dictionary containing user information.
        """
        url = URL_USERINFO.format(self.username)
        self.data: dict = Request.get(url).json()
        for key, value in self.data.items():
            setattr(self, key, value)
        return self.data

    def _get_users(self, base_url: str, attr_name: str) -> list[User]:
        users = []
        while True:
            url = base_url.format(self.username, len(users))
            user = [User(user_dict=user, formatter=self.formatter) for user in Request.get(url).json()[attr_name]]
            if not user:
                return users
            users.extend(user)

    def followers(self) -> list[User]:
        """
        Get the user's followers and return them as a list of User objects.

        Returns:
        - A list of User objects representing the user's followers.
        """
        self.followers = self._get_users(URL_FOLLOWERS, 'followers')
        return self.followers

    def followings(self) -> list[User]:
        """
        Get the user's followings and return them as a list of User objects.

        Returns:
        - A list of User objects representing the user's followings.
        """
        self.followings = self._get_users(URL_FOLLOWINGS, 'followings')
        return self.followings

    def tells(self) -> list[Tell]:
        """
        Get the user's tells and return them as a list of Tell objects.

        Returns:
        - A list of Tell objects representing the user's tells.
        """
        if not hasattr(self, 'id'):
            raise UserIdMissingException()

        self.tells = []
        while True:
            url = URL_TELLS.format(self.id, len(self.tells))
            tells = [Tell(tell) for tell in Request.get(
                url)['answers'] if 'adType' not in tell]
            if not tells:
                break
            self.tells.extend(tells)

        return self.tells

    def download_images(self, out_path: str):
        """
        Download the user's profile pictures to the specified output path.

        Parameters:
        - out_path (str): The path to download the profile pictures to.

        Returns:
        - True if the images were downloaded successfully, False otherwise.
        """
        out_path = os.path.join(out_path, str(self.id))
        if not os.path.exists(out_path):
            os.makedirs(out_path)

        [open(os.path.join(out_path, img['avatarFileName']), 'wb').write(Request.get(
            URL_PROFILEPICTURE.format(img['avatarFileName'])).content) for img in self.avatars]

        return True

    def __repr__(self) -> str:
        if not self.formatter:
            return f"<Tellonym.data_classes.user.User object at {id(self):#018x}>"

        variables = vars(self)

        if '*' in self.formatter:
            return str({k: v for k, v in variables.items() if k != 'formatter'})

        output = {}

        for format in self.formatter:
            if not format in variables:
                continue
            output[format] = variables[format]

        return str(output)