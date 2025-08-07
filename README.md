# Instagram account creation and follow accounts automation

> [!CAUTION]
> ```This tool is intended for educational purposes only, and we are not responsible for any misuse of the code!```

## REQUIREMENTS

- Python installed

## HOW TO USE

```
git clone https://github.com/gustavosantossh/instagram-follow-automation

cd ./instagram-follow-automation
```

After cloning the repository, change the Config.py class to the data of your preferences. (src/app/config/Config.py)

```
class Config:

    # Optional (Random values if not filled)
    ACC_EMAIL_PREFIX = "your_email_prefix" 
    ACC_PASSWORD_PREFIX = "your_password" 
    ACC_FULLNAME_PREFIX = "fullName_account" # acc_fullName + random token
    ACC_USERNAME_PREFIX = "username_account" # acc_username + "_" + random token

    # Required
    USER_TO_FOLLOW = "user_to_follow"
```

**Accounts will be generated automatically with random email, using the designated prefixes** 

```
email -> ACC_EMAIL_PREFIX + random token + domain
password -> ACC_PASSWORD_PREFIX + "_" + random token
fullname -> ACC_FULLNAME_PREFIX + random token
username -> ACC_USERNAME_PREFIX + "_" + random token
```

**For instagram not to block your ip, add a proxy without authentication.**

In src/app/Window.py:

```
@staticmethod
    def __create():
        # proxy = "your_proxy_here"
        options = webdriver.ChromeOptions()
        options.add_argument('--incognito')
        # options.add_argument(f'--proxy-server=http://{proxy}')
        # options.add_argument("--disable-gpu")
        # options.add_argument("--headless=new")
        window = webdriver.Chrome(options=options)
        
        return window
```
*Uncomment line 12 and add your proxy, then uncomment line 15.

Install project dependencies

```
pip3 install -r requirements.txt
```

Run the application

```
python main.py
```

**warning**

```console
I would like to inform you that I am not responsible for the misuse of this tool, do not use it for malicious purposes.
```