# import netifaces

# def network(interface=None):
#     if interface:
#         try:
#             netifaces.ifaddresses(interface)
#             interfaces = [interface]
#         except ValueError:
#             return {"message": "interface {} not available".format(interface)}
#     else:
#         interfaces = netifaces.interfaces()

#     data = dict()
#     for i in interfaces:
#         try:
#             data[i] = netifaces.ifaddresses(i)[2]
#         except KeyError:
#             data[i] = {"message": "AF_INET data missing"}
#     return data

# print(network())



import netifaces as ni
import winreg as wr
from pprint import pprint

def get_connection_name_from_guid(iface_guids):
    iface_names = ['(unknown)' for i in range(len(iface_guids))]
    reg = wr.ConnectRegistry(None, wr.HKEY_LOCAL_MACHINE)
    reg_key = wr.OpenKey(reg, r'SYSTEM\CurrentControlSet\Control\Network\{4d36e972-e325-11ce-bfc1-08002be10318}')
    for i in range(len(iface_guids)):
        try:
            reg_subkey = wr.OpenKey(reg_key, iface_guids[i] + r'\Connection')
            iface_names[i] = wr.QueryValueEx(reg_subkey, 'Name')[0]
        except FileNotFoundError:
            pass
    return iface_names

x = ni.interfaces()
pprint(get_connection_name_from_guid(x))