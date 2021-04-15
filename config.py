
class Config():

    _config = {
        'API_VERSIONS': [
            1, 2
        ],
        'ENDPOINTS': [
            'tasks', 'views'
        ],
    }

    def get_value(self, key):
        return self._config.get(key)
