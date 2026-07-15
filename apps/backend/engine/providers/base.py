from abc import ABC, abstractmethod

class BaseProvider(ABC):

    @abstractmethod
    def build_prompt(self, scene: dict, camera: dict) -> str:
        pass

    @abstractmethod
    def workflow(self) -> dict:
        pass

    @abstractmethod
    def name(self) -> str:
        pass
