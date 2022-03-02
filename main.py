# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def osszead(s1,s2):
    s3=s1+s2
    return s3

print_hi("Edina")
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    print(osszead("Edina","Mucsi"))

for i in range(10):
    print(i)
    print_hi("Edina")
k=1
while k<10:
    print(k)
    k=k+1

mylist = ["poi", "oij", "vik"]
for i in range(len(mylist)):
    print(i)
    print(mylist[i])

for i,name in enumerate(mylist):
    print(i, name)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

