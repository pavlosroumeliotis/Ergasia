keimeno=raw_input("Dwste keimeno:") #eisagwgi keimenou
neokeimeno ="" #neo keimeno
for i in range(len(keimeno)): #gia ka8e xaraktira
    if keimeno[i]!=" ":
        asc = ord(keimeno[i]) #euresi ascii gia ton xaraktira
        if asc <=90: #an einai kefalaio / pezo
            if asc + 13<=90:
                asc+=13
            else:
                asc = (asc+13)-90+65-1
        else:
            if asc + 13<=122:
                asc+=13
            else:
                asc = (asc+13)-122+97-1
        neokeimeno+=chr(asc) #prosthiki sto neo keimeno
    else:
        neokeimeno+=" "
print neokeimeno
