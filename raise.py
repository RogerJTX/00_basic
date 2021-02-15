'''
raise 的使用，抛出异常

当程序出现错误，python会自动引发异常，也可以通过raise显示地引发异常。
一旦执行了raise语句，raise后面的语句将不能执行。

raise 唯一的一个参数指定了要被抛出的异常。它必须是一个异常的实例或者是异常的类（也就是 Exception 的子类）。
如果你只想知道这是否抛出了一个异常，并不想去处理它，那么一个简单的 raise 语句就可以再次把它抛出。
'''
#
# x = 10
# if x > 5:
#     raise Exception('x 不能大于 5。x 的值为: {}'.format(x))

try:
    raise NameError('HiThere')
except NameError:
    print('An exception flew by!')
    raise

print(1)