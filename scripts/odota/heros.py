import json

HERO="h"
ITEM="i"

def writeHeros(names):
    result =[]
    for hero in names:
        codes = []
        abcd=hero[0:3]
        codes.append(abcd.lower())
        arr = hero.split(" ")
        if len(arr) > 1:
            codes.append("".join([x[0:1].lower() for x in arr]))
        arr = hero.split("-")
        if len(arr) > 1:
            codes.append("".join([x[0:1].lower() for x in arr]))
        for code in codes:
            result.append([hero,f"{HERO}{code}"])
    with open("hero.txt","w+") as txt:
        txt.writelines([("	".join(line) + "\n") for line in result])
    return result
def main():
    with open("./heroes.json") as heros:
        odota = json.load(heros)
        names = [x['localized_name'] for x in odota.values()]
        print(writeHeros(names))
        print(len(names))

main()
