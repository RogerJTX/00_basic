def funA(fn):
    """参数为一个函数对象"""
    print('A')
    fn() #执行传入的fn函数
    return 'tizer'

'''
下面的代码相当于funA(funB)
funB将会被替换为该语句的返回值
由于funA返回tizer，因此funB就是tizer
'''
@funA
def funB():
    print('B')
print(funB)


# 解释：既然funB作为参数传给了funA，那就是得先执行funA中的代码，所以执行了print(‘A’)，打印了A，然后执行第4行fn(),因为传入的funB，funB中的代码为print('B'),所以打印了B，然后funA 返回了一个字符串tizer，所以funB 等同于 tizer，第15行print(funB) 等同于 print('tizer'),所以打印了tizer。