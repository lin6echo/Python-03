'''
print("#")
print("#")
print("#")
'''
'''
for _ in range(3):
    print("#")
'''
def main():
    print_column(3)

def print_column(height):
    '''
    for _ in range(height):
    print("#")
    ''' 
    print("#\n" * height, end="")
main()