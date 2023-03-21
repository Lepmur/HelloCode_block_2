class Contact:
    def __init__(self, last_name: str, first_name: str, phone_number: str, comment: str):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.comment = comment

    def __str__(self):
        return f'{(self.last_name + " " + self.first_name):<20} | {self.phone_number:<14} | {self.comment:<20}'

    def to_str(self):
        return f'{self.last_name};{self.first_name};{self.phone_number};{self.comment}'


