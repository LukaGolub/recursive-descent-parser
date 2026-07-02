import sys

class ParseError(Exception):
    pass


def unos_niza():
    line = sys.stdin.readline()  
    line = line.strip()          
    if all(ch in 'abc' for ch in line):
        return line + '\n'       
    else:
        print("FAIL")
        return ''  
def A():
    global ulaz, i
    print("A", end="")
    if ulaz == 'b':
        
        if i + 1 < duljina:
            i += 1
            ulaz = niz[i]
        else: ulaz = "\n"
        
        C()
    elif ulaz == 'a':
        
        if i + 1 < duljina:
            i += 1
            ulaz = niz[i]
        else: ulaz = "\n"
    else: raise ParseError("Kraj niza")
        

def B():
    global ulaz, i
    print("B", end="")
    if ulaz == 'c':
        if i + 1 < duljina:
            i += 1
            ulaz = niz[i]
        else: ulaz = "\n"
        
        ulaz = niz[i]
        if ulaz == 'c':
            if i + 1 < duljina:
                i += 1
                ulaz = niz[i]
            else: ulaz = "\n"
            S()
            if ulaz == 'b':
                if i + 1 < duljina:
                    i += 1
                    ulaz = niz[i]
                else: ulaz = "\n"
                if ulaz == 'c':
                    if i + 1 < duljina:
                         i += 1
                         ulaz = niz[i]
                    else: ulaz = "\n"
    



def C():
    global ulaz, i
    print("C", end="")
    A()
    A()
    return


def S():
    global ulaz, i
    print("S", end="")
    if ulaz == 'a':
        if i + 1 < duljina:
            i += 1
            ulaz = niz[i]
        else: ulaz = "\n"
        A()
        B()
    elif ulaz == 'b':
        if i + 1 < duljina:
            i += 1
            ulaz = niz[i]
        else: ulaz = "\n"        
        B()
        A()

    else: raise ParseError("Kraj niza")

niz = unos_niza()
i = 0
duljina = len(niz)
global ulaz 
ulaz = niz[i]

try:
    S()
    if ulaz == '\n':
        print("\nDA")
    else:
        print("\nNE")
except ParseError:
    print("\nNE")
