from libs.debugger import *

class Config():

    _config = {
        'DEV_DB': {
            'DATABASE': 'klime',
            'USER': 'klime',
            'PASSWORD': '1',
            'HOST': '127.0.0.1',
            'PORT': '5432',
        },
        'API_VERSIONS': {
            '1': 'api',
        },
        'API_ENDPOINTS': {
            '1': {
                'api/getall': 'get all api endpoints',
            },
        },
        'FAKE_USERS': {
            'Maxim': {
                'surname': 'Vtulkin',
                'group_name': 'two',
                'phone': '88005553535',
                'payment_date': '23232020',
                'lessons_left': '228',
            },
            'Gennadiy': {
                'surname': 'Rakin',
                'group_name': 'third',
                'phone': '78005553537',
                'payment_date': '13232020',
                'lessons_left': '342',
            },
        },
    }

    def get_value(self, keys):
        '''
        usage sample: get_value(['DEV_DB', 'DATABASE'])
        '''

        keys_count = len(keys)
        res = ''

        if keys_count <= 0:
            raise Exception('Count of keys must be >= 1')

        if keys_count == 1:
            return self._config.get(keys[0])

        if keys_count == 2:
            return self.get_value([keys[0]]).get(keys[1])

        #TODO
        # if keys_count >= n:

# Export Config instance
config = Config()