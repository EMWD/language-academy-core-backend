from config import Config

class ApiVersionController():

    @staticmethod
    def get_value(key):
        config = Config()
        return config.get_value(key)
