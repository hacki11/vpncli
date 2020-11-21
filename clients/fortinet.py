import logging
import os
import subprocess


class FortiClient:

    def __init__(self, path, url, user, password):
        self.path = path
        self.url = url
        self.user = user
        self.password = password
        self.bin = os.path.join(path, "FortiSSLVPNclient.exe")

    def connect(self):
        logging.info('Connecting to ' + self.url)
        proc = subprocess.Popen([self.bin, 'connect',
                                 '-h' + self.url,
                                 '-u' + self.user + ':' + self.password,
                                 '-m'])
        try:
            proc.communicate(timeout=2)
        except subprocess.TimeoutExpired:
            # we do not care
            pass

    def disconnect(self):
        subprocess.Popen([self.bin, 'disconnect'])
