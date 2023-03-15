# `Tellonym.data_classes.tell.Tell` class documentation

## `__init__(self, tell: dict) -> None`

Initializes a new Tell object with the given tell dictionary.

Parameters

- `tell` (dict): A dictionary containing tell information.

## Properties

The Tell object has the following properties:

| Field Name              | Data Type | Description                                                            |
| ----------------------- | --------- | ---------------------------------------------------------------------- |
| type                    | str       | Type of the post.                                                      |
| postType                | int       | Type of the post.                                                      |
| id                      | int       | Unique identifier for the post.                                        |
| answer                  | str       | The text content of the post.                                          |
| likesCount              | int       | The number of likes received for the post.                             |
| createdAt               | str       | The date and time the post was created in ISO 8601 format.             |
| tell                    | str       | The text content of the tell associated with the post.                 |
| isLiked                 | bool      | Indicates if the post has been liked by the current user.              |
| userId                  | int       | ID of the user who received the post.                                  |
| senderStatus            | int       | The status of the sender of the tell.                                  |
| sender                  | dict      | Sender of the tell.                                                    |
| isCurrentUserTellSender | bool      | Indicates if the current authenticated user is the sender of the tell. |
| likes                   | dict      | Information about the likes received for the post.                     |
| media                   | list      | Array of media associated with the post.                               |
| pointsKarma             | int       | The number of points or karma associated with the post.                |
| rtType                  | null      | Reserved field.                                                        |
| rtVariance              | null      | Reserved field. Always set to null.                                    |