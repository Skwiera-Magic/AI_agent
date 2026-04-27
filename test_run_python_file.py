from functions.run_python_file import run_python_file

def main():
    print("Result for calculator:")
    print(run_python_file("calculator", "main.py"))
    print("\n")
    print("Result for calculator's 3 + 5:")
    print(run_python_file("calculator", "main.py", ["3 + 5"]))
    print("\n")
    print("Result for calculator's test:")
    print(run_python_file("calculator", "tests.py"))
    print("\n")
    print("Expecting error:")
    print(run_python_file("calculator", "../main.py"))
    print("\n")
    print("Expecting error:")
    print(run_python_file("calculator", "nonexistent.py"))
    print("\n")
    print("Expecting error:")
    print(run_python_file("calculator", "lorem.txt"))
    print("\n")


main()