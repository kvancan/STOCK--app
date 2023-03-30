##import os

##with os.scandir('.') as entries:
    ##for entry in entries:
        #print(entry.name)#
import os 
from var_dump import var_dump
     
        
def addproductquantity():
    print('type product name')
    a=input()
    print('type product quantity')
    b=input()
    with open(a+' quantity.txt','w',encoding = 'utf-8') as f:
      f.write(b)
      print('quantity added')
     
    return a
def addproductprice(a):
    
    print('type product price')
    b=input()
    with open(a+' price.txt','w',encoding = 'utf-8') as f:
      f.write(b)
      print('price added')
      

def combine():
    b=addproductquantity()
    addproductprice(b) 
    program()     
    
def stockinformation():
    print('enter the name of the product you want to know the stock information')  
    d=input()
    f = open(d+" quantity.txt",'r',encoding = 'utf-8')
    variable=f.read()
    final=variable
    if final==-1:
      print('product does not exist') 
      program()       
    else:
      print(final) 
      program()       

def priceinformation():
    print('enter the name of the product you want to know the price information')  
    d=input()
    f = open(d+" price.txt",'r',encoding = 'utf-8')
    variable=f.read()
    final=variable
    if final==-1:
      print('product does not exist')
      program()      
    else:
      print(final)
      program()      

def stocks():
    

    with os.scandir('.') as entries:
        for entry in entries:
            a=entry.name.find(" quantity.txt")
            a=str(a)
            if a!='-1':
              newname=entry.name.replace("quantity.txt",'')
              print(newname+"="+str(read(entry.name)))
    program()
        

def prices():
    

    with os.scandir('.') as entries:
        for entry in entries:
            a=entry.name.find(" price.txt")
            a=str(a)
            if a!='-1':
              newname=entry.name.replace("price.txt",'')
              print(newname+"="+str(read(entry.name)))   
    program()              

def totalassets():
    products=[]
    total=0
    

    with os.scandir('.') as entries:
        for entry in entries:
            a=entry.name.find(" quantity.txt")
            a=str(a)
            if a!='-1':
              products.append(entry.name)    
    
    for product in products:
        product1=product.replace("quantity.txt","price.txt")
        total=total+(read(product)*read(product1))  
    print(total) 
    program()
    
def read(filename):
    f = open(filename,'r',encoding = 'utf-8')
    variable=f.read()
    final=variable
    variable=int(variable)
    return variable
    
    
def program():
    
    
   print('What action would you like to take? \n 1-add new product  \n 2-stock information \n 3-price information \n 4-quantity information of all products \n 5-price information of all products \n 6-total values of assets')

   x = input()
   if x=='1':
      combine()
  
   if x=='2':
      stockinformation()
  
  
   if x=='3':
      priceinformation()


   if x=='4':
      stocks()
   

   if x=='5':
      prices()  
       
       
   if x=='6':
      totalassets()   

   
         
        
program()