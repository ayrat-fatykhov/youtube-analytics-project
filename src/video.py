from src.apimixin import APIMixin


class Video(APIMixin):
    """Класс для видео из ютуба"""

    def __init__(self, video_id):
        """Экземпляр инициализируется по id видео. Дальше все данные будут подтягиваться по API"""
        self.video_id = video_id
        try:
            youtube = self.get_service()
            self.video = youtube.videos().list(part="snippet,statistics", id=video_id).execute()
            snippet = self.video["items"][0]["snippet"]
            statistics = self.video["items"][0]["statistics"]
            self.video_name = snippet["title"]
            self.video_url = snippet["thumbnails"]["default"]["url"]
            self.video_view = statistics["viewCount"]
            self.video_like = statistics["likeCount"]
        except IndexError:
            self.video_name = None
            self.video_view = None
            self.video_like = None

    def __repr__(self):
        """Выводит данные, полученные по API"""
        return str(self.video)

    def __str__(self):
        """Выводит название видео"""
        return self.video_name


class PLVideo(Video):
    """Класс для плейлиста из ютуба"""

    def __init__(self, video_id, play_list_id):
        """Экземпляр инициализируется по id видео и плейлиста. Дальше все данные будут подтягиваться по API."""
        super().__init__(video_id)
        self.play_list_id = play_list_id
        youtube = self.get_service()
        self.play_list = youtube.playlists().list(part='contentDetails, snippet', id=play_list_id).execute()
