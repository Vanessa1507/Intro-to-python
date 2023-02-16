str = "X-DSPAM-Confidence: 0.8475 "

cleanStr= str.strip()
findSpace = cleanStr.find(" ")

num = float(cleanStr[findSpace: ])
print(num)