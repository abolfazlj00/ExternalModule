from options.base_options import BaseOptions
from options.data_model import Options
import yaml

class YamlBaseOptions(BaseOptions):

    def __init__(self, file_path: str) -> None:
        super().__init__(file_path)


    def initialize(self) -> Options:
        with open(self._file_path) as file:
            self.__json_data = yaml.load(file, Loader=yaml.SafeLoader)
        
        return Options(
            self.__json_data[BaseOptions.SERVICE_NAME],
            self.__json_data[BaseOptions.ROUTING_FOLDER],
            self.__json_data[BaseOptions.HOST],
            int(self.__json_data[BaseOptions.PORT]),
            self.__json_data[BaseOptions.SETTINGS],
            self.__json_data[BaseOptions.CACHE]
        )
        