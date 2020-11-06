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

    def get_videos(self):
        posts = self.get_posts()
        videos = []
        for post in posts:
            try:
                if post['attachments'][0]['type'] == "video":
                    owner_id = post['attachments'][0]['video']['owner_id'].split(
                        '-')[1]
                    id = post['attachments'][0]['video']['id']
                    video = f'https://vk.com/video-{owner_id}_{id}'
                    videos.append(video)
            except:
                pass
        return videos

    def get_texts(self):
        posts = self.get_posts()
        texts = []
        for post in posts:
            try:
                if post['text']:
                    text = post['text']
                    texts.append(text)
            except:
                pass
        return texts

    def get_albums(self):
        pass

# https://api.vk.com/method/video.get?videos=owner_id + _ + id + _ + access_key
# https://api.vk.com/method/video.get?videos=26086420_456241200_614d1cfb11f73a63d4_86e8512286e8512286e85122c1869c2076886e886e85122d961af523e9d750cb2459c25
# https://vk.com/video-56263398_456285706?list=61b6e7646bbef0b524
# https://vk.com/video-56263398_456285457?list=5507bfc060d09395f3
# f2e737b0cc4995e068
# video_ffdd234eIFQ6BIgg4iT27sCmoCjNMF4CmyF9ZnOv0beiwTIXJqMRfi9ujCbhIPzgy_mUHfsCZjevFEplF8o
# https://oauth.vk.com/authorize?client_id=*******&scope=notify,photos,friends,audio,video,notes,pages,docs,status,questions,offers,wall,groups,messages,notifications,stats,ads,offline,save&redirect_uri=http://api.vk.com/blank.html&display=page&v=5.68&response_type=token
