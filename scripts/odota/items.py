import json

HERO="h"
ITEM="i"

def writeItems(names):
    result =[]
    for item in names:
        codes = []
        abcd=item[0:3]
        codes.append(abcd.lower())
        arr = item.split(" ")
        if len(arr) > 1:
            codes.append("".join([x[0:1].lower() for x in arr]))
        arr = item.split("-")
        if len(arr) > 1:
            codes.append("".join([x[0:1].lower() for x in arr]))
        for code in codes:
            result.append([item,f"{ITEM}{code}"])
    with open("item.txt","w+") as txt:
        txt.writelines([("	".join(line) + "\n") for line in result])
    return result
def main():
    with open("./items.json") as items:
        odota = json.load(items)
        names = []
        for item in odota.values():
            if 'dname' not in item:
                print(item)
            else:
                dname = item['dname']
                if '&' in dname:
                    dname=dname.replace("&","and")
                if ('(Shared)' not in dname ) and (' - ' not in dname) and ('Recipe' not in dname) and (':' not in dname):

                    names.append(dname)
        names = set(names)
        print(writeItems(names))
        print(len(names))

main()
