from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Subject(ABC):

    @abstractmethod
    def follow(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def unfollow(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass


class SportNews(Subject):

    _state: str = None

    _observers: List[Observer] = []

    def follow(self, observer: Observer) -> None:
        print("Новый подписчик.")
        self._observers.append(observer)

    def unfollow(self, observer: Observer) -> None:
        print("Пользователь отписался.")
        self._observers.remove(observer)

    def notify(self) -> None:

        print("Отправка уведомлений...")
        for observer in self._observers:
            observer.update(self)

    def some_logic(self, new) -> None:

        print("\nСобытие в мире спорта.")
        self._state = new

        print(f"{self._state}: выпуск новой новости.")
        self.notify()


class Observer(ABC):

    @abstractmethod
    def update(self, subject: Subject) -> None:
        pass


class FootballObserver(Observer):
    def update(self, subject: Subject) -> None:
        if subject._state == 'Футбол':
            print("Футбольный болельщик получил уведомление.")


class HockeyObserver(Observer):
    def update(self, subject: Subject) -> None:
        if subject._state == 'Хоккей':
            print("Хоккейный болельщик получил уведомление.")


if __name__ == "__main__":

    subject = SportNews()

    observer_a = FootballObserver()
    subject.follow(observer_a)

    observer_b = HockeyObserver()
    subject.follow(observer_b)

    subject.some_logic('Футбол')
    subject.some_logic('Хоккей')

    subject.unfollow(observer_a)

    subject.some_logic('Футбол')
