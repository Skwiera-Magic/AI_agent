from functions.write_file import write_file

def main():
    print("Result for overwriting lorem.txt with 'wait, this isn't lorem ipsum':")
    print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
    print("\n")
    print("Result for writing to pkg/morelorem.txt:")
    print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
    print("\n")
    print("Result for writing to /tmp/temp.txt:")
    print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))
    print("\n")

main()