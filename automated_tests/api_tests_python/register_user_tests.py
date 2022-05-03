import unittest
from automated_tests.api_tests_python.assisting_functions import post_for_new_user


class UserRegister(unittest.TestCase):

    def test_success_new_user_creating(self):
        """test success of registering new user - expected success status (doesn't check message)"""
        resp = post_for_new_user()
        status = resp.json()['status']
        self.assertEqual('SUCCESS', status)

    def test_failure_new_user_same_username_creating(self):
        """test success of registering new user with same username - expected failure status and right error message
        here I first of all I create user and then try to create ome more with same username"""
        resp_0 = post_for_new_user(special_data={'username': 'Mister Bean'})
        resp = post_for_new_user(special_data={'username': 'Mister Bean'})
        status = resp.json()['status']
        error_message = resp.json()['message']
        self.assertEqual('FAILURE', status)
        self.assertEqual('User exists', error_message)

    def test_failure_new_user_empty_password_creating(self):
        """test success of registering new user with empty password - expected failure status"""
        resp = post_for_new_user(special_data={'password': ''})
        print(resp.json())
        status = resp.json()['status']
        self.assertEqual('FAILURE', status)

    def test_failure_new_user_empty_username_creating(self):
        """test success of registering new user with empty username - expected failure status
        And also here I check that it breaks not because of error of already existing user with empty name"""
        resp_0 = post_for_new_user(special_data={'username': ''})
        resp = post_for_new_user(special_data={'username': ''})
        status = resp.json()['status']
        self.assertEqual('FAILURE', status)
        message = resp.json()['message']
        self.assertNotEqual('User exists', message)

    def test_failure_new_user_symbols_in_phone_creating(self):
        """test success of registering new user with symbols in phone - expected failure status"""
        resp = post_for_new_user(special_data={'phone': 'pumpurum'})
        status = resp.json()['status']
        self.assertEqual('FAILURE', status)

    def test_failure_new_user_all_empty_creating(self):
        """test success of registering new user with all empty fields - expected failure status
        And also here I check that it breaks not because of error of already existing user with empty name"""
        resp_0 = post_for_new_user(special_data={'username': ''})
        resp = post_for_new_user(special_data={'username': '',
                                               'password': '',
                                               'firstname': '',
                                               'lastname': '',
                                               'phone': ''})
        status = resp.json()['status']
        message = resp.json()['message']
        self.assertEqual('FAILURE', status)
        self.assertNotEqual('User exists', message)

    def test_failure_new_user_with_same_phone(self):
        """test failure of registering new user with same phone number as another user have - expected failure status"""
        resp_0 = post_for_new_user(special_data={'phone': '777'})
        resp_1 = post_for_new_user(special_data={'phone': '777'})
        print(resp_1.json())
        status = resp_1.json()['status']
        self.assertEqual('FAILURE', status)


if __name__ == "__main__":
    unittest.main()
