import xmltodict

xml = open('Complete.xml', encoding='utf-8').read()
DandD = xmltodict.parse(xml)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    for thing in DandD['compendium']['item']:
        print(f"{thing['name']}")



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm!!!!!')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
