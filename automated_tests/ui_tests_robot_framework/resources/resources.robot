*** Settings ***
Library    SeleniumLibrary
Library    String

*** Variables ***
${BROWSER}    chrome
${REGISTER_LINK}    /register
${LOGIN_LINK}    /login
${LOGOUT_LINK}    /logout
${HOME_LINK}    /
${REGISTER_URL}    http://127.0.0.1:8080/register
${LOGIN_URL}=    http://127.0.0.1:8080/login
${USER_URL}    http://127.0.0.1:8080/user
${INDEX_URL}    http://127.0.0.1:8080/
${ERROR_URL}    http://127.0.0.1:8080/error

*** Keywords ***
Check basic unauthorized links
    page should contain link    ${LOGIN_LINK}
    page should contain link    ${REGISTER_LINK}
    page should contain link    ${HOME_LINK}

Check basic authorized links
    page should contain link    ${LOGOUT_LINK}
    page should contain link    ${HOME_LINK}

Open index page
    open browser    ${INDEX_URL}    ${BROWSER}
    wait until page contains    index page

Open login page
    open browser    ${LOGIN_URL}    ${BROWSER}
    wait until page contains element    xpath://input[@value="Log In"]

Open user page
    open browser    ${USER_URL}    ${BROWSER}
    wait until page contains    User Information


