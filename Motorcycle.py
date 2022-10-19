from Form import Form


class MotorcycleLicenseForm(Form):
    def __init__(self, name, address, qualified):
        super().__init__(name, address)
        self.qualified = qualified

    def validate_form(self):
        print("motorcycle")
        super().validate_form()
        print(self.is_valid)
        if self.is_valid and self.qualified:
            self.is_valid = True
        else:
            self.is_valid = False


ml = MotorcycleLicenseForm("Bob", "123 Main", True)
ml.run()
print(ml)
