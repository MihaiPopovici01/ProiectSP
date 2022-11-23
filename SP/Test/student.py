class Student:
    def __init__(self, nume, email):
        self.nume = nume
        self.email = email

    def __str__(self):
        str = "Nume " + self.nume + ", Email: " + self.email
        return str
        
        
   