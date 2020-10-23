import time
import requests

from data.config import VK_USERNAME, VK_PASSWORD


class PostVK:
    """Posting in group VK"""

    def __init__(self, group_id):
        self.owner_id = group_id

    def getAccessToken(self):
        response = requests.post(
            f'https://oauth.vk.com/token?grant_type=password&client_id=3697615&client_secret=AlVXZFMUqyrnABp8ncuU&username={VK_USERNAME}&password={VK_PASSWORD}').json()

        return response["access_token"]

    def postMedia(self, messages):
        access_token = self.getAccessToken()

        try:
            response = requests.get('https://api.vk.com/method/wall.post'
                                    f'?owner_id=-{self.owner_id}'
                                    f'&message={messages}'
                                    # f'&attachments={attachments}'
                                    '&from_group=0'
                                    f'&access_token={access_token}&v=5.124'
                                    ).json()
            return response

        except:
            return 'ERROR -> POSTING BREAK'
