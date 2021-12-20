import contacts as ct

storage = ct.ContactsCollection()

class Action():
    def __init__(self, name):
        self.name = name
        
    def _get_storage():
        return storage
    
    def execute():
        print(len(storage.items))
    
class NewUserAction(Action):
    def __init__(self):
        self.name = "NEW_USER"
        
    def execute(self):
        contactName = input("Enter contact name: ")
        contactEmail = input("Enter contact email: ")
        contactPhoneNumber = input("Enter contact phone number: ")
        storage = Action._get_storage()
        
        contact = ct.Contact(storage.generate_id(), contactName, contactEmail, contactPhoneNumber)
        storage.items.append(contact)
        print(f"Contact has been saved. ID: '{contact.id}'")
        print(f"{len(storage.items)} item(s) in the storage.")
        
class UserDetailsAction(Action):
    def __init__(self, contactId):
        self.name = "USER_DETAILS"
        self.contactId = contactId
        
    def execute(self):
        contact = storage.find(self.contactId)
        if(contact == None):
            print(f"Not found the contact with ID '{self.contactId}'.")
        else:
            print(f"Contact info: '{contact.toString(True)}'")
            
class UserNameListAction(Action):
    def __init__(self):
        self.name = "USER_NAME_LIST"
        
    def execute(self):
        contacts = Action._get_storage().get_sorted_contacts(key='name')
        if(contacts == None or len(contacts) == 0):
            print("No stored contacts.")
            return
        
        for item in contacts:
            print(f"Contact info: '{item.toString(True)}'")
        
class AllUsersAction(Action):
    def __init__(self):
        self.name = "ALL_USERS"
        
    def execute(self):
        contacts = Action._get_storage().get_sorted_contacts(key='name')
        if(contacts == None):
            print("No stored contacts.")
            return
        for item in contacts:
            print(f"Contact info: '{item.toString()}'")
            
class DeleteUserAction(Action):
    def __init__(self, contactId):
        self.name = "DELETE_USER"
        self.contactId = contactId
        
    def execute(self):
        contact = storage.find(self.contactId)
        if(contact == None):
            print(f"Not found the contact with ID '{self.contactId}'")
            return
        
        storage.items.remove(contact)
        print("Contact has been removed from the storage.")
        
class DeleteUsersByIdListAction(Action):
    def __init__(self, contactIds):
        self.name = "DELETE_USERS_BY_IDS"
        self.contactIds = contactIds
        
    def execute(self):
        removedItems = 0
        for contactId in self.contactIds:    
            contact = storage.find(contactId)
            if(contact == None):
                print(f"Not found the contact with ID '{contactId}'")
                continue
            
            storage.items.remove(contact)
            removedItems += 1
        
        if(removedItems > 0):
            print(f"{removedItems} contact(s) have been removed from the storage.")
        
class DeleteUsersByIdRangeAction(Action):
    def __init__(self, start, end):
        self.name = "DELETE_USERS_BY_ID_RANGE"
        self.start = start
        self.end = end
        
    def execute(self):
        contactsToDelete = storage.get_by_id_range(self.start, self.end)
        if(contactsToDelete == None or len(contactsToDelete) == 0):
            print("No contacts to delete.")
        else:
            for contact in contactsToDelete:
                storage.items.remove(contact)
            print(f"Contacts with id in the range '{self.start} - {self.end}' have been removed.")