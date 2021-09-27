# Problem 1
# DNS
# Program supports domain names starting with 'www' and ending with '.com', 'com.au', 'edu.au', 'gov.au', '.org'

# Variables
string = str
database = {}  # Dictionary for storing DNS
domainName = str
IPAddress = 0


# Create class for Domain Name Server (DNS)
class DNS:

    def __init__(self, domain, IPA):
        self._domain = domain
        self._IPA = IPA

    # Methods for DNS
    def updateDNS(self, dictionary):
        # Check and sort input strings for syntax
        if self._domain.startswith('www.') and self._domain.endswith('.com') or self._domain.endswith('.com.au') or \
                self._domain.endswith('.edu.au') or self._domain.endswith('.gov.au') or self._domain.endswith('.org'):
            if 1 < self._domain.count(".") < 4:  # Check number of full stops
                splitDomain = self._domain.split(".")  # Split input to check is alpha
                counter = 0
                for letters in splitDomain:
                    if letters.isalpha():
                        counter += 1
                    else:
                        break  # Check the split lines counter for
                if counter == len(splitDomain):  # is alpha equals length of list.
                    self._domain = '.'.join(splitDomain)  # Joins back together

                    if self._IPA.count(".") == 3:  # Check number of full stops
                        splitIPA = self._IPA.split(".")  # Split input to check is digit
                        for numbers in splitIPA:  # Convert to integer and check if lower
                            if numbers.isdigit():  # than 255 and join back together
                                numbers = int(numbers)
                                if numbers > 255:
                                    print("Incorrect IPA Format")
                                    break
                                self._IPA = '.'.join(splitIPA)
                            else:
                                print("Incorrect IPA Format")
                                break
                        dictionary[self._domain] = self._IPA
                        print("Updated DNS.", self._domain, self._IPA)
                    else:
                        print("Incorrect IPA Format")
                else:
                    print("Incorrect Domain Name Format")
            else:
                print("Incorrect Domain Name Format")
        else:
            print("Incorrect Domain Name Format")

    def returnIPA(self, dictionary):
        if self._domain in dictionary:
            value = dictionary[self._domain]
            return print("IP Address: ", value, "for Domain name: ", self._domain)
        else:
            return print(None)


class newDNS(DNS):
    bList = []  # list in class to be made a private attribute list

    # Defining subclass from superclass
    def __init__(self, bList, domain, IPA):
        super().__init__(domain, IPA)
        self.__bList = bList

    # New method for black list
    def blackList(self, IPA):
        self.__bList.append(IPA)

    def returnIPA(self, dictionary):
        if self._domain in dictionary:
            value = dictionary[self._domain]
            if value not in self.__bList:
                return print("IP Address: ", value, "for Domain name: ", self._domain)
            else:
                return print(None)
        else:
            return print(None)


while string != 'exit':
    try:
        # Create inputs in loop. Use class with inputs
        testInput = input("Type in desired function for DNS: update, blacklist, search or exit: ")

        # For updating DNS
        if testInput == 'update':
            domainName = input("Enter a Domain name: ")
            IPAddress = input("Enter an IP Address for the Domain name: ")
            result = DNS(domainName, IPAddress)  # Use class to get results
            result.updateDNS(database)
            # print(database)

        elif testInput == 'blacklist':
            IPAddress = input("Enter an IP Address for the Domain name: ")
            newResult = newDNS(newDNS.bList, domainName, IPAddress)
            newResult.blackList(IPAddress)
            try:
                print("Added to blacklist")
            except:
                print("Syntax Error")

        # For searching DNS
        elif testInput == 'search':
            domainName = input("Enter a Domain name: ")
            newResult = newDNS(newDNS.bList, domainName, IPAddress)  # Use class to get results
            newResult.returnIPA(database)

        # For exiting DNS
        elif testInput == 'exit':
            string = 'exit'

        else:
            print("Syntax Error")

    except:
        print("Syntax Error")
