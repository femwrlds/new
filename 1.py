class Member: 
    def __init__(self,name,member_id):

        self.name = name 
        self.member_id = member_id

class StudentMember(Member): 
    def __init__(self, name, member_id):
        super().__init__(name, member_id)
        self.borrowed_books=0

        def add_books(self):
            self.borrowed_books += 1
            print(f"{self.name} has borrowed a new book. ")

        def return_book(self):
            if self.borrowed_books >0:
               self.borrowed_books -= 1
               print(f"{self.name} has returned a book. ")
            else: 
                print("No books to return. ")

        def display_status(self):
            print(f"{self.name} has borrowed {self.borrowed_books} books(s). ")
