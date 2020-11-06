import time
import requests
import random
from data.config import VK_USERNAME, VK_PASSWORD

API_URL = "https://api.vk.com/method/"
version = "5.124"


class VK_API:
    user_token = ""
    owner_id = ""
    group_id = ""
    group_domain = ""

    def __init__(self, group_domain="copypastme", group_id="199593124", owner_id="-199593124", name=VK_USERNAME, password=VK_PASSWORD) -> None:
        """
        Set: group_domain, group_id, owner_id, name, password
        """
        self.user_token = self._get_user_AccessToken(name, password)
        self.owner_id = owner_id
        self.group_id = group_id
        self.group_domain = group_domain

    def _get_user_AccessToken(self, username: str, password: str) -> str:
        """
        Get user access token
        """
        return requests.post(
            "https://oauth.vk.com/token?grant_type=password",
            params={
                'client_id': '3697615',
                'client_secret': 'AlVXZFMUqyrnABp8ncuU',
                'username': username,
                'password': password
            }).json()["access_token"]

    def get_wall(self, count: int, offset=0):
        """
        Get JSON posts
        """
        count += offset
        posts = []

        while offset < count:
            posts.extend(
                requests.get(
                    API_URL + "wall.get",
                    params={
                        'access_token': self.user_token,
                        'v': version,
                        'domain': self.group_domain,
                        'count': count - offset,
                        'offset': offset
                    }).json()['response']['items'])
            offset += 100
            if count > 100:
                time.sleep(0.5)

        return posts

    def get_wall_search(self, query: str, count: int, offset=0):
        """
        Get searched JSON posts
        """
        count += offset
        posts = []

        while offset < count:
            posts.extend(
                requests.get(
                    API_URL + "wall.search",
                    params={
                        'access_token': self.user_token,
                        'v': version,
                        'domain': self.group_domain,
                        'query': f'"{query}"',
                        'owners_only': 1,
                        'count': count - offset,
                        'offset': offset
                    }).json()['response']['items'])
            offset += 100
            if count > 100:
                time.sleep(0.5)

        return posts

    def get_wall_photos(self, count: int):
        """
        Get mass of photos from wall
        """
        posts = self.get_wall(count)
        photos = []
        for post in posts:
            att = post['attachments'][0]
            if att['type'] == "photo":
                photos.append(att['photo']['sizes'][-1]['url'])
        return photos

    def get_wall_texts(self, count: int):
        """
        Get mass of texts from wall
        """
        posts = self.get_wall(count)
        texts = []
        for post in posts:
            if post['text'] != "":
                texts.append(post['text'])
        return texts

    def get_newsfeed(self, query: str, count: int):
        pass

    def get_newsfeed_search(self, query: str, count: int):
        """
        Get searched JSON posts from news feed
        """
        start_from = 0
        posts = []

        while start_from < count:
            posts.extend(
                requests.get(
                    API_URL + "newsfeed.search",
                    params={
                        'access_token': self.user_token,
                        'v': version,
                        'q': f'"{query}"',
                        'extended': 1,
                        'count': count - start_from,
                        'start_time': int(time.time()) - 86400,  # 3600,
                        # 'end_time': int(time.time()),
                        'start_from': start_from
                    }).json()['response']['items'])
            start_from += 200  # max 200
            if count > 100:
                time.sleep(0.5)

        return posts

    def send_wall_post(self, messages="", attachments=""):
        """
        Send post on wall
        And print post ID
        """
        response = requests.get(
            API_URL + "wall.post",
            params={
                'owner_id': self.owner_id,
                'message': messages,
                'attachments': attachments,
                'friends_only': 0,
                'from_group': 1,
                'signed': 0,
                'publish_date': int(time.time()) + 3600,
                'access_token': self.user_token,
                'v': version
            })

        print("Post #", response.json()['response']['post_id'])

    def CopyPosts(self, count: str, offset=0):
        posts = self.get_wall(count, offset)
        for post in posts:

            text = post['text']

            att = post['attachments'][0]
            if att['type'] == "photo":
                attachment = (
                    'photo'+str(
                        att['photo']['owner_id']
                    )+'_'+str(
                        att['photo']['id']
                    )+'&access_key='+str(
                        att['photo']['access_key']
                    ))
            elif att['type'] == "video":
                attachment = (
                    'photo'+str(
                        att['video']['owner_id']
                    )+'_'+str(
                        att['video']['id']
                    )+'&access_key='+str(
                        att['video']['access_key']
                    ))

            self.send_wall_post(text, attachment)

            if count <= 3:
                timer = 5
            elif count <= 10:
                timer = 600 + int(random.uniform(0, 120))  # 11 min +-1
            else:
                timer = 1800 + int(random.uniform(0, 360))  # 33 min +-3

            time.sleep(timer)


# a = VK_API().get_newsfeed_search(query="v", count=3)
# print(a)
# VK_API(group_domain="kusvjopky").CopyPosts(count=2, offset=100)
# a = VK_API(group_domain="kusvjopky").get_wall_search(query="может", count=100)
# print(a)
