def kecilinDong(inputan):
  daftar_huruf = { # dictionary -> kamus 
    "A": "a",
    "B": "b",
    "C": "c",
    "D": "d",
    "E": "e"
  }

  hasil = ""
  for huruf in inputan:
    hasil += daftar_huruf[huruf]
  
  return hasil

def gedeinDong(inputan):
  daftar_huruf = {
    "a": "A",
    "b": "B",
    "c": "C",
    "d": "D",
    "e": "E"
  }

  hasil = ""
  for huruf in inputan:
    hasil += daftar_huruf[huruf]
  
  return hasil  

inputan = "ABCDE"
print(kecilinDong(inputan))
print(gedeinDong("abcde"))
