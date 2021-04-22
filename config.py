# from libs.debugger import *


class Config():

    _config = {
        'DEV_DB': {
            'DATABASE': 'klime',
            'USER': 'klime',
            'PASSWORD': '1',
            'HOST': '127.0.0.1',
            'PORT': '5432',
        },
        'API_VERSIONS': [
            1, 2
        ],
        'ENDPOINTS': [
            'TASKS', 'views'
        ],
    }

    def get_value(self, keys):

        keys_count = len(keys)
        res = ''

        if keys_count <= 0:
            raise Exception('Count of keys must be >= 1')

        if keys_count == 1:
            return self._config.get(keys[0])

        if keys_count == 2:
            return self.get_value([keys[0]]).get(keys[1])

        #TODO
        # if keys_count >= 1:
        #     for key in range(keys_count):
        #     return self.get_value(keys[0])
