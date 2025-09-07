with open("theentirebible.txt","r", encoding="utf-8") as f:
    data = f.read()
newdata = []
for letter in data:
    if letter in ["0","1","2","3","4","5","6","7","8","9","'","\"",":",";",".",",","?","!","-"]:
        newdata.append(" ")
    else:
        newdata.append(letter)

newdata = "".join(newdata)

with open("theentirebible_fixed.txt", "w", encoding="utf-8") as biblefile:
    biblefile.write(newdata)

print("yuh")