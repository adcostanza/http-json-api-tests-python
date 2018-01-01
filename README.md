## Purpose
The purpose of this small piece of Python software is to enable quick building of tests that target an HTTP JSON API.

## Usage
See `Auth.py` for some examples of usage. To import the TestServer simply type `import TestServer as test` which will enable you to access all of the methods under the test namespace:

### HTTP Request Assertion
See below for the arguments you may pass in you assertion. It will by default check if the status of the response is 200, which you may change to a different status code (i.e. 403) if desired.

```
anyAssert(type,url,description, data=[], tests=[], headers={}, statusExpected=200):
```
### Tests
The following are tests that I have built so far, but you may build others just as easily following the same class with check method as seen in `TestServer.py`:

1. `hasProperty(self,property,should)`
2. `hasTrueProperty(self,property,should)`
3. `hasFalseProperty(self,property,should)`
4. `hasPropertyEqualTo(self,property,equals,should)`

### Reusing values from response
It is as easy as just assigning `anyAssert` to a variable, i.e. `body=anyAssert(...)` and then you may use either of these methods or parse the returned JSON (or null response) yourself:
1. `getValueFromResponse(body,property)`
2. `getValuesFromResponse(body,property)`

## Example output
### Success
Below is an example of all tests passing:
![output](https://i.imgur.com/cBKnpTJ.png "")


### Failure
Even better is when we catch failure, such as that the API shows that the user is unable to change the admins password but it turns out that when I try to login as as the admin with the new password it has indeed been changed. Simply prefixing a `return` to the `res.status(403)` ended up fixing this error so the code execution was halted after authorization failure.
![fail](https://i.imgur.com/L6a303y.png "")
