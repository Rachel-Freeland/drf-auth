# LAB - Class 33
## Project: Authentication & Production Server
### Author: Rachel Freeland
### Links and Resources
* [Docker](https://www.docker.com/)
* Features added:
  * JWT authorizations - provides a token for user access

### Setup
* Make ure that you have Docker on your system - follow the link above
* At the command prompt enter: `docker compose up`

### How to initialize/run your application (where applicable)
* Run `docker compose up --build`

### How to use your library (where applicable)
### Tests
* How do you run tests?
  * Tests were run using ThunderClient
* Any tests of note?
  * No, log in, post, update, delete methods working as expected
* Describe any tests that you did not complete, skipped, etc
  * Tested the routes before obtaining a token to demonstrate failure if no access token is supplied
  * Tested the routes with the access token to demonstrate working when authorization is provided
  * Routes tested:
    * /admin/
    * /api/v1/dogs/
    * /api/v1/dogs/1
    * /api/token/
    * /api/token/refresh/
