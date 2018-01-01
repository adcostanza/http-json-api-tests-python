## Purpose
The purpose of this small piece of Python software is to enable quick building of tests that target an HTTP JSON API.

## Usage
See `Auth.py` for some examples of usage. To import the TestServer simply type `import TestServer as test` which will enable you to access all of the methods under the `test` namespace.

### HTTP Request Assertion
See below for the arguments you may pass into your HTTP assertion. It will by default check if the status of the response is 200, which you may change to a different status code (i.e. 403) if desired.

```
anyAssert(type,url,description, data=[], tests=[], headers={}, statusExpected=200):
```
### Tests
The following are tests/assertions that I have built so far, but you may build others just as easily following the same class with `check` method as seen in `TestServer.py`:

1. `hasProperty(self,property,should)`
2. `hasTrueProperty(self,property)`
3. `hasFalseProperty(self,property)`
4. `hasPropertyEqualTo(self,property,equals,should)`

In all cases, `should` is a `string` that should contain language such as `have a token` for the error messages. `hasTrueProperty` and `hasFalseProperty` do not require a `should` statement as the intention is self evident.

### Reusing values from response
It is as easy as just assigning `anyAssert` to a variable, i.e. `body=anyAssert(...)` and then you may use either of these methods or parse the returned JSON (or null response) yourself:
1. `getValueFromResponse(body,property)`
2. `getValuesFromResponse(body,property)`

## Example output
### Success
Below is an example of all tests passing:
![output](https://i.imgur.com/cBKnpTJ.png "")


### Failure
Even better is when we catch failure, such as the one below where a user is sent a 403 status code when attempting to do admin functions, but even with the 403 status the admins password is changed by the user! Clearly the blocked routes aren't being blocked after returning the status code.  Simply prefixing a `return` to the `res.status(403)` in the express API ended up fixing this error so the code execution was halted after authorization failure. Imagine if this sort of bug wasn't caught, that is why automated testing is so important.
![fail](https://i.imgur.com/L6a303y.png "")

## Inspiration
I was inspired by Chai and Mocha in JavaScript/TypeScript but ultimately thought it would be a bit easier and less convoluted to do automated HTTP testing with Python and `requests`. I ended up having more flexibility as far as making for loops, etc. with assertions and reusing both generic tests as well as more specific ones with the code written here. Chai and Mocha would be better for unit testing.
