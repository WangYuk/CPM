import NPV
from math import pow

def one_time_pay_final():
    print("请输入现在时间点的金额：")
    p = float(input())
    print("请输入年利率:")
    i = float(input())
    print("请输入年限：")
    n = int(input())
    f = p * pow((1 + i),n)
    print("F = P(1 + i)^n = %s"%f)

def one_pay_present():
    print("请输入期末值：")
    f = float(input())
    print("请输入年利率:")
    i = float(input())
    print("请输入年限：")
    n = int(input())
    p = f / pow((1 + i),n)
    print("P = F/(1 + i)^n = %s"%p)

def equal_pay_final():
    print("请输入每期末存入的的金额：")
    a = float(input())
    print("请输入年利率:")
    i = float(input())
    print("请输入年限：")
    n = int(input())
    f = a * (pow((1 + i),n) - 1) / i
    print("F = A((1 + i)^n - 1) / i = %s"%f)

def equal_oay_per():
    print("请输入期末的金额：")
    f = float(input())
    print("请输入年利率:")
    i = float(input())
    print("请输入年限：")
    n = int(input())
    a = f * i / (pow((1 + i),n) - 1)
    print("A = F * i / ((1 + i)^n - 1) = %s"%a)

def equal_pay_repay():
    print("请输入现在时间点的金额：")
    p = float(input())
    print("请输入年利率:")
    i = float(input())
    print("请输入年限：")
    n = int(input())
    a = p * i * pow((1 + i),n) / (pow((1 + i),n) - 1)
    print("A = P * i * (1 + i)^n / ((1 + i)^n - 1) = %s"%a)

def equal_pay_present():
    print("请输入每期末取出的的金额：")
    a = float(input())
    print("请输入年利率:")
    i = float(input())
    print("请输入年限：")
    n = int(input())
    p = a * (pow((1 + i),n) - 1) / (i * pow((1 + i),n))
    print("A = P * ((1 + i)^n - 1) / (i * (1 + i)^n )= %s"%p)


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
    print("9. 结束")
    print("请输入你想计算的公式号码：")
    end = False
    while not end:
        method = int(input())
        if method == 1:
            one_time_pay_final()
        elif method == 2:
            one_pay_present()
        elif method == 3:
            equal_pay_final()
        elif method == 4:
            equal_oay_per()
        elif method == 5:
            equal_pay_repay()
        elif method == 6:
            equal_pay_present()
        elif method == 7:
            npv = NPV.NetPresentValue(1)
            npv.calculate()
        elif method == 8:
            npv = NPV.NetPresentValue(0)
            print("要自己输入开始算插值的上下界吗？(y/n)")
            if input() == "y":
                npv.cal_irr(True)
            else:
                npv.cal_irr(False)
        elif method == 9:
            end = True
            break
        else:
            print("不支持的指令")
        print("请输入下一个公式代码：")
