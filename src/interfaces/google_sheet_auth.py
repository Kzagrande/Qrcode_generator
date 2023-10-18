from abc import ABC,abstractmethod
from googleapiclient.discovery import Resource


class GoogleSheetAuthInterface(ABC):
    
    @abstractmethod
    def get_service(self) -> Resource:
        pass
