import os

from googleapiclient.discovery import build

API_KEY: str = os.getenv('YT_API_KEY')


class Video:
    """Класс для видео из ютуба"""

    def __init__(self, video_id):
        """Экземпляр инициализируется по id видео. Дальше все данные будут подтягиваться по API"""
        self.video_id = video_id
        youtube = self.get_service()
        self.video = youtube.videos().list(part="snippet,statistics", id=video_id).execute()
        snippet = self.video["items"][0]["snippet"]
        statistics = self.video["items"][0]["statistics"]
        self.video_name = snippet["title"]
        self.video_url = snippet["thumbnails"]["default"]["url"]
        self.video_view = statistics["viewCount"]
        self.video_like = statistics["likeCount"]

    def __repr__(self):
        """Выводит данные, полученные по API"""
        return str(self.video)

    def __str__(self):
        """Выводит название видео"""
        return self.video_name

    @classmethod
    def get_service(cls):
        """Возвращает объект для работы с YouTube API"""
        return build('youtube', 'v3', developerKey=API_KEY)


class PLVideo(Video):
    """Класс для плейлиста из ютуба"""

    def __init__(self, video_id, play_list_id):
        """Экземпляр инициализируется по id видео и плейлиста. Дальше все данные будут подтягиваться по API."""
        super().__init__(video_id)
        self.play_list_id = play_list_id
        youtube = self.get_service()
        self.play_list = youtube.playlists().list(part='contentDetails, snippet', id=play_list_id).execute()
