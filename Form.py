class Form:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.is_valid = False

    def __str__(self):
        return f"name={self.name}, address={self.address} is_valid={self.is_valid}"

    def validate_form(self):
        print("base form")
        if self.name != "" and self.address != "":
            self.is_valid = True
        else:
            self.is_valid = False

    def submit(self):
        if self.is_valid:
            print("success")
        else:
            print("failure")

    def run(self):
        self.validate_form()
        self.submit()
