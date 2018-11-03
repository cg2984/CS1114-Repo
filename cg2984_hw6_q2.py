#Clara Gilligan
#Homework 6
#CS 1114
#10/30/18

def print_top(offset, width) :
    # signature: int -> NoneType
    print ((offset+(width//2))* ' ' + '^')
def print_middle(offset, width) :
    # signature: int , int -> NoneType
    print (offset * ' ' + '/' + width * ' ' + '\\')
def print_bottom(offset , width):
    # signature: int , int -> NoneType
    print ((offset)* ' ' + width * '-')
def print_triangle():
    o = 10
    w = 7
    print_top(o, w)
    print_middle(o+2, w-6)
    print_middle(o+1, w-4)
    print_middle(o, w-2)
    print_bottom(o, w)
def main():
    print_triangle()
main()

