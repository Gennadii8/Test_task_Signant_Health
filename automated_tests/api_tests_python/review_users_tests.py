import copy
import unittest
import requests
from automated_tests.api_tests_python.assisting_functions import HEADERS, URL, create_new_user


class UsersReviewer(unittest.TestCase):

    def test_check_existing_users_with_token(self):
        """get info with token about all users(create user at first and get token for him)
        - expected success (also payload can be checked)"""
        # here new user is created
        username, password = create_new_user()
        # them get his token
        resp_token = requests.get(URL + "/api/auth/token",
                                  auth=(username, password),
                                  headers=HEADERS)
        token = resp_token.json()['token']
        edited_headers = copy.deepcopy(HEADERS)
        edited_headers['Token'] = f'{token}'
        resp = requests.get(URL + "/api/users",
                            headers=edited_headers)
        status = resp.json()['status']
        self.assertEqual('SUCCESS', status)


    def test_check_existing_users_with_wrong_token(self):
        """get info with wrong token about all users(create wrong token) - expected failure"""
        edited_headers = copy.deepcopy(HEADERS)
        edited_headers['Token'] = 'sdsdfsdfsdfsdfsddfsfsddfsfsdfsdfsddfsdfsdf'
        resp = requests.get(URL + "/api/users",
                            headers=edited_headers)
        status = resp.json()['status']
        self.assertEqual('FAILURE', status)

    def test_check_existing_users_without_token(self):
        """get info without token about all users - expected failure"""
        resp = requests.get(URL + "/api/users",
                            headers=HEADERS)
        status = resp.json()['status']
        self.assertEqual('FAILURE', status)


if __name__ == "__main__":
    unittest.main()
