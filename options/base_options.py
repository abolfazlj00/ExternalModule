from options.interface_options import IOptions
import os

class BaseOptions(IOptions):
    SERVICE_NAME = "serviceName"
    ROUTING_FOLDER = "routingFolder"
    HOST = "host"
    PORT = "port"
    SETTINGS = "settings"
    CACHE = "cache"
    
    def __init__(self, file_path: str) -> None:
        super().__init__()
        self._file_path = file_path
        if not os.path.isfile(self._file_path):
            raise FileNotFoundError(f"Options file not found!")        

