import div
import sub
import mul
import add

def main():
    print("Welcome to the Python Calculator!")
    while True:
        print("\nChoose an operation:")
        print("1. Division")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Addition")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '5':
            print("Thank you for using the calculator. Goodbye!")
            break
        
        if choice not in ['1', '2', '3', '4']:
            print("Invalid choice. Please try again.")
            continue
        
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        if choice == '1':
            result = div.perform_division(num1, num2)
        elif choice == '2':
            result = sub.perform_subtraction(num1, num2)
        elif choice == '3':
            result = mul.perform_multiplication(num1, num2)
        else:
            result = add.perform_addition(num1, num2)
        
        print(f"Result: {result}")

if __name__ == "__main__":
    main()
