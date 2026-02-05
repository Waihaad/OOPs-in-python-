class Project:
    def __init__(self, creator_name, location):
        
        self.creator_name = creator_name
        
        
        self.location = location
        
        
        self.comments = []

    
    def add_comment(self, comment):
        self.comments.append(comment)

    
    def display_comments(self):
        if not self.comments:
            print("No comments available.")
        else:
            print("Comments:")
            for comment in self.comments:
                print("-", comment)

    
    def display_creator_name(self):
        print("Creator Name:", self.creator_name)

    
    def display_location(self):
        print("Location:", self.location)



project1 = Project("ATOM", "Mysore")

project1.add_comment("Good project design")
project1.add_comment("Needs optimization")


project1.display_creator_name()
project1.display_location()
project1.display_comments()
