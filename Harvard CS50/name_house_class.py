
class Student:
    def __init__(self, name, house):
        if not name:
            return None
        self.name = name
        self.house = house
 
def main():
    student = get_student()
    print(f"{student.name} from {student.house}")

def get_student():
    '''
    student = Student()
    student.name = input("Name: ")
    student.house = input("House: ")
    '''
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)
    

if __name__ == "__main__":
    main()