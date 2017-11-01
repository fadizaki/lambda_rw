# Reading input file and eliminate \n and blank lines:
file = open('Input.txt').readlines()
file = [x for x in file if x != "\n"]
file = [s.rstrip() for s in file]

# parsing:
name = file[0]
num = file[1:]
nameZ = name[:-1]
nameY = list(nameZ)
nameY[2] = "Y"
nameY="".join(nameY)
part1 = map(lambda line:"BLODI:DEV=UPDR-"+str(int(line)*32+1)+"&&-"+str(int(line)*32+31), num)
part2 = map(lambda line:"EXDAE:DEV=UPDR-"+str(int(line)*32+1)+"&&-"+str(int(line)*32+31), num)
part3 = map(lambda line:"EXDRE:DEV=UPDR-"+str(int(line)*32+1)+"&&-"+str(int(line)*32+31), num)
part4 = map(lambda line:"EXDUE:DEV=UPDR-"+str(int(line)*32)+"&&-"+str(int(line)*32+31), num)
part5 = map(lambda line:"NTBLI:SNT=RTDMA-"+str(int(line)), num)
part6 = map(lambda line:"NTCOE:SNT=RTDMA-"+str(int(line)), num)

# open output file:
f = open("script.txt", "w+")

# defining writing function:
def writing(s):
    for x in list(s):
        f.write(x+";\n")
    f.write("\n\n")

f.write('@CONNECT ("%s")' %file[0][0:2])
f.write("\n\nBLURE:R=%sO,PERM;\nBLURE:R=%sI,PERM;\nDUDSE:R=%sO,PERM;\nDUDSE:R=%sI,PERM;\n\n"%(nameZ,nameZ,nameZ,nameZ))
writing(part1)
writing(part2)
writing(part3)
writing(part4)
writing(part5)
writing(part6)
f.write("ADRDC:R=%sO,DRAG;\nADRDC:R=%sI,DRAG;\n!ADRDC:R=%sO,DRAG;\n!ADRDC:R=%sI,DRAG;\n"%(nameZ,nameZ,nameY,nameY))
f.write("EXROE:R=%sO&%sI;\n"%(nameZ,nameZ))
f.write("!EXROE:R=%sO&%sI;\n"%(nameY,nameY))
f.write("\n@DISCONNECT")

f.close()