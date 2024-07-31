def test(text):
    return text.upper()
print(test("hi infinitude"))
def test2(func):
    string=func("this is a string")
    print(string)
test2(test)
