import datetime

accounts = [
  {"nazwa": "Masło Extra", "kod_kreskowy": "001", "cena_netto": 6.50},
  {"nazwa": "Chleb wiejski", "kod_kreskowy": "002", "cena_netto": 4.50},
  {"nazwa": "Makaron Babunia", "kod_kreskowy": "003", "cena_netto": 9.20},
  {"nazwa": "Dżem truskawkowy", "kod_kreskowy": "004","cena_netto":  8.10},
  {"nazwa": "Kiełbasa myśliwska", "kod_kreskowy": "005","cena_netto":  29.00},
  {"nazwa": "Szynka konserwowa", "kod_kreskowy": "006", "cena_netto": 22.00},
  {"nazwa": "Chipsy paprykowe", "kod_kreskowy": "007", "cena_netto": 6.00},
  {"nazwa": "Serek wiejski", "kod_kreskowy": "008", "cena_netto": 3.50},
  {"nazwa": "Sól kuchenna", "kod_kreskowy": "009", "cena_netto": 2.70},
  {"nazwa": "Cukier kryształ", "kod_kreskowy": "010", "cena_netto": 3.20},
]

def cena_brutto(cena_netto):
  return cena_netto * 1.23
  
koszyk=[]
kwota = 0

while True:
  print("Wybierz opcję")
  print("1 => LISTA WSZYSTKICH PRODUKTÓW")
  print("2 => ZAKUPY")
  print("3 => ZAKOŃCZ PROGRAM")
  
  wybor = input("Wybierz opcję 1,2 lub 3: ")
  if wybor == "1":
    print("KOD KRESKOWY | NAZWA")
    for produkt in accounts:
      print(f"{produkt['kod_kreskowy']} | {produkt['nazwa']}")
      
  elif wybor == "2":
    while True:  
      kod = input("KOD KRESKOWY LUB WYDRUK PARAGONU (P) :")
      for produkt in accounts:
      
          if produkt["kod_kreskowy"] == kod:
            koszyk.append(produkt)
            kwota += cena_brutto(produkt["cena_netto"])
            print(f"{produkt['nazwa']}")
            print (f"Cena łączna: {cena_brutto(produkt['cena_netto']):.2f} zł")
            break
        
      
          elif kod == "P":
            print("---------------------------------")
            print("Paragon")
            print(f"DATA ZAKUPU: {datetime.date.today()}")
            print("---------------------------------")
            print("---------------------------------")
            for produkt in koszyk:
              print(f"{produkt['nazwa']} | {cena_brutto(produkt['cena_netto']):.2f} zł")
            print(f"Do zapłaty: {kwota:.2f} zł")
            print(f"W tym VAT: {(kwota * 0.23):.2f} zł")
            print("---------------------------------")
            break
    
    else:
      print("Zły kod")
      break
        
    
    
    
    
    
  elif wybor == "3":
      break

  else:
      print("Nieprawidłowy wybór")
      break
