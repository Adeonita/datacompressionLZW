filename = 'files/ed2test.txt'

with open(filename) as f:
  while True:
    c = f.read(1)
    if not c:
      print ("End of file")
      break
    print ("Read a character:", c)
