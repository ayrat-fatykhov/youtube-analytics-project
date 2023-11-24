import json
import os
from googleapiclient.discovery import build
API_KEY: str = os.getenv('YT_API_KEY')


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        youtube = self.get_service()
        self.channel = youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
        snippet = self.channel["items"][0]["snippet"]
        statistics = self.channel["items"][0]["statistics"]
        self.title = snippet["title"]
        self.channel_description = snippet["description"]
        self.url = snippet["thumbnails"]["default"]["url"]
        self.channel_subscribers = statistics["subscriberCount"]
        self.video_count = statistics["videoCount"]
        self.channel_views = statistics["viewCount"]

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(json.dumps(self.channel))

    @classmethod
    def get_service(cls):
        youtube = build('youtube', 'v3', developerKey=API_KEY)
        return youtube

    def to_json(self, file_name):
        date = {'title': self.title, 'video_count': self.video_count, 'url': self.url}
        with open(file_name, 'w') as file:
            json.dump(date, file)
