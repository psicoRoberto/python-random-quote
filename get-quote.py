import random
def primary():
   # print("Keep it logically awesome. Please")
  f= open("quotes.txt", "a")
  f.write("Now the file has more content!\n")
  f.write("This test is working\n")
  f.close()

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  last= len(quotes) - 1
  rnd  = random.randint(0, last)
  rnd0 = random.randint(0, last)
  rnd1 = random.randint(0, last)
  rnd2 = random.randint(0, last)

  print (quotes [rnd] end='')
  print (quotes [rnd0] end='') 

if __name__== "__main__":
  primary()
  
