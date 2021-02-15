import os, sys
import traceback
try:
    aa = 0
    # if aa == 1:
    sys.exit(0)
    print(1)
except:
    print('die')
    print(traceback.format_exc())
finally:
    print('cleanup')

try:
    sys.exit(100)
    print(1)
except SystemExit as SyntaxError:
    print('Syn:', SyntaxError)
finally:
    print('cleanup01')

try:
    a = 0
    print(a.a)

except SystemExit as SyntaxError:
    print('Syn1:', SyntaxError)
    print(1)
    sys.exit(1)
except Exception:
    print(traceback.format_exc())


try:
    print(1)
    sys.exit(100)
    print(2)
except SystemExit as SyntaxError02:
    print ('捕捉到SystemExit异常,SystemExit 并不派生自Exception 所以用Exception对它没有用')
    print(SyntaxError02)
print('并没有退出呀...')






try:
    os._exit(0)
except:
    print('die02')
print('os.exit')


