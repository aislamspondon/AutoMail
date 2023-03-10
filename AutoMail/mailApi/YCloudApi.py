import requests

API_URL = "https://api.ycloud.com/v2/emails"

class YCloudAPI:

    def mail_api(self,api, sendermail, receiver, subject, content):
        API_KEY = api
        payload = {
        "from": f"{sendermail}",
        "to":  receiver,
        "subject": subject,
        "content": content,
        "contentType": "text/html"
        }
        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "X-API-Key": API_KEY
        }

        response = requests.post(API_URL, json=payload, headers=headers)

        if response.status_code == 200:
            return True
        else:
            return False