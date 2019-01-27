class User:
    '''
    Class that generates new users
    '''
    user_list=[]

    def __init__(self,firstname,email):
        '''
        defining properties for our object
        '''
        self.myfirstname=firstname
        self.myemail=email

    def save_user(self):
        '''
        save_user method saves user objects into user_list
        '''

        User.user_list.append(self)
        
    def delete_user(self):

        '''
        delete_user method deletes a saved user from the user_list
        '''

        User.user_list.remove(self)

    @classmethod
    def display_users(cls):
        '''
        method that returns the users list
        '''
        return cls.user_list
