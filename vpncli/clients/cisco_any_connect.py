import logging
from subprocess import Popen, PIPE, STDOUT, TimeoutExpired
import os


class CiscoAnyConnect:

    def __init__(self, path, url, user, password):
        self.path = path
        self.url = url
        self.user = user
        self.password = password
        self.bin = os.path.join(path, "vpncli.exe")

    def connect(self):
        logging.info('Connecting to ' + self.url)
        proc = Popen([self.bin, 'connect', self.url, '-s'], stdout=PIPE, stdin=PIPE, stderr=STDOUT)

        try:
            stdout = proc.communicate(input=str(self.user + '\n' + self.password + '\n').encode(), timeout=2)[0]
            logging.debug(stdout.decode())
            proc.wait()
        except TimeoutExpired:
            # we do not care
            pass

    def disconnect(self):
        Popen([self.bin, 'disconnect'])
