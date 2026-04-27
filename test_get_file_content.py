from functions.get_file_content import get_file_content

def main():
    lorem = get_file_content("calculator", "lorem.txt")
    main = get_file_content("calculator", "main.py")
    calculator = get_file_content("calculator", "pkg/calculator.py")
    cat = get_file_content("calculator", "/bin/cat")
    dne = get_file_content("calculator", "pkg/does_not_exist.py")
    print("Result for file lorem.txt:")
    print(f"Length of lorem: {len(lorem)}")
    if len(lorem) > 10000:
        print("Text is over 10k signs and was truncated")
    print("\n")
    print("Result for file main.py:")
    print(f"Contents of main.py: {main}")
    if len(main) > 10000:
        print("Text is over 10k signs and was truncated")
    print("\n")
    print("Result for file calculator.py:")
    print(f"Contents of calculator.py: {calculator}")
    if len(calculator) > 10000:
        print("Text is over 10k signs and was truncated")
    print("\n")
    print("Result for file cat.py:")
    print(f"Contents of cat.py: {cat}")
    if len(cat) > 10000:
        print("Text is over 10k signs and was truncated")
    print("\n")
    print("Result for file does_not_exist.py:")
    print(f"Contents of does_not_exist.py: {dne}")
    if len(dne) > 10000:
        print("Text is over 10k signs and was truncated")
    print("\n")

main()