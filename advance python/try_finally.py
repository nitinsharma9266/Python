def main():
    try:
        a=int(input("enter the number :"))
        print(a)

    except ValueError as v:
        print(v)

    finally:
        print("I am inside the finally ")   #  it will be executed every times .

main()
    