import NPV
from math import pow


def one_time_pay_final():
    p = float(input("请输入现在时间点的金额："))
    i = float(input("请输入年利率:"))
    n = int(input("请输入年限："))
    f = p * pow((1 + i), n)
    print("F = P(1 + i)^n = %s" % f)


def one_pay_present():
    f = float(input("请输入期末值："))
    i = float(input("请输入年利率:"))
    n = int(input("请输入年限："))
    p = f / pow((1 + i), n)
    print("P = F/(1 + i)^n = %s" % p)


def equal_pay_final():
    a = float(input("请输入每期末存入的的金额："))
    i = float(input("请输入年利率:"))
    n = int(input("请输入年限："))
    f = a * (pow((1 + i), n) - 1) / i
    print("F = A((1 + i)^n - 1) / i = %s" % f)


def equal_oay_per():
    f = float(input("请输入期末的金额："))
    i = float(input("请输入年利率:"))
    n = int(input("请输入年限："))
    a = f * i / (pow((1 + i), n) - 1)
    print("A = F * i / ((1 + i)^n - 1) = %s" % a)


def equal_pay_repay():
    p = float(input("请输入现在时间点的金额："))
    i = float(input("请输入年利率:"))
    n = int(input("请输入年限："))
    a = p * i * pow((1 + i), n) / (pow((1 + i), n) - 1)
    print("A = P * i * (1 + i)^n / ((1 + i)^n - 1) = %s" % a)


def equal_pay_present():
    a = float(input("请输入每期末取出的的金额："))
    i = float(input("请输入年利率:"))
    n = int(input("请输入年限："))
    p = a * (pow((1 + i), n) - 1) / (i * pow((1 + i), n))
    print("A = P * ((1 + i)^n - 1) / (i * (1 + i)^n )= %s" % p)


def npvfunc():
    npv = NPV.NetPresentValue(1)
    npv.calculate()


def irr():
    npv = NPV.NetPresentValue(0)
    if input("要自己输入开始算插值的上下界吗？(y/n)") == "y":
        npv.cal_irr(True)
    else:
        npv.cal_irr(False)


def static_repay_time():
    n = int(input("请输入年限："))
    money = input("请在一行内输入各年净现金流，以空格分隔：").split()
    total = 0
    print("|%9s|%10s|%10s|" % ("年末", "Ft", "Sum Ft"))
    first_positive = True
    repay_time = -1
    for i in range(n + 1):
        if total + float(money[i]) > 0 and first_positive:
            repay_time = i - 1 + abs(total) / float(money[i])
            first_positive = False
        total += float(money[i])
        print("|%10d|%10.2f|%10.2f|" % (i, float(money[i]), total))
    if repay_time > 0:
        print("静态回收期： %s " % repay_time)
    else:
        print("这个项目不回本")


if __name__ == '__main__':
    print("支持功能：")
    print("1. 一次支付终值公式（已知初值利率年限求终值）")
    print("2. 一次支付现值公式（已知种植利率年限求初值）")
    print("3. 等额支付系列终值公式（已知每期末存入，利率年限求终值）")
    print("4. 等额支付系列债偿基金公式（期末想得到F，每期末应该存入多少）")
    print("5. 等额支付系列资金回收公式（已知期初，连续取n年，每年取多少）")
    print("6. 等额支付系列现值公式（已知每期末取出A，求期初存入多少）")
    print("7. 净现值")
    print("8. 内部收益率（插值法）")
    print("9. 静态回收期")
    print("10. 结束")
    print("请输入你想计算的公式号码：")
    methods = [0, one_time_pay_final, one_pay_present, equal_pay_final, equal_oay_per, equal_pay_repay,
               equal_pay_present, npvfunc, irr, static_repay_time]
    while True:
        method = int(input())
        if 1 <= method <= 9:
            methods[method]()
        elif method == 10:
            end = True
            break
        else:
            print("不支持的指令")
        print("请输入下一个公式代码：")
