from replit import clear
from art import logo 

def addition(n1, n2):
    return n1 + n2
def substraction(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def devide(n1, n2):
    return n1 / n2
calc = {
"+" : addition,
"-" : substraction,
"*" : multiply,
"/" : devide 
}
def Calculator():
    clear()
    print(logo)
    will_continue = True
    num1 = int(input("Write the first number : "))
    for symbols in calc:
            print(symbols)
    while will_continue:
        op = input("Write the operation : ")    
        num2 = int(input("Write the second number : "))
        function = calc[op]
        result = function(num1, num2)
        print(f" {num1} {op} {num2} : {result}")
        should_continue = input("Do yo want to continue? then type in 'y' or 'n'  to start a new calculation .!! : ")
        if should_continue == "n":
            will_continue = False
            Calculator()
        else:
            num1 = result    

Calculator()
