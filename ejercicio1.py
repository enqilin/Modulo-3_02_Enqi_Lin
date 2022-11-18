
while True:
  a=input("Introduce un número: ")
  b=input("Introduce un número: ")
  try:
    a=int(a)
    b=int(b)
    x=a/b
    print(x)
    
    break
  except ZeroDivisionError:
    print("No se puede dividir por el zero. ")
    
    



if __name__=="__main__":
     main()
      