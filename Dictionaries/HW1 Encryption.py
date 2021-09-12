#step one: read the file

infile = open("info_security.txt", "r")
security_file = infile.read()

#step two: encrypt the file
encryption = {'A': "1", 'a': '!', 's': 'l', 'S': 'L', 'd': 'K', 'D': 'k',
'f': 'J', 'F': 'j', 'G': 'H', 'g': 'h', 'E': '#', 'e': '3', 'i': '8', 
'I': '*', 'm': 'U', 'p': '?', 'l': 'S', 'o': '9', 'y': "6", ' ': '`', 'b': 'E',
'h': 'g', 'v': 'c', 'r': "<", 'c': 'V', 'n': 'b', 't': '5', 'u': '7', 'z': 'x',
".": '<', 'C': 'X', 'w': '2', 'k': 'd', 'x': 'z', 'R': '$', 'O': '(', ':': '|'}

#step three: write the file

outfile = open("EncryptedFile.txt", "w")
for x in security_file:
    scramble = encryption[x]
    outfile.write(scramble)

infile.close()
outfile.close()