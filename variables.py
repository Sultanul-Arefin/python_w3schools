x = 5;
y = "fahim";
print(x)
print(y)

# assign value to multiple variables
x, y, z = "sultanul", "arefin", "fahim"
print(x)
print(y)
print(z)

#same value to multiple variable
m = n = o = "fahim"
print(m)
print(n)
print(o)

#Output Variable
h= "awesome"
print("Python is "+h)

i = "Python is"
j = " Awesome"
print(i + j)

#if try to combine a string and a number, python will give an error

#global variable
a = "cool" #global

def myfunc():
	a="fantastic" #local
	print("Python is "+a)

myfunc()
print("Python is "+a)