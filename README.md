# test-automation

## pre-requisites
- Run one of the following commands to install necessary packages:
    ```shell script
    pip3 install selenium
    ```
    OR
    ```
    pip3 install -r ./resources.txt 
    ```

- [Download Chromedriver](https://chromedriver.chromium.org/downloads) and add it to your system PATH variable

**NOTE:** You will need to [add a valid account email/password](./testData/user_accounts.py) to the `/testData/user_accounts.py` in order to successfully run the following tests:
 - `/test/test_sign_out.py`
 - `/test/test_valid_login.py`

### Running tests

To run all tests, run the following command:
```shell script
python3 -m unittest
```

##### Run individual test
```shell script
python3 -m unittest test/test_invalid_login.py
```
