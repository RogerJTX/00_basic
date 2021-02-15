import difflib
import sys
a = open('01/7-1.txt', 'r', encoding='utf-8').readlines()
b = open('01/7-3.txt', 'r', encoding='utf-8').readlines()
diff = difflib.ndiff(a, b)
sys.stdout.writelines(diff)
