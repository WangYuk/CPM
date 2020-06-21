import math
from math import ceil, floor

class NetPresentValue:
    net_cash_flow = []
    income_rate = 0
    year = 0

    def __init__(self,status):
        self.input_paras(status)
        self.net_present_value = 0

    def input_paras(self,status):
        if status == 1:
            self.income_rate = float(input("请输入收益率："))
        self.year = int(input("请输入寿命期："))
        self.net_cash_flow = input("请在一行内输入各年净现金流，以空格分隔：").split()

    def calculate(self):
        net_cash_flow = []
        net_cash_flow_present = []
        total_cash_flow_present = []
        first_positive = 0
        dynamite_repay_time = 0
        set = False
        for i in range(self.year+1):
            net_cash_flow.append(math.pow((1+self.income_rate),-i))
            net_cash_flow_present.append(float(self.net_cash_flow[i]) / math.pow((1+self.income_rate),i))
            self.net_present_value = self.net_present_value + float(self.net_cash_flow[i]) / math.pow((1+self.income_rate),i)
            total_cash_flow_present.append(self.net_present_value)
            if not set and total_cash_flow_present[i] > 0:
                first_positive = i
                dynamite_repay_time = first_positive - 1 + -total_cash_flow_present[i-1] / net_cash_flow_present[i]
                set = True
        print("|       年序     |", end="")
        for i in range(self.year + 1):
            print("%10d|"%i,end="")
        print("")
        print("|    折现系数    |", end="")
        for i in range(self.year + 1):
            print("%10.3f|"%net_cash_flow[i],end="")
        print("")

        print("|  净现金流量现值 |",end="")
        for i in range(self.year + 1):
            print("%10.3f|" % net_cash_flow_present[i], end="")
        print("")
        print("|累积净现金流量现值|", end="")
        for i in range(self.year + 1):
            print("%10.3f|" % total_cash_flow_present[i], end="")
        print("")
        print("净现值为：%s"%self.net_present_value)
        print("动态投资回收期： %s"%dynamite_repay_time)

    def cal_tmp_npv(self, rate):
        out = 0
        for i in range(self.year+1):
            out = out + float(self.net_cash_flow[i]) / math.pow((1+rate),i)
        return out

    def cal_irr(self,is_diy):
        i1 = 0
        i2 = 1
        if is_diy:
            i1 = float(input("请输入开始的下界："))
            i2 = float(input("请输入开始的上界："))
        while i2 - i1 >= 0.02:
            i3 = (i1 + i2) / 2
            npv1 = self.cal_tmp_npv(i1)
            npv2 = self.cal_tmp_npv(i2)
            npv3 = self.cal_tmp_npv(i3)
            if npv3 == 0:
                print("内部收益率： %s%% (精确值)" % i3 * 100)
                return
            if npv1 * npv3 < 0:
                i2 = i3
            else:
                i1 = i3
            print("NPV(%s%%) = %s, NPV(%s%%) = %s" % (i1 * 100, npv1, i2 * 100, npv2))
        i1, i2 = floor(i1 * 100) / 100, ceil(i2 * 100) / 100
        print("NPV(%s%%) = %s, NPV(%s%%) = %s" % (i1 * 100, npv1, i2 * 100, npv2))
        ret = i1 + self.cal_tmp_npv(i1) * (i2 - i1) / (self.cal_tmp_npv(i1) - self.cal_tmp_npv(i2))
        print("内部收益率： %s%%,i1 = %s%%, i2 = %s%%"%(ret*100,i1*100,i2*100))
