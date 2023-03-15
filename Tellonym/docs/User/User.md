# `Tellonym.data_classes.user.User` class documentation

This class represents a Tellonym user and provides various methods to interact with the Tellonym API. Here is the documentation of the class and its methods.

## Class User
The User class is the main class for interacting with the Tellonym API to retrieve and manipulate user data. It is defined in the Tellonym.data_classes.user module and can be imported as follows:

```python
from Tellonym.data_classes.user import User
```
## Constructor `__init__(self, username: str = "", user_dict: dict = {}, formatter: list[str] = None)`

This method initializes a new `User` object with the given `username`, `user_dict`, and `formatter`.

Parameters:

- `username` (str): The username of the user.
- `user_dict` (dict): A dictionary containing user information.
- `formatter` (list[str]): A list of keys to include when formatting the user as a string (you can use every string from the [properties section](#properties).

## Method `info(self) -> dict`

This method gets user information from the Tellonym API and returns it as a dictionary.

Returns:

- A dictionary containing user information.

## Method `followers(self) -> list[User]`

This method gets the user's followers and returns them as a list of `User` objects.

Returns:

- A list of `User` objects representing the user's followers.

## Method `followings(self) -> list[User]`

This method gets the user's followings and returns them as a list of `User` objects.

Returns:

- A list of `User` objects representing the user's followings.

## Method `tells(self) -> list[Tell]`

This method gets the user's tells and returns them as a list of `Tell` objects.

Returns:

- A list of `Tell` objects representing the user's tells.

## Method `download_images(self, out_path: str) -> bool`

This method downloads the user's profile pictures to the specified output path.

Parameters:

- `out_path` (str): The path to download the profile pictures to.

Returns:

- `True` if the images were downloaded successfully, `False` otherwise.

## Properties

| Name                     | Type   | Description                                                            |
| ------------------------ | ------ | ---------------------------------------------------------------------- |
| `id`                     | `int`  | The unique identifier of the user.                                     |
| `username`               | `str`  | The username of the user.                                              |
| `displayName`            | `str`  | The display name of the user.                                          |
| `aboutMe`                | `str`  | The user's bio.                                                        |
| `avatarFileName`         | `str`  | The file name of the user's avatar image.                              |
| `followerCount`          | `int`  | The number of followers the user has.                                  |
| `anonymousFollowerCount` | `int`  | The number of anonymous followers the user has.                        |
| `follower`               | `list` | A list of the user's followers.                                        |
| `followingCount`         | `int`  | The number of users the user is following.                             |
| `followings`             | `list` | A list of users the is following.                                      |
| `likesCount`             | `int`  | The total number of likes the user has received.                       |
| `answerCount`            | `int`  | The total number of answers the user has posted.                       |
| `tellCount`              | `int`  | The total number of tells the user has posted.                         |
| `tells`                  | `list` | A list of the user's tells                                             |
| `pinnedPosts`            | `list` | A list of the user's pinned posts.                                     |
| `isAbleToChat`           | `bool` | Indicates whether the user is able to chat with others.                |
| `tintColor`              | `int`  | The user's selected color for their profile.                           |
| `badge`                  | `int`  | The user's selected badge for their profile.                           |
| `statusEmoji`            | `int`  | The user's selected emoji for their status.                            |
| `isFollowed`             | `bool` | Indicates whether the user is followed by the authenticated user.      |
| `followNotificationType` | `int`  | The user's notification settings for follow notifications.             |
| `isVerified`             | `bool` | Indicates whether the user is a verified user.                         |
| `isBlocked`              | `bool` | Indicates whether the authenticated user has blocked the user.         |
| `isBlockedBy`            | `bool` | Indicates whether the authenticated user has been blocked by the user. |
| `linkData`               | `list` | A list of the user's linked social media accounts.                     |
| `countryCode`            | `str`  | The two-letter country code of the user's location.                    |
| `isActive`               | `bool` | Indicates whether the user's account is active.                        |
| `avatars`                | `list` | A list of the user's avatar images.                                    |