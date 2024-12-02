# variable scope = where a variable is visible and accessible
# scope resolution = (LEGB) Local -> Enclosed -> Global -> Built-in

# Local variable


def func1():
    a = 1
    print(a)

def func2():
    b = 2
    print(b)

func1()
func2()

# Global variable

def func1():
    print(x)

def func2():
    print(x)

x = 3

func1()
func2()