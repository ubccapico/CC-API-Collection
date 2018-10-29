# CAPICO-Library
A helper library for Python 3 that provides a variety of helper functions for working with the Canvas API. Pagination is dealt with automatically for all relevant functions (so a returned pandas DataFrame will have **ALL** information).

## To begin:
```python
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

# allow_student_organized_groups, enable_offline_web_export
'''
Change settings for a course
Parameters:
    url_in (String): URL of Canvas instance
    token_in (String): Canvas token
    course_in (String): Canvas ID of course
    setting_name (String): Name of setting to change
    setting_value (int/Boolean): 1 is True, 0 is False
Returns:
    None
'''
def change_course_settings(url_in, token_in, course_in, setting_name, setting_value)
```

#### Course-quiz functions:
```python
'''
Get all submissions for a specified quiz (Incomplete)
Parameters:
    url_in (String): URL of Canvas instance
    token_in (String): Canvas token
    course_in (String): Canvas ID of course
    quiz_in (String): Canvas ID of quiz
Returns:
    JSON of all quiz submissions
'''
def get_all_quiz_submissions(url_in, token_in, course_in, quiz_in)

'''
Gives specified extra time to student
Parameters:
    url (String): URL of Canvas instance
    token (String): Canvas token
    class_id (String): Canvas ID of course
    quiz_id (String): Canvas ID of quiz
    student_id (String): Canvas ID of student
    extra_time (String): Extra time given to student in minutes
Returns:
    Response body of API request
'''
def extend_time(url, token, class_id, quiz_id, student_id, extra_time)

'''
Gives specified extra time to all students in a course
Parameters:
    url (String): URL of Canvas instance
    token (String): Canvas token
    class_id (String): Canvas ID of course
    quiz_id (String): Canvas ID of quiz
    extra_time (String): Extra time given to student in minutes
Returns:
    None
'''
def extend_all(url, token, class_id, quiz_id, extra_time)
```

#### Blueprint-level functions:
```python
'''
Helper function that gets a list of courses associated with a blueprint course (MAY CHANGE WHEN BLUEPRINT SYSTEM UPDATED)
Parameters:
    blue_id: Blueprint course ID on Canvas
    token: User-generated API token
    url: URL of Canvas instance
'''
def get_associated_courses(blue_id, token, url)

'''
Function adds and removes courses from blueprint associations
Parameters:
    blue_id (String): Canvas ID of blueprint course
    token (String): Canvas token
    url (String): Canvas URL
    to_remove (List[String]): List of courses to remove from blueprint association (if you do not wish to remove any, give an empty list)
    to_add (List[String]): List of courses to add from blueprint association (if you do not wish to add any, give an empty list)
Returns:
    None
'''
def update_associations(blue_id, token, url, to_remove, to_add)

```

#### Subaccount-level functions:
```python
'''
Function prints out the subaccount structure of a given node
Parameters:
    account_id (String): Canvas ID of node to find children for
    token (String): Canvas token
    url (String): Canvas URL
Returns:
    None
'''
def print_subaccount_tree(account_id, token, url)

'''
Gets the info about a subaccount (Incomplete)
'''
def get_account_info(url_in, token_in, subaccount_in)

'''
Gets all courses under a subaccount (and all of its children accounts as well)
Parameters:
    url_in (String): URL of Canvas instance
    token_in (String): Canvas token
    subaccount_in (String, int): Canvas Subaccount ID
Returns:
    Pandas DataFrame of all course under a subaccount
'''
def get_account_courses(url_in, token_in, subaccount_in)

# See change_course_settings
def change_course_settings_subaccount(url_in, token_in, subaccount_in, setting_names, setting_value)

'''
List all of the enrollment terms under a master account
Parameteres:
    url_in (String): URL of Canvas instance
    token_in (String): Canvas token
    subaccount_in (String): Canvas ID of master account
Returns:
    Pandas DataFrame of all enrollment terms
'''
def list_enrollment_terms(url_in, token_in, subaccount_in)

```
