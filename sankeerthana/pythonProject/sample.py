try:

        result=10/0

except Exception as e:

        print(f"zero division error:{e} ")


except ValueError :
       print("valueerror")
else:
    print("nothing")

finally:
    print("completed")