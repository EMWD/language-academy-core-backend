import socket


class IpResolver():

    def get_hostname(self):
        return socket.gethostname()

    def get_host_addres(self):
        return socket.gethostbyname(socket.gethostname())

    def get_current_config_db_value(self):
        current_config_value = 'PROD_DB'
        current_addres = self.get_host_addres()

        if current_addres == '127.0.0.1' or current_addres == '127.0.1.1':
            current_config_value = 'DEV_DB'

        return current_config_value


ipr = IpResolver()
