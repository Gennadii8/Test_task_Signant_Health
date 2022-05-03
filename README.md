# Test assignment Gennadii Matveev #

## Installation Instructions ##
(There is a video of tests executions, so 
you can just check the code and the video without setting up environment)

I have uploaded new requirements.txt with bigger list of libraries versions, because there were some conflicts + I used some more libraries
1) Jinja has removed Markup and escape in a recent version — 3.1.0 — released on March 24th, 2022. - downgrade to 3.0.3
2) itsdangerous downgrade to 2.0.1

## Instruction for start the app ##
To run the app on Windows, there might be one more command, full instruction below:
1) pip install -r requirements.txt
2) set FLASK_APP=demo_app
3) $env:FLASK_APP = "demo_app"
4) flask init-db
5) flask run --host=127.0.0.1  --port=8080

(Still need python 3.7 and SQLite)

App will be running on http://127.0.0.1:8000/

## UI testing ##

3 files were created:
1) ui_tests.robot - the main file (I didn't split the files in this test task)
2) resources.robot - a file with the main resources
3) register_page_resources.robot - a file with resources for the registration page

To run the tests, run the "robot ui_tests.robot" command from the "ui_tests_robot_framework" folder.

There are 4 tests in total:
1) Registration of a new user
2) Logging in, verification of information, logging out
3) Registration with an empty password
4) Logging in with the wrong password

4/4 tests pass

When testing the UI, I created one exponentially good test case - "Register new normal user".
In it, I separately moved all the variables and actions to 
the register_page_resources.robot file. With this case, I wanted to show how I 
can design test cases using the Robot Framework. The other three cases are made simply 
for testing minimal functionality. Their proper design could take too much time for 
a test task, so I left them ugly. (For more information about time, see the Spent time 
and thoughts section below). Also, the test case "Login, checking info and 
logging out for existing user" contains a lot of checks - in real development, I would 
divide it into several cases. 

Also, I didn't go too deep into checking the presence of elements on pages 
using "wait until page contains" and "page should contain". 

I didn't run the tests separately using pabot, since there are only 4 of them here.
## API testing ##

I used unittest and Selenium. 
How to run tests:
* You can run them through IDE (as I did in video)
For the launch, it is important that the default test runner is unittest. 
* Or you can open command line in Test_task direction and write:
  1) pip install -r requirements.txt
  2) python -m unittest {your_path}/Test_task/automated_tests/api_tests_python/token_creation_tests.py
  3) python -m unittest {your_path}/Test_task/automated_tests/api_tests_python/review_users_tests.py 
  4) python -m unittest {your_path}/Test_task/automated_tests/api_tests_python/register_user_tests.py
  5) python -m unittest {your_path}/Test_task/automated_tests/api_tests_python/get_and_update_certain_user_tests.py

Here I have created 5 files:
1) assisting_functions.py - auxiliary optimizing functions for tests.
2) token_creation_tests.py - verification of token creation for an existing and non-existing user.
3) register_user_tests.py - registration of a new user, registration of a user with a 
duplicate login, registration with an empty password, registration with an empty login, 
registration with letters in the phone number, registration with all empty fields, 
registration with a duplicate number.
4) review_users_test.py - getting information about all users with a token, 
without a token and with the wrong token.
5) get_and_update_certain_user_tests.py - get information about a user using a token, 
get information about a user without using a token, get information about a user 
(who does not have a token) using someone else's token, get information about a 
user (who has a token) using someone else's token, update user information using a token, 
update user information without using a token, update user information using someone 
else's token.

1. token_creation_tests.py - 2/2 test pass. 
2. register_user_tests.py - 2/7 tests pass. (Fails - possible to create user with all empty fields,
possible to create user with empty password, possible to create user with empty username,
possible to create user letters in phone, possible to create user letters with duplicated phone) 
3. review_users_test.py - 1/3 tests pass. (Fails - possible to get list of users with wrong token,
possible to get list of users without token) 
4. get_and_update_certain_user_tests.py - 7/7 tests pass.

Queries were optimized separately by taking out query functions (POST for example) - 
in fact, it would be possible to use transmission via args/kwargs (better kwargs), but it
seemed to me that this would be clearer (although the kwargs functionality is 
understandable - in general, I can do both) - I didn't optimize the rest of the 
queries, but I could have optimized them, if I would spend more time. So as an example of good autotests, 
it's worth looking at the design of the file register_user_tests.py

I have not written prints anywhere (including for errors), because it's implemented 
differently in different conditions, but writing them is not a problem.

I can still add a lot of test cases in every file, but I have created only the main options.

I mostly looked only at the response statuses, I almost didn't check the messages, 
but it's also easy to finish.

More tests have already been created here than in UI testing, but I also didn't use 
parallel launch, because it seems to me that it's more convenient to view the test task this way.

## Bugs ##
I know how to fully and correctly paint test cases, but for a test task, 
I think such a brief description will be okay.
1) If logged in, then it's impossible transit to the profile page from the main page (UI small bug)
2) With a password "*" you can register through the interface, but then it's impossible to log in
3) You can create a user for the same phone number (POST /api/users)
4) You can enter letters in the phone field and create a user like this - both in the interface and through the API (POST /api/users)
5) In general, with any empty fields, you can create a user through API (+ You can create a person without a password through the API, but then you can't
log in to the profile through the interface + You can create a person without a username through the API, but then you can't log in to the profile through the interface) (POST /api /users)
6) Micro-error - a typo in the successful api response to search for information about a certain user (/api/users/{username}) - 'message': 'retrieval successful'. Successful with two S
7) Without a token and with the wrong token, I can simply get a list of all users by API (GET /api/users) - the token check in this request is not processed
8) Being authorized, I can go to url /register and create a new user

## Spent time and thoughts ##
To be honest, I counted the time a little badly (my mistake, I admit). I did this 
task 4 times for several hours. In general, I spent about 10-12 hours.

It's a little strange that by the condition of the task, a user can receive data from 
other users and change the data of other users through the API, but  as stated in the 
task, I thought this was the right functionality, although it's a little strange. It 
seems it would be logical to create a separate type of admin tokens 
that have the rights to do this, but perhaps this is too much for a test.

I could also test the functions themselves in the code, but it would take even more time,
and you probably didn't mean it.

I hope that everything is clear. If you have any questions, please email me.