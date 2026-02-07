#Problem Statement
#Create a program for an Instagram Account System using Encapsulation.

class InstagramAccount:
    def __init__(self, account_name, password):
        self.account_name = account_name          
        self._private_reels = []                  
        self.__archived_reels = []                 
        self.__password = password                 

    
    def add_private_reel(self, reel_name):
        self._private_reels.append(reel_name)

    
    def display_private_reels(self, is_follower):
        if is_follower:
            print("Private Reels:", self._private_reels)
        else:
            print("Access Denied! Only followers can view private reels")

    
    def add_archived_reel(self, reel_name):
        self.__archived_reels.append(reel_name)

    
    def display_archived_reels(self, password):
        if password == self.__password:
            print("Archived Reels:", self.__archived_reels)
        else:
            print("Access Denied! Only account holder can view archived reels")

    
    def get_archived_reels(self, password):
        if password == self.__password:
            return self.__archived_reels
        else:
            return "Access Denied!"

    
    def set_password(self, old_password, new_password):
        if old_password == self.__password:
            self.__password = new_password
            print("Password updated successfully")
        else:
            print("Wrong password! Cannot update")

# Object Creation and Testing
# Create object
insta = InstagramAccount("atom_official", "1234")

# Add private reels
insta.add_private_reel("Gym Reel")
insta.add_private_reel("Travel Reel")

# Add archived reels
insta.add_archived_reel("Old Dance Reel")
insta.add_archived_reel("Memories Reel")

# Display private reels
insta.display_private_reels(True)     
insta.display_private_reels(False)    

# Display archived reels
insta.display_archived_reels("1234")  
insta.display_archived_reels("0000") 

# Update password
insta.set_password("1234", "abcd")

# Check again with new password
insta.display_archived_reels("abcd")






