import actions as ac

def parse_action(enteredAction: str):
    if(enteredAction == 'exit'):
        return ac.Action('EXIT')
    elif(enteredAction == 'new_user'):
        return ac.NewUserAction()
    elif(enteredAction == 'all'):
        return ac.AllUsersAction()
    elif(enteredAction.startswith('user id')):
        contactId = enteredAction.replace('user id ', '')
        return ac.UserDetailsAction(contactId)
    elif(enteredAction.startswith('user name')):
        return ac.UserNameListAction()
    elif(enteredAction.startswith('del_user')):
        options = enteredAction.replace('del_user ', '')
        if(options.find(",") == -1 and options.find("-") == -1):
            return ac.DeleteUserAction(options)
        elif(options.find(",") != -1):
            ids = options.split(',')
            return ac.DeleteUsersByIdListAction(ids)
        elif(options.find("-") != -1):
            idRange = options.split('-')
            return ac.DeleteUsersByIdRangeAction(int(idRange[0]), int(idRange[1]))

# main code

while(True):
    action = parse_action(input('Please select action: '))
    if(action.name == 'EXIT'):
        break
    
    action.execute()
    