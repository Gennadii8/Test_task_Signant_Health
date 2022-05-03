import requests
import string
import random

URL = "http://localhost:8080"
HEADERS = {'Content-Type': 'application/json'}


def create_new_user():
    """duplicated functionality, but comfortable to use in token_creation_tests"""
    username = ''.join(random.choice(string.ascii_lowercase) for i in range(10))
    password = ''.join(random.choice(string.ascii_lowercase) for i in range(10))
    firstname = ''.join(random.choice(string.ascii_lowercase) for i in range(10))
    lastname = ''.join(random.choice(string.ascii_lowercase) for i in range(10))
    phone = ''.join(random.choice(string.digits) for i in range(10))
    resp = requests.post("http://localhost:8080/api/users",
                         headers=HEADERS,
                         json={'username': str(username),
                               'password': str(password),
                               'firstname': str(firstname),
                               'lastname': str(lastname),
                               'phone': int(phone)})
    return username, password


def create_data_for_new_user(extra_data=None):
    """create dict with params for new user"""
    user_data = {}
    params_list = ['username', 'password', 'firstname', 'lastname']
    # adding special data to dict
    if extra_data:
        for param, value in extra_data.items():
            user_data[f'{param}'] = value
    # adding other data in dict
    for one_param in params_list:
        user_data.setdefault(one_param, ''.join(random.choice(string.ascii_lowercase) for i in range(10)))
    # special adding for phone (because it should consist of numbers)
    user_data.setdefault('phone', ''.join(random.choice(string.digits) for i in range(10)))
    return user_data


def post_for_new_user(special_data=None):
    user_info_0 = create_data_for_new_user(special_data)
    resp_0 = requests.post(URL + "/api/users",
                           headers=HEADERS,
                           json=user_info_0)
    return resp_0
