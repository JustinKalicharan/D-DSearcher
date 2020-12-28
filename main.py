import xmltodict
import helper.compendium as DnD5e


xml = open('Complete.xml', encoding='utf-8').read()
DandD = xmltodict.parse(xml)


def main():
    # Use a breakpoint in the code line below to debug your script.
    comp = DnD5e.Compendium()
    comp.testing()


    for d in DandD['compendium']['item']:
        if d['name'] == 'Copper (cp)':
            print(f"{d['name']}, {d['text']}")



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()





