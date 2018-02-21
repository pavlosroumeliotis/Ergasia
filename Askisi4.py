LATINIKA = [
    (1000000,"(-M)"),(500000,"(-D)"),(100000,"(-C)"),(50000,"(-L)"),(10000,"(-X)"),(5000,"(-V)"),(4000,"(-IV)"),(1000,"M"),(900,"CM"),(500,"D"),(400,"CD"),(100,"C"), (90,"XC"),(50,"L"),(40,"XL"),(10,"X"),(9,"IX"),(5,"V"),(4,"IV"),(1,"I"),
] #antistixia 
number=input("DWSE ENA NOUMERO MEXRI KAI TO 1.000.000:")#eisagwgi ari8mou
if number <= 1000000: #proipothesi
    def metatropi(number): #dimiouria sinartisis tis metatropis
        result = ""
        for (arabika, latinika) in LATINIKA:
            (factor, number) = divmod(number, arabika)
            result += latinika * factor
        return result
    print metatropi(number)
else:
    print ("O ARI8MOS EINAI MEGALYTEROS TOY 1.000.000")
