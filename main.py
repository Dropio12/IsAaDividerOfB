import Divider as dd
def main():
    test_number=float(input("Which number will be the divider: "))
    if dd.Divider(test_number,main_number):
        print("The number is a divider")
    else:
        Retry= input("It isn't. Would you like to retry with another number? (Y/N)")
        if Retry == "Y" or Retry== "y":
            main()
        else:
            print('Better chance next time!')


if __name__ == '__main__':
    main_number=float(input("Which number do you want us to test a divider for: "))
    main()
