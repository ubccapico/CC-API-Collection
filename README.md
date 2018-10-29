# CAPICO-Library
A helper library for Python 3 that provides a variety of helper functions for working with the Canvas API.

## To begin:
```
from CC_API_jh2 import CAPICO
```

### Available Functions:
#### User-level Functions:
```
  '''
    Function gets page views for a user between start and end dates (UTC-8 DateTime objects).
    Parameters:
        user (String): Canvas user ID in question
        token (String): Canvas token
        start (DateTime): UTC-8 DateTime object for start of time range
        end (DateTime): UTC-8 DateTime object for end of time range
    Returns:
        Pandas dataframe of all pages views for a user between start and end date
    '''
    def get_user_page_views(user, token, url, start, end)
```
