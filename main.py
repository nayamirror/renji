def main():
    num1 = float(input("Введіть перше число: "))
    num2 = float(input("Введіть друге число: "))

    while True:
        print("Виберіть дію:")
        print("1. +")
        print("2. -")
        print("3. *")
        print("4. /")
        print("5. Заміна чисел")
        print("0. Вихід")

        choice = input(">> ")

        if choice == '1':
            print(f"{num1} + {num2} = {num1 + num2}")
        elif choice == '2':
            print(f"{num1} - {num2} = {num1 - num2}")
        elif choice == '3':
            print(f"{num1} * {num2} = {num1 * num2}")
        elif choice == '4':
            if num2 == 0:
                print("На нуль ділити не можна!")
                num2 = float(input("Введіть інше число: "))
                if num2 == 0:
                    print("На нуль ділити не можна!")
                    continue
                else:
                    print(f"{num1} / {num2} = {num1 / num2}")
            else:
                print(f"{num1} / {num2} = {num1 / num2}")
        elif choice == '5':
            num1 = float(input("Введіть перше число: "))
            num2 = float(input("Введіть друге число: "))
        elif choice == '0':
            break
        else:
            print("Невідома опція, спробуйте ще раз.")

        input("Натисніть Enter, щоб продовжити...")

if __name__ == "__main__":
    main()