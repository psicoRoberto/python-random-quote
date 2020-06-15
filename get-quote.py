#Known issue:
#f.write will keep writing the same line over and over again to the txt file.
#The print command prints the first line in a different way than the others (at least in VS Code).

import random
def primary():
   # print("Keep it logically awesome. Please")

   #this part adds quotes to the txt file
  f= open("quotes.txt", "a")
  f.write("Now the file has more content!\n")
  f.write("This test is working\n")
  f.close()

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

#A simple way to get multiple random quotes
  last= len(quotes) - 1
  rnd  = random.randint(0, last)
  rnd0 = random.randint(0, last)
  rnd1 = random.randint(0, last)
  rnd2 = random.randint(0, last)

#Use of (end='') to remove the newline at the end
  print (quotes [rnd], quotes [rnd0], quotes [rnd1], quotes [rnd2], end='')

if __name__== "__main__":
  primary()
  
