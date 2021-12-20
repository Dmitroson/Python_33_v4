import operator

class ContactsCollection():
    __last_id = 0
    
    def __init__(self):
        self.items = []
    
    def generate_id(self):
        self.__last_id += 1
        return self.__last_id
    
    def find(self, contactId):
        for item in self.items:
            if(str(item.id) == contactId):
                return item
        return None
    
    def get_sorted_contacts(self, key):
        if(key == 'name'):
            return sorted(self.items, key=operator.attrgetter('name'))
        else:
            return sorted(self.items, key=operator.attrgetter('id'))
        
    def get_by_id_range(self, start, end):
        contacts = self.get_sorted_contacts('id')
        result = []
        for contact in contacts:
            if(contact.id >= start and contact.id <= end):
                result.append(contact)
        return result
    
class Contact():
    def __init__(self, generated_id, name, email, phoneNumber):
        self.id = generated_id
        self.name = name
        self.email = email
        self.phoneNumber = phoneNumber
        
    def toString(self, fullInfo=False):
        if(fullInfo):
            return f"Id: {self.id}, Name: {self.name}, Email: {self.email}, Phone number: {self.phoneNumber}"
        else:
            return f"Name: {self.name}, Email: {self.email}, Phone number: {self.phoneNumber}"