import task2

def main():
    try:
        start=int(input("enter a number"))
        end=int(input("enter a number"))

        if start > end:
            print("invalid")
        random_numbers=task2.generate_random(10,start,end)
        print("generated random numbers",random_numbers)
    except ValueError:
        print("invalid")
if __name__=="__main__":
    main()
