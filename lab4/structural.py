from abc import ABC, abstractmethod
import time, random

cache = {}

class Video(ABC):

    @abstractmethod
    def downloading(self) -> None:
        pass


class RealVideo(Video):
    def __init__(self, name):
        self.name = name

    def downloading(self) -> None:
        print("Начало скачивания...")
        time.sleep(3)
        print("Скачивание завершено.")
        cache.update({self.name:random.randrange(10000, 99999)})


class Proxy(Video):
    def __init__(self, real_subject: RealVideo) -> None:
        self._real_subject = real_subject

    def downloading(self) -> None:
        if self.check_cache():
            self.cache_access()
        else:
            self._real_subject.downloading()

    def check_cache(self) -> bool:
        print("Поиск видео в кэше...")
        return self._real_subject.name in cache

    def cache_access(self) -> None:
        print("Видео найдено в кэше.")


def client_code(subject: Video) -> None:

    # ...

    subject.downloading()

    # ...


if __name__ == "__main__":
    print("Без кэша...")
    print("Видео1:")
    real_subject1 = RealVideo("video1")
    client_code(real_subject1)
    print("Видео2:")
    real_subject2 = RealVideo("video2")
    client_code(real_subject2)
    print("Видео1:")
    client_code(real_subject1)

    print("")

    print("С кэшем...")
    print("Видео3:")
    real_subject3 = RealVideo("video3")
    proxy = Proxy(real_subject3)
    client_code(proxy)
    print("Видео4:")
    real_subject4 = RealVideo("video4")
    proxy = Proxy(real_subject4)
    client_code(proxy)
    print("Видео3:")
    proxy = Proxy(real_subject3)
    client_code(proxy)