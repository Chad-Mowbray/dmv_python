from Form import Form


class DriversLicenseForm(Form):
    def __init__(self, name, address):
        super().__init__(name, address)


dl = DriversLicenseForm("Bob", "123 Main")
dl.run()
print(dl)
