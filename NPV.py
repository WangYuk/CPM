import math

class NetPresentValue:
    net_cash_flow = []
    income_rate = 0
    year = 0
    net_present_value = 0

    def __init__(self,status):
        self.input_paras(status)

    def input_paras(self,status):
        if (status == 1):
            print("请输入收益率：")
            self.income_rate = float(input())
        print("请输入寿命期：")
        self.year = int(input())
        print("请在一行内输入各年净现金流，以空格分隔：")
        self.net_cash_flow = input().split()

    def calculate(self):
        for i in range(self.year+1):
            self.net_present_value = self.net_present_value + float(self.net_cash_flow[i]) / math.pow((1+self.income_rate),i)
        print("净现值为：%s"%self.net_present_value)

    def cal_tmp_npv(self, rate):
        out = 0
        for i in range(self.year+1):
            out = out + float(self.net_cash_flow[i]) / math.pow((1+rate),i)
        return out

    def cal_irr(self,is_diy):
        i1 = 0
        i2 = 1
        if is_diy:
            print("请输入开始的下界：")
            i1 = float(input())
            print("请输入开始的上界：")
            i2 = float(input())
        while i2 - i1 >= 0.05:
            i3 = (i1 + i2) / 2
            npv1 = self.cal_tmp_npv(i1)
            npv2 = self.cal_tmp_npv(i2)
            npv3 = self.cal_tmp_npv(i3)
            if npv3 == 0:
                print("内部收益率： %s%%,i1 = %s%%, i2 = %s%%" % (i3 * 100, i1 * 100, i2 * 100))
                return i3
            if npv1 * npv3 < 0:
                i2 = i3
            else:
                i1 = i3
            print("NPV(%s%%) = %s, NPV(%s%%) = %s" % (i1 * 100, npv1, i2 * 100, npv2))
        ret = i1 + self.cal_tmp_npv(i1) * (i2 - i1) / (self.cal_tmp_npv(i1) - self.cal_tmp_npv(i2))
        print("内部收益率： %s%%,i1 = %s%%, i2 = %s%%"%(ret*100,i1*100,i2*100))
