import xmltodict
import helper.compendium as DnD5e


xml = open('Complete.xml', encoding='utf-8').read()
DandD = xmltodict.parse(xml)


def main():
    # Use a breakpoint in the code line below to debug your script.
    comp = DnD5e.Compendium()

    comp.testing()
    items = {}

    for d in DandD['compendium']['item']:
        try:
            name = d['name']
        except:
            name = "None"

        try:
            type = d['type']
        except:
            type = "None"

        try:
            weight = d['weight']
        except:
            weight = 0

        try:
            text = d['text']
        except:
            text = ""

        try:
            value = d['value']
        except:
            value = 0

        try:
            roll = d['roll']
        except:
            roll = ""

        try:
            items[name] = DnD5e.Items(name, type, weight, text, value, roll)
            print(items[name].name, items[name].type, items[name].weight, items[name].value, items[name].roll)
        except:
            print("Could not create item")

        #if d['name'] == 'Copper (cp)':
            #print(f"{d['name']}, {d['text']}")



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()





