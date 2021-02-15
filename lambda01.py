# 一个lambda函数，把参数加10，然后返回结果:
x = lambda a : a + 10
print(x(5))

# 一个lambda函数，将参数a与参数b相乘，然后返回结果:
x = lambda a, b : a * b
print(x(5, 6))


# 下面的示例使用这个函数定义创建了一个函数，该函数把传入的参数乘以2，返回结果:
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(1))

def myfunc(n):
  return lambda a : a * n

mytripler = myfunc(3)

print(mytripler(1))

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(1))
print(mytripler(1))

