from abc import ABC, abstractmethod

class BaseAgent(ABC):
    @abstractmethod
    def execute(self, mcs_string: str):
        pass
