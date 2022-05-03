import copy
import unittest
import requests
from automated_tests.api_tests_python.assisting_functions import HEADERS, URL, create_new_user


class UserEditor(unittest.TestCase):

    def test_get_special_user_info_without_token(self):
        """get info without token about specific user(create him at first) - expected failure and right error message"""
        new_user = create_new_user()[0]
        resp = requests.get(URL + f"/api/users/{new_user}",
                            headers=HEADERS)
        status = resp.json()['status']
        message = resp.json()['message']
        self.assertEqual('FAILURE', status)
        self.assertEqual('Token authentication required', message)

    def test_get_special_user_info_with_token(self):
        """get info with token about specific user(create him at first, then get token) - expected
        success and correct message"""
        # here new user is created
        username, password = create_new_user()
        # them get his token
        resp_token = requests.get(URL + "/api/auth/token",
                                  auth=(username, password),
                                  headers=HEADERS)
        token = resp_token.json()['token']
        edited_headers = copy.deepcopy(HEADERS)
        edited_headers['Token'] = f'{token}'
        resp = requests.get(URL + f"/api/users/{username}",
                            headers=edited_headers)
        status = resp.json()['status']
        message = resp.json()['message']
        self.assertEqual('retrieval succesful', message)
        self.assertEqual('SUCCESS', status)

    def test_get_special_user_without_token_info_by_other_token(self):
        """get info with token of another user about specific user(create first, get token for first user, create
        second user) - expected success"""
        # here new user is created
        username_0, password_0 = create_new_user()
        # them get his token
        resp_token = requests.get(URL + "/api/auth/token",
                                  auth=(username_0, password_0),
                                  headers=HEADERS)
        token = resp_token.json()['token']
        edited_headers = copy.deepcopy(HEADERS)
        edited_headers['Token'] = f'{token}'
        # create another user
        username_1, password_1 = create_new_user()
        resp = requests.get(URL + f"/api/users/{username_1}",
                            headers=edited_headers)
        status = resp.json()['status']
        self.assertEqual('SUCCESS', status)

    def test_get_special_user_with_token_info_by_other_token(self):
        """get info with token of another user about specific user that also has token(create first,
        get token for first user, create second user, get token for second user) - expected success"""
        # here new user is created
        username_0, password_0 = create_new_user()
        # them get his token
        resp_token_0 = requests.get(URL + "/api/auth/token",
                                    auth=(username_0, password_0),
                                    headers=HEADERS)
        token = resp_token_0.json()['token']
        edited_headers = copy.deepcopy(HEADERS)
        edited_headers['Token'] = f'{token}'
        # create another user
        username_1, password_1 = create_new_user()
        resp_token_1 = requests.get(URL + "/api/auth/token",
                                    auth=(username_1, password_1),
                                    headers=HEADERS)
        resp = requests.get(URL + f"/api/users/{username_1}",
                            headers=edited_headers)
        status = resp.json()['status']
        self.assertEqual('SUCCESS', status)

    def test_update_special_user_info_with_token(self):
        """update info with token about specific user(create him at first and his token) - expected success"""
        # create user
        username, password = create_new_user()
        # get token for user
        resp_token = requests.get(URL + "/api/auth/token",
                                  auth=(username, password),
                                  headers=HEADERS)
        token = resp_token.json()['token']
        edited_headers = copy.deepcopy(HEADERS)
        edited_headers['Token'] = f'{token}'
        payload = {'firstname': 'table', 'lastname': 'wall'}
        resp = requests.put(URL + f"/api/users/{username}",
                            headers=edited_headers,
                            json=payload)
        status = resp.json()['status']
        self.assertEqual('SUCCESS', status)

    def test_update_special_user_info_without_token(self):
        """update info without token about specific user(create him at first) - expected failure"""
        # create user
        username, password = create_new_user()
        payload = {'firstname': 'chair', 'lastname': 'window'}
        resp = requests.put(URL + f"/api/users/{username}",
                            headers=HEADERS,
                            json=payload)
        status = resp.json()['status']
        self.assertEqual('FAILURE', status)

    def test_update_special_user_info_with_another_token(self):
        """update with token of another user info about specific user(create him at first and his token)
        - expected success"""
        # here new user is created
        username_0, password_0 = create_new_user()
        # them get his token
        resp_token_0 = requests.get(URL + "/api/auth/token",
                                    auth=(username_0, password_0),
                                    headers=HEADERS)
        token = resp_token_0.json()['token']
        edited_headers = copy.deepcopy(HEADERS)
        edited_headers['Token'] = f'{token}'
        # create another user
        username_1, password_1 = create_new_user()
        payload = {'firstname': 'table', 'lastname': 'wall'}
        resp = requests.put(URL + f"/api/users/{username_1}",
                            headers=edited_headers,
                            json=payload)
        status = resp.json()['status']
        self.assertEqual('SUCCESS', status)


if __name__ == "__main__":
    unittest.main()
