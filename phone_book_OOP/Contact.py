class Contact:
    def __init__(self, first_name: str, last_name: str, phone_number: str, comment: str):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.comment = comment

    def __str__(self):
        print(f'{self.first_name} {self.last_name:<16} | {self.phone_number:<14} | {self.comment:<20}')

    def to_str(self):
        return f'{self.first_name};{self.last_name};{self.phone_number};{self.comment}'


