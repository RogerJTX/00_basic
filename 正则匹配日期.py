import re

test_date = '他的生日是2016年12月12日 14:34,是个可爱的小宝贝.二宝的生日是2016-12-21 11:34,好可爱的.'
mat = re.search(r"(\d{4}-\d{1,2}-\d{1,2})",test_date)
print(mat.groups())
print(mat.group(0))

test_date = '2016年12月12日11'
# mat = re.search(r"(\d{4}-\d{1,2}-\d{1,2})",test_date)
# print(mat.groups())
# print(mat.group(0))


date_all = re.findall(r"(\d{4}-\d{1,2}-\d{1,2})",test_date)
print(date_all)



date_reg_exp = re.compile('\d{4}[-/年]\d{2}[-/月]\d{2}')
test_str= """
   平安夜圣诞节2016-12-24的日子与去年2015/12/24的是有不同哦2015年12月12日11.
   """
# 根据正则查找所有日期并返回
matches_list=date_reg_exp.findall(test_str)
# 列出并打印匹配的日期
for match in matches_list:
 print(match.replace('年', '').replace('月', ''))