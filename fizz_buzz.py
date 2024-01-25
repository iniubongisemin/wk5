# fizzbuzz game
# 1. in a list of integers any number divisible by 3 print fizz
# 2. if it is divisible by 5 print buzz
# 3. if it's divisible by 5 and 3 print fizzbuzz

fizzbuzz_list = [ 3, 5, 9, 10, 12, 15, 18, 20, 21 ]
fizz_list = []
buzz_list = []
fizz_buzz = []

def fizzbuzz():
    for x in fizzbuzz_list:            
        if x % 3 == 0 and x % 5 == 0:
            print("fizzbuzz")
            fizz_buzz.append(x)
            print(fizz_list)
        elif x % 5 == 0: 
                print('buzz')
                buzz_list.append(x)
                print(buzz_list)
        elif x % 3 == 0:
                print('fizz')
                fizz_list.append(x)

fizzbuzz()

def welcome_func():
    print('welcome to 2024')

welcome_func()

class Newyear:

    def __init__(self, month, school) -> None:
        self.january = month
        self.univelcity = school

    def bootcamp():
        print('i am a backend engineer')

year = Newyear.bootcamp()
