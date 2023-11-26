#factorial
def fact(n):
    if (n==0 or n==1):
        return 1
    else:
        return n*(n-1)
n_terms=int(input("Enter a number"))
factorial= fact(n_terms)
print(factorial)
 # Python program to display the Fibonacci sequence

def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

nterms = int(input("enter a number:"))

# check if the number of terms is valid
if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(recur_fibo(i))
