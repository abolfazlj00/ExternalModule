from options.base_options import BaseOptions

class JsonBaseOptions(BaseOptions):

    def __init__(self, file_path: str) -> None:
        super().__init__(file_path)

    