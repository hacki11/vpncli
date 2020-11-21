import configparser
import argparse
import logging
import sys

from vpncli.connectivity import wait_for_connection, wait_until_unreachable
from vpncli.clients.fortinet import FortiClient
from vpncli.clients.cisco_any_connect import CiscoAnyConnect
from vpncli.credentials.keepass import KeePass


def connect(site):
    test_address = config.get(site, 'testAddress')
    logging.info("Connect to " + site)
    client = create_client(site)
    client.connect()
    if wait_for_connection(test_address) == 0:
        logging.info("Connection established.")
    else:
        raise Exception("Could not establish connection to " + site)


def disconnect(site):
    logging.info("Disconnect from " + site)
    client = create_client(site)
    client.disconnect()
    if wait_until_unreachable(config.get(site, 'testAddress')) == 0:
        logging.info("Disconnected successfully")
    else:
        raise Exception("Could not disconnect from " + site)


def switch(site):
    logging.info("Switching to " + site)
    dis_sites = config.sections()
    dis_sites.remove(site)
    for site in dis_sites:
        disconnect(site)

    connect(site)
    logging.info("Switched successfully to " + site)


def create_client(site):
    client_type = config.get(site, 'type')

    if 'fortinet' == client_type:
        creds = cred_provider.get(config.get(site, 'server'))
        return FortiClient(config.get(site, 'clientPath'),
                           config.get(site, 'server'),
                           creds.login,
                           creds.password)

    elif 'cisco' == client_type:
        creds = cred_provider.get(config.get(site, 'server'))
        return CiscoAnyConnect(config.get(site, 'clientPath'),
                               config.get(site, 'server'),
                               creds.login,
                               creds.password)

    else:
        raise Exception("VPN client type '" + client_type + "' not supported.")


def create_cred_provider(type):
    if 'keepass' == type:
        return KeePass()
    else:
        raise Exception("Credential provider '" + type + "' not supported.")


if __name__ == '__main__':

    logging.basicConfig(format=logging.BASIC_FORMAT, stream=sys.stdout, level=logging.DEBUG)
    parser = argparse.ArgumentParser(description='Generic VPN client command line')

    mux = parser.add_mutually_exclusive_group()
    mux.add_argument("-c", '--connect', metavar='site', help='Connect to a clients site')
    mux.add_argument("-d", '--disconnect', metavar='site', help='Disconnect from a clients site')
    mux.add_argument("-s", '--switch', metavar='site', help='Switch to a clients site')
    parser.add_argument("-f", "--file", required=False, help='Configuration file (default: vpn.ini)', default='vpn.ini')

    config = configparser.ConfigParser()

    args = parser.parse_args()
    config.read(args.file)
    cred_provider = create_cred_provider('keepass')

    if args.connect:
        connect(args.connect)
    elif args.disconnect:
        disconnect(args.disconnect)
    elif args.switch:
        switch(args.switch)
