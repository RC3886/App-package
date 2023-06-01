class Calculator:

    def addition(self, num1, num2):
        print(f"The result is {num1 + num2}")
        print()

    def subtraction(self, num1, num2):
        print(f"The result is {num1 - num2}")
        print()

    def multiplication(self, num1, num2):
        print(f"The result is {num1 * num2}")
        print()

    def division(self, num1, num2):
        try:
            print(f"The result is {num1 / num2}")
        except ZeroDivisionError:
            print("Cannot divide by zero.")
        print()

    def power(self, num1, num2):
        print(f"The result is {num1 ** num2}")
        print()

    def square_root(self, num1):
        try:
            print(f"The result is {num1 ** 0.5}")
        except ValueError:
            print("Cannot take square root of negative number")
        print()

    def calc_enabled(self):
        calculator_mode = True
        while calculator_mode:
            print("Select an operator from the list:")
            op = int(input("1 - addition\n2 - subtraction\n3 - multiplication\n4 - division\n5 - power\n6 - sqrt\n0 - "
                       "back to the main menu. "))
            if op == 0:
                calculator_mode = False
            elif op == 6:                   # separated code, so the program doesn't ask for a second num
                num1 = int(input("Enter a number: "))
                self.square_root(num1)
            else:
                num1 = int(input("Enter the first number: "))
                num2 = int(input("Enter the second number: "))
                if op == 1:
                    self.addition(num1, num2)
                elif op == 2:
                    self.subtraction(num1, num2)
                elif op == 3:
                    self.multiplication(num1, num2)
                elif op == 4:
                    self.division(num1, num2)
                elif op == 5:
                    self.power(num1, num2)
                else:
                    print("Wrong operator.")




