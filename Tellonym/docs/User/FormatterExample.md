# Formatter Example

```python
import Tellonym
from Tellonym.data_classes.user import User

user: User = Tellonym.user(username='Tellonym', formatter['username', 'id', 'follower'])
user.info()
user.followers()
print(user)
```

Results in following output: 
```json
{
    "username": "Tellonym",
    "id": 1,
    "followers": [
        {
            "username": "derN3rd",
            "id": 2
        },
        {
            "username": "trusto",
            "id": 3
        },
        {
            "username": "pizzaundso",
            "id": 457
        },
        ...
    ],
}
```

Note: follower "derN3rd" doesn't contain any followers since those aren't scraped and therefore not available