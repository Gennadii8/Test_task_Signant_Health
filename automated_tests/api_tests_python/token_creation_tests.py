import unittest
import requests
from automated_tests.api_tests_python.assisting_functions import create_new_user, HEADERS, URL


class APITokenCreator(unittest.TestCase):

    def test_get_token_for_existing_user(self):
        """create token for existing user - success and token expected"""
        # here new user is created
        username, password = create_new_user()
        resp = requests.get(URL+"/api/auth/token",
                            auth=(username, password),
                            headers=HEADERS)
        token = resp.json()['token']
        status = resp.json()['status']
        self.assertTrue(token)
        self.assertEqual('SUCCESS', status)

    def test_get_token_for_nonexistent_user(self):
        """create token for nonexistent user - failure expected"""
        # send wrong username and password
        username = 'sfvndfjvnjdbvhbdvhbdhv34333bjdstgt'
        password = 'bvbvbybrtyvbrtvytrbvsivoeoeiurf'
        resp = requests.get(URL+"/api/auth/token",
                            auth=(username, password),
                            headers=HEADERS)
        status = resp.json()['status']
        self.assertEqual('FAILURE', status)


if __name__ == "__main__":
    unittest.main()
