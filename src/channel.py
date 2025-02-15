import json

from src.apimixin import APIMixin


class Channel(APIMixin):
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

    def __str__(self) -> str:
        """Возвращает название и ссылку на канал по шаблону"""
        return f"{self.title} ({self.url})"

    def __add__(self, other) -> int:
        """Возвращает результат сложения количества подписчиков"""
        return int(self.channel_subscribers) + int(other.channel_subscribers)

    def __sub__(self, other) -> int:
        """Возвращает результат вычитания количества подписчиков"""
        return int(self.channel_subscribers) - int(other.channel_subscribers)

    def __gt__(self, other) -> bool:
        """Возвращает результат сравнения (меньше) количества подписчиков"""
        return int(self.channel_subscribers) > int(other.channel_subscribers)

    def __ge__(self, other) -> bool:
        """Возвращает результат сравнения (меньше или равно) количества подписчиков"""
        return int(self.channel_subscribers) >= int(other.channel_subscribers)

    def __lt__(self, other) -> bool:
        """Возвращает результат сравнения (больше) количества подписчиков"""
        return int(self.channel_subscribers) < int(other.channel_subscribers)

    def __le__(self, other) -> bool:
        """Возвращает результат сравнения (больше или равно) количества подписчиков"""
        return int(self.channel_subscribers) <= int(other.channel_subscribers)

    def __eq__(self, other) -> bool:
        """Возвращает результат сравнения (равно) количества подписчиков"""
        return int(self.channel_subscribers) == int(other.channel_subscribers)

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(json.dumps(self.channel))

    def to_json(self, file_name) -> None:
        """Сохраняет в файл значения атрибутов экземпляра Channel"""
        date = {'title': self.title, 'video_count': self.video_count, 'url': self.url}
        with open(file_name, 'w') as file:
            json.dump(date, file)
