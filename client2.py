import sys, Ice
import Demo
 
communicator = Ice.initialize(sys.argv)

base1 = communicator.stringToProxy("SimplePrinter1:tcp -h 98.94.241.216 -p 5678")
base2 = communicator.stringToProxy("SimplePrinter2:tcp -h 98.94.241.216 -p 5678")
printer1 = Demo.PrinterPrx.checkedCast(base1)
printer2 = Demo.PrinterPrx.checkedCast(base2)
if (not printer1) or (not printer2):
    raise RuntimeError("Invalid proxy")

# printString — método original
rep = printer1.printString("Hello World from printer1!")
print(rep)
rep = printer2.printString("Hello World from printer2!")
print(rep)
 
# toUpperCase — printer1
rep = printer1.toUpperCase("hello from printer1")
print(rep)
 
# toUpperCase — printer2
rep = printer2.toUpperCase("hello from printer2")
print(rep)
 
# countWords — printer1
n = printer1.countWords("sistemas distribuidos com ice middleware")
print(f"printer1 contou {n} palavras")
 
# countWords — printer2
n = printer2.countWords("zeroc ice rpc framework")
print(f"printer2 contou {n} palavras")
 
communicator.destroy()