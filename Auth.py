from subprocess import call
call(["docker-compose", "down","-v"])
call(["docker-compose","up","-d","db"])

import time
time.sleep(2)

import TestServer as test

#Tests that we can use in any of our assertions
success = test.hasTrueProperty('success')
fail = test.hasFalseProperty("success")
hasToken = test.hasProperty("token","have token in response")

#Setting up a database test, expecting 200 response and a true success property
test.anyAssert('get','/setup/098##$223fadsf3','first time setup',[success])
#Logging in and loading the response body into a variable
body = test.anyAssert('post','/login','first login as adam',{'username':'adam','password':'tacos'},[hasToken])
#Retrieve the token from the response
token = test.getValueFromResponse(body,'token')

#Some other tests
test.anyAssert('post','/passwords','change adams password to tac0', {'password':'tac0'},[success],{'x-access-token':token})
test.anyAssert('post','/login','login as adam with password tac0',{'username':'adam','password':'tac0'},[hasToken])
test.anyAssert('post','/passwords','change adams password back to tacos',{'password':'tacos'},[success],{'x-access-token':token})

test.anyAssert('post','/users/george','create user george',{'password':'tac0s','role':'user'},[success], {'x-access-token':token})
test.anyAssert('post','/users/george','create another user george',{'password':'tac0s','role':'user'},[fail], {'x-access-token':token})
