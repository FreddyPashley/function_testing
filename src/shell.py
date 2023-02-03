from function_testing import Test


def func1(x, y):
    return f"hello{y} "*x


tester = Test()

print("Version: "+tester.version+"\n")

result = tester.test(func1, locals(), args=[2, 3], expected_type=str)
result.all()
