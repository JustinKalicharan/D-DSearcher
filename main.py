import xmltodict

xml = open('Complete.xml', encoding='utf-8').read()
DandD = xmltodict.parse(xml)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.



    for d in DandD['compendium']['item']:
        if d['name'] == 'Copper (cp)':
            print(f"{d['name']}, {d['text']}")



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm!!!!!')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
