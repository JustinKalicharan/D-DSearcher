class Compendium(object):

    def testing(self):
        print("Testing the Compendium")


class Items(object):

    def __init__(self, name, item_type, weight, text, value, roll):
        try:
            self.name = name
        except:
            print("No Name defined")
            self.name = ""

        try:
            self.type = item_type
        except:
            print("No Type defined")
            self.type = ""

        try:
            self.weight = weight
        except:
            print("No weight defined")
            self.weight = 0

        try:
            self.text = text
        except:
            print("No text defined")
            self.text = ""

        try:
            self.value = value
        except:
            print("No value defined")
            self.value = 0

        try:
            self.roll = roll
        except:
            print("No roll defined")
            self.roll = ""





