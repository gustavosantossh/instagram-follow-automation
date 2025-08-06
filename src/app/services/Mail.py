import requests
import random
import json
from src.app.config.Config import Config


class Mail:

    @staticmethod
    def getDomain() -> str:
        response = requests.get('https://api.mail.tm/domains')
        domain = response.json()['hydra:member'][0]['domain']
        return domain

    @staticmethod
    def randomMailAddress() -> str:
        hex_chars = '0123456789abcdef'
        chars = [random.choice(hex_chars) for _ in range(12)]
        return Config.ACC_EMAIL_PREFIX + "".join(chars)

    @staticmethod
    def createMailAccount() -> dict[str, str]:
        
        domain = Mail.getDomain()
        random_mail_address = Mail.randomMailAddress()

        email = random_mail_address + "@" + domain
        password = Config.ACC_PASSWORD

        response = requests.post('https://api.mail.tm/accounts', json={
            "address": email,
            "password": password
        })

        mail = response.json()['address']

        auth = Mail.getTmAuth(mail, password)

        content = {
            "mail": mail,
            "password": password,
            "id": auth['id'],
            "token": auth['token']
        }

        Mail.__save(content)
        return content

    @staticmethod
    def getTmAuth(email, password):
        response = requests.post('https://api.mail.tm/token', json={
            "address": email,
            "password": password
        })

        if response.ok:
            return response.json()

        return False

    @staticmethod
    def __save(content):
        data = []
        try:
            with open('./src/log/accounts.json', 'r') as f:
                data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            data = []

        data.append(content)

        with open('./src/log/accounts.json', 'w') as f:
            json.dump(data, f, indent=4)


    @staticmethod
    def getMessages(email):
        
        with open('./src/log/accounts.json', 'r') as f:
            contas = json.load(f)

        conta = [x for x in contas if x.get('mail') == email]

        if not conta:
            return False

        token = conta[0]['token']

        response = requests.get('https://api.mail.tm/messages', headers={
            "Authorization": f"Bearer {token}"
        })

        return response.json()
    
    @staticmethod
    def deleteAccount(id) -> bool:
        response = requests.delete(f'https://api.mail.tm//accounts/{id}')
        
        if response.status_code == 204:
            return True
        
        return False


print(
    Mail.createMailAccount()
)