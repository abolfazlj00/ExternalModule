from abc import abstractmethod
from options.data_model import Options

class IOptions:

    @abstractmethod
    def initialize(self) -> Options: ...