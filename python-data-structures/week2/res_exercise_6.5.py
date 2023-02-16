str = "X-DSPAM-Confidence: 0.8475 "

findColon = str.find(":")
piece = str[findColon+1: ]
value = float(piece)

print(value)