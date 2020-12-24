from __future__ import annotations
from abc import ABC, abstractmethod, abstractproperty
from typing import Any


class Builder(ABC):

    @abstractproperty
    def car(self) -> None:
        pass

    @abstractmethod
    def buildCarBody(self) -> None:
        pass

    @abstractmethod
    def setEngine(self) -> None:
        pass

    @abstractmethod
    def setTransmission(self) -> None:
        pass

    @abstractmethod
    def setCruiseControl(self) -> None:
        pass

    @abstractmethod
    def setAirConditioning(self) -> None:
        pass


class SedanCarBuilder(Builder):

    def __init__(self) -> None:
        """
        Новый экземпляр строителя должен содержать пустой объект продукта,
        который используется в дальнейшей сборке.
        """
        self.reset()

    def reset(self) -> None:
        self._product = Product1()

    @property
    def car(self) -> Product1:
        car = self._product
        self.reset()
        return car

    def buildCarBody(self) -> None:
        self._product.add("Sedan")

    def setEngine(self) -> None:
        self._product.add("VR38DETT")

    def setTransmission(self) -> None:
        self._product.add("6-speed dual-clutch")

    def setCruiseControl(self) -> None:
        self._product.add("Cruise Control")

    def setAirConditioning(self) -> None:
        self._product.add("Air Conditioning")


class HatchbackCarBuilder(Builder):

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._product = Product1()

    @property
    def car(self) -> Product1:
        car = self._product
        self.reset()
        return car

    def buildCarBody(self) -> None:
        self._product.add("Hatchback")

    def setEngine(self) -> None:
        self._product.add("VR38DETT")

    def setTransmission(self) -> None:
        self._product.add("6-speed dual-clutch")

    def setCruiseControl(self) -> None:
        self._product.add("Cruise Control")

    def setAirConditioning(self) -> None:
        self._product.add("Air Conditioning")


class Product1():

    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self):
        print(f"Product parts: {', '.join(self.parts)}", end="")
        return self.parts


class Director:

    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        self._builder = builder

    def build_minimal_version_car(self) -> None:
        self.builder.buildCarBody()
        self.builder.setEngine()
        self.builder.setTransmission()

    def build_full_version_car(self) -> None:
        self.builder.buildCarBody()
        self.builder.setEngine()
        self.builder.setTransmission()
        self.builder.setCruiseControl()
        self.builder.setAirConditioning()


if __name__ == "__main__":

    director = Director()

    print("Sedans: ")
    builder = SedanCarBuilder()
    director.builder = builder

    print("Standard basic car: ")
    director.build_minimal_version_car()
    builder.car.list_parts()

    print("\n")

    print("Standard full version car: ")
    director.build_full_version_car()
    builder.car.list_parts()

    print("\n")

    print("Hatchbacks: ")
    builder = HatchbackCarBuilder()
    director.builder = builder

    print("Standard basic car: ")
    director.build_minimal_version_car()
    builder.car.list_parts()

    print("\n")

    print("Standard full version car: ")
    director.build_full_version_car()
    builder.car.list_parts()

    print("\n")

    print("Custom hatchback car: ")
    builder.buildCarBody()
    builder.setEngine()
    builder.setTransmission()
    builder.setAirConditioning()
    builder.car.list_parts()
