import requests

API_KEY = "fb627db9268792b4117e101b8a6ba398"
API_URL = "https://api.ycloud.com/v2/emails"

class YCloudAPI:

    def mail_api(self, sendermail, receiver, subject, content):
        payload = {
        "from": f"{sendermail}@billboss.online",
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