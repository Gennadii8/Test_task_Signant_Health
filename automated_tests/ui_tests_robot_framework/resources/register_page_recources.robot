*** Settings ***
Library    SeleniumLibrary
Resource    resources.robot

*** Variables ***
${USERNAME_INPUT}    id:username
${PASSWORD_INPUT}    id:password
${FIRSTNAME_INPUT}    id:firstname
${LASTNAME_INPUT}    id:lastname
${PHONE_INPUT}    id:phone
${REGISTER_BUTTON}    xpath://input[@value='Register']

*** Keywords ***
Open register page by url
    open browser    ${REGISTER_URL}    ${BROWSER}
    wait until page contains element    ${REGISTER_BUTTON}

Open register page by ui click
    click link    ${REGISTER_LINK}
    wait until page contains element    ${REGISTER_BUTTON}

Write username
    [Arguments]    ${username}
    input text    ${USERNAME_INPUT}    ${username}

Write password
    [Arguments]    ${password}
    input password    ${PASSWORD_INPUT}    ${password}

Write first name
    [Arguments]    ${firstname}
    input text    ${FIRSTNAME_INPUT}    ${firstname}

Write last name
    [Arguments]    ${lastname}
    input text    ${LASTNAME_INPUT}    ${lastname}

Write phone
    [Arguments]    ${phone}
    input text    ${PHONE_INPUT}    ${phone}

Click register button
    click button    ${REGISTER_BUTTON}

Create random user
    ${RANDOM_USERNAME}    generate random string    10    [Letters]
    ${RANDOM_PASSWORD}    generate random string    10    [Letters]
    ${RANDOM_FIRSTNAME}    generate random string    10    [Letters]
    ${RANDOM_LASTNAME}    generate random string    10    [Letters]
    ${RANDOM_PHONE}    generate random string    10    [Numbers]
    Set Suite Variable      ${RANDOM_USERNAME}
    Set Suite Variable      ${RANDOM_PASSWORD}
    Set Suite Variable      ${RANDOM_FIRSTNAME}
    Set Suite Variable      ${RANDOM_LASTNAME}
    Set Suite Variable      ${RANDOM_PHONE}
