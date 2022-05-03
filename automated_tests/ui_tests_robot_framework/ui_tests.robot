*** Settings ***
Library    SeleniumLibrary
Resource    resources/resources.robot
Resource    resources/register_page_recources.robot
Suite Teardown    Close All Browsers

*** Variables ***

*** Test Cases ***
Register new normal user
    [Documentation]    Test of success of transition from main to register pages and normal user creating
    Open index page
    maximize browser window
    Check basic unauthorized links
    Open register page by ui click
    Check basic unauthorized links
    Create random user
    Write username    ${RANDOM_USERNAME}
    Write password    ${RANDOM_PASSWORD}
    Write first name    ${RANDOM_FIRSTNAME}
    Write last name    ${RANDOM_LASTNAME}
    Write phone    ${RANDOM_PHONE}
    Click register button
    location should be    ${LOGIN_URL}
    close browser

Login, checking info and logging out for existing user
    [Documentation]    Test of success of login into system by existing user with right usermane and password + check user info (taking user from previous test case)
    Open login page
    Check basic unauthorized links
    maximize browser window
    input text    id:username    ${RANDOM_USERNAME}
    input password    id:password    ${RANDOM_PASSWORD}
    click element    xpath://input[@value="Log In"]
    location should be    ${USER_URL}
    Check basic authorized links
    page should contain    ${RANDOM_USERNAME}
    page should contain    ${RANDOM_FIRSTNAME}
    page should contain    ${RANDOM_LASTNAME}
    page should contain    ${RANDOM_PHONE}
    page should not contain   ${RANDOM_PASSWORD}
    click link    ${LOGOUT_LINK}
    location should be    ${INDEX_URL}
    Check basic unauthorized links
    close browser

Check error with empty password registration
    [Documentation]    Test of error when entering empty password on registration
    Open index page
    maximize browser window
    Check basic unauthorized links
    Open register page by ui click
    Check basic unauthorized links
    Create random user
    Write username    ${RANDOM_USERNAME}
    Write password    ${EMPTY}
    Write first name    ${RANDOM_FIRSTNAME}
    Write last name    ${RANDOM_LASTNAME}
    Write phone    ${RANDOM_PHONE}
    Click register button
    location should be    ${REGISTER_URL}
    Check basic unauthorized links
    close browser

Check error with wrong password login
    [Documentation]    Test of error when entering wrong password on login page
    Open login page
    Check basic unauthorized links
    maximize browser window
    input text    id:username    ${RANDOM_USERNAME}
    input password    id:password    sdg5dfg2f6g62ds32g62
    click element    xpath://input[@value="Log In"]
    page should contain    Login Failure
    location should be    ${ERROR_URL}
    Check basic unauthorized links
    close browser




