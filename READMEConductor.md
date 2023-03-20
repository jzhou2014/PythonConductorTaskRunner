## Start the Conductor server locally
1. Clone [Netflix Conductor repository](https://gitee.unigroupinc.com/enterprise-data/conductor/-/tree/unigroup)
```bash
$ git clone git@gitee.unigroupinc.com:enterprise-data/conductor.git
$ cd conductor/
```
2. Start the Conductor server
```bash
/conductor$ ./gradlew bootRun
```
3. Start Conductor UI
```bash
/conductor$ cd ui/
/conductor/ui$ yarn install
/conductor/ui$ yarn run start
```
You should be able to access:

 - Conductor API:

   http://localhost:8080/swagger-ui/index.html
- Conductor UI:

   http://localhost:5000
