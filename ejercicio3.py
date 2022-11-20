paises = { "españa":"español", "eeuu":"inglés", "italia":"italiano" } 
def error(paises):
  try:
    paises["alemania"]
  except KeyError:
    print("No existe esta clave.")
    

if __name__=="__main__":
  main()