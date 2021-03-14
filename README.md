# Python Twitter Bot using Selenium

This is a simple twitter bot made using Selenium that at the moment just creates and sends out tweets.

## What You'll Need

- Selenium module installed using the following:
  ```
  pip install selenium
  ```
- dotenv-python module installed (implemented just to handle the private nature of usernames and passwords)
  ```
  pip install python-dotenv
  ```
- Browser driver for your browser of choice. In my case, I used Google Chrome in which the driver can be found at the following: https://chromedriver.chromium.org/downloads (Ensure that the driver version matches your browser version)
  \*Note that in my case, I also relocated the driver to be in my Program Files (x86) directory. If you have it in another location, change the PATH in the code as seen below:
  ```
  PATH = "INSERT_DRIVER_PATH_HERE"
  ```
- Create a .env file and add your credentials as follows:
  ```
  TWITTER_USERNAME=Insert_Username_Here
  TWITTER_PASSWORD=Insert_Password_Here
  ```

## References

- https://medium.com/swlh/automate-your-tweets-with-selenium-ee93bf26eb82 (used to look for the selector for certain elements)
