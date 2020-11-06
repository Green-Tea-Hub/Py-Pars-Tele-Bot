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
        post_time_out = int(time.time()) + 4500
        attachments = "https://sun9-65.userapi.com/ukMulUNq6vnvP-M_SQF5tKKQYRggeTJ60WcdrA/E4PjNCio8WA.jpg"
        # "https://gosut0.files.wordpress.com/2018/09/ivi4.png?w=740"
        # "photo-153384330_457289560"
        # https://vk.com/photo-199593124_457239050
        # photo100172_166443618,photo-1_265827614
        try:
            response = requests.get('https://api.vk.com/method/wall.post'
                                    f'?owner_id=-{self.owner_id}'
                                    f'&message={messages}'
                                    f'&attachments={attachments}'
                                    # '&friends_only=1'
                                    '&from_group=1'
                                    '&signed=0'
                                    f'&publish_date={post_time_out}'
                                    f'&access_token={access_token}&v=5.124'
                                    ).json()
            return response

        except:
            return 'ERROR -> POSTING BREAK'
