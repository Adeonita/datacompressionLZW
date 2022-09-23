# generate asc codes
for x in range(0, 128):
  number = str(x)

  if (len(number) == 1):
    print('0' + str(x))
  else:
    print(x)
