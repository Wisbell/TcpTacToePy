def parseLanGameChoice(self, choice, interfaces):
        # Manually input ip if no interfaces or Manual choice chosen
        if interfaces == None or int(choice) == len(interfaces) + 1:
            self.showGetManualIP()
        # Go back to LAN game menu
        elif int(choice) == len(interfaces) + 2:
            self.showCreateGameMenu()
        # Loop over interfaces and find iface that was chosen
        else:
            for i, iface in enumerate(interfaces.items()):
                if int(choice) == i + 1:
                    self.choosePort(iface[1])