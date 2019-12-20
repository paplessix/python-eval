from ruler import Ruler
import sys


def iter_rule(datfile):
    with open(datfile,'r') as f:
        string1 = ""
        string2 = ""
        for line in f :
            if line == '' or line ==' ' or line == '\n':
                pass
            elif string1 == '':
                string1 = line
            elif string2 == '':
                string2 = line

                ruler = Ruler(string1,string2)
                string1, string2 = '', ''
                ruler.compute()
                top,bottom = ruler.report()

                yield ruler.distance, top, bottom

def affichage(datfile):
    for number, tuples in enumerate(iter_rule(datfile),1):
        dist,top,bottom = tuples
        print(f"====== example # {number} - distance = {dist}")
        print(top)
        print(bottom)

def main():
    if len(sys.argv) == 2:
        datafile = sys.argv[1]
        affichage(datafile)
    return 0

if __name__ == '__main__':
    sys.exit(main())


    