cour = int(input('Enter Course Code: '))
match cour:
    case 101:
        print('Course Selected: Python Programing')
    case 102:
        print('Course Selected: Java Programing')
    case 103:
        print('Course Selected: Web Programming')
    case 104:
        print('Course Selected: C/C++ Programming')
    case 105:
        print('Course Selected: Data Analytics')
    case _:
        print('Invalid Course Code')