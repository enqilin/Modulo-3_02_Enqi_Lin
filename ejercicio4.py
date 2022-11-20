def error(*args):
  resultado=0
  for numero in *args: 
  try:
    resultado=+numero
  except TypeError:
    print("NO se puede encadenar 'string'con 'int'")
  




if __name__=="__main__":
  main()