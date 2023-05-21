year = int(input("请输入年份："))
tiaojian1=(((year%4) == 0) and ((year%100) != 0))
tiaojian2=(year%400==0)
print(tiaojian1 or tiaojian2)