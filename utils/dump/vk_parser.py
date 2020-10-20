import time
import requests

from data.config import VK_APP_TOKEN


class GetVK:
    token = VK_APP_TOKEN
    version = 5.92
    offset = 0

    def __init__(self, group, count=100):
        self.domain = group
        self.count = count

    def get_posts(self):
        posts = []
        while self.offset < self.count:
            response = requests.get('https://api.vk.com/method/wall.get',
                                    params={
                                        'access_token': self.token,
                                        'v': self.version,
                                        'domain': self.domain,
                                        'count': self.count - self.offset,
                                        'offset': self.offset
                                    })
            self.offset += 100
            post = response.json()['response']['items']
            posts.extend(post)
            time.sleep(0.5)
        return posts

    def get_photos(self):
        posts = self.get_posts()
        photos = []
        for post in posts:
            try:
                if post['attachments'][0]['type'] == "photo":
                    photo = post['attachments'][0]['photo']['sizes'][-1]['url']
                    photos.append(photo)
            except:
                pass
        return photos

    def new_photos(self):
        photos = self.get_photos()

        with open('databases/links.txt', 'r+') as f:
            if f.readline(1) != photos[-1]:
                return False
            else:
                f.write(photos[-1])
                return photos[-1]
