m=False
w= False
a=0
b=1
fibonacci_row=[a,b]
while m == False:
     b = a + b
     fibonacci_row.append(b)
     a=b-a
     if len(fibonacci_row)==100:
          m = True
     else:
          m = False

print('Enter a number up to 3.000.000 to find out if it belongs to the Fibonacci sequence')
while w==False:
     randomnumber = int(input())
     if randomnumber in fibonacci_row:
          print('this number is in the sequence')
          w=True
     elif randomnumber>3000000:
          print('Please enter a smaller number')
          w=False
     elif randomnumber<0:
          print('please enter a positive number')
          w=False
     else:
          print('this number is not a part of the sequence')
          w=True
     



