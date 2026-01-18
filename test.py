def main():
    name = input("Enter your name: ")
    print(name)
    print(hello(2))

def hello(n):
    print("Hello, world!")
    return n*n 
    
main()