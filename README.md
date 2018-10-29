# CAPICO-Library
A helper library for Python 3 that provides a variety of helper functions for working with the Canvas API.

## To begin:
```
from CC_API_jh2 import CAPICO
```

### Available Functions:
#### User-level Functions:
```python
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
#### Course-level Functions:
```python
'''
Helper function that gets Canvas course information.
Parameters:
    course_id (String): ID of Canvas course
    token (String): User-generated API token
    url (String): URL of Canvas instance
Returns:
    Course object (JSON)
'''
def get_course_info(course_id, token, url)

'''
Gets all students in a course.
Parameters:
    url (String): URL of Canvas instance
    class_id (String): Canvas ID of course
    token (String): Canvas token
Returns:
    Pandas DataFrame of students in a course
'''
def get_student_list(url, class_id, token)

'''
Gets all course modules
Parameters:
    url (String): URL of Canvas instance
    class_id(String): Canvas ID of course
    token (String): Canvas token
Returns:
    Pandas DataFrame of modules in a course
'''
def get_course_modules(url, class_id, token)

'''
Gets all course pages
Parameters:
    url (String): URL of Canvas instance
    class_id(String): Canvas ID of course
    token (String): Canvas token
Returns:
    Pandas DataFrame of pages in a course
'''
def get_course_pages(url, class_id, token)

'''
Gets all course files
Parameters:
    url (String): URL of Canvas instance
    class_id(String): Canvas ID of course
    token (String): Canvas token
Returns:
    Pandas DataFrame of files in a course
'''
def get_course_files(url, class_id, token)

'''
Gets all users with as specified role in a course
Parameters:
    url_in (String): URL of Canvas instance
    token_in (String): Canvas token
    course_in (String): Canvas ID of course
    user_type (String): Specified role to look for (e.g. students)
Returns:
    Pandas DataFrame of all users with a specified role in a course
'''
def get_course_users(url_in, token_in, course_in, user_type)
```
