import sys
import netifaces
import winreg

"""
Note: It maybe be possible to find the right interface without using winreg
Check the netifaces docs, remember . . .
AF_LINK = ethernet
AF_INET = normal ip - ipv4
AF_INET6 = ipv6
Need to find Wifi AF

Could loop through each and check if either ethernet or wifi
using the appropiate AF variable
"""

# Find out what OS user is running and return parsed Ethernet/Wi-Fi interfaces
def findLocalInterfaces(self):
    # Windows
    if sys.platform == "win32":

        parsedInterfaces = {}

        # Store list of interfaces
        interfaces = netifaces.interfaces()

        # Set up registry vars to search interface names
        reg = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)
        reg_key = winreg.OpenKey(reg, r'SYSTEM\CurrentControlSet\Control\Network\{4d36e972-e325-11ce-bfc1-08002be10318}')
        
        # Find Ethernet/Wi-Fi interfaces
        # Loop over interfaces and get type, ip
        for i in range(len(interfaces)):
            try:
                reg_subkey = winreg.OpenKey(reg_key, interfaces[i] + r'\Connection')

                # Check for wifi or ethernet adapters
                if winreg.QueryValueEx(reg_subkey, "Name")[0] == "Ethernet" or winreg.QueryValueEx(reg_subkey, "Name")[0] == "Wi-Fi":
                    
                    interfaceType = winreg.QueryValueEx(reg_subkey, "Name")[0] # Ethernet or Wi-Fi

                    # Get detailed interface information on particular interface
                    interfaceAddresses = netifaces.ifaddresses(interfaces[i])

                    # Loop over detailed interface list and return IP
                    for key, value in interfaceAddresses.items():

                        # If number is 
                        if key == netifaces.AF_INET:

                            for addrType, val in value[0].items():

                                if addrType == "addr":
                                    parsedInterfaces[interfaceType] = val

            except FileNotFoundError:
                pass

    # Linux/OSX
    elif sys.platform == "linux" or sys.platform == "darwin":
        # set up linux later - necessary for RPI testing
        print("Add linux functionality doofus")

    return parsedInterfaces
