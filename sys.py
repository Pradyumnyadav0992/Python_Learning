import sys
print(len(sys.argv))
sys.stderr.write("This is an error")

sys.stdout.write("Hi\n")
print("Hi\n")

inp=input()
if inp.lower() == "hello":
    sys.exit()
 
print(sys.getsizeof("12345"))
print(sys.getdefaultencoding())