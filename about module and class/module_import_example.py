import sys #importing "sys" module
sys.path.append('..') #make path is importing module from the same dir
import module_example #importing module called "module_example"

alpha = module_example.bebek() #call class named "bebek" from "module_example" module

beta = alpha.b() #call the "b" function inside the "bebek" class

charlie = beta.stri #get the stri variable from the function "b" in the "module_example" module

print(charlie) #it print 'a', because the "stri" value is "a"
