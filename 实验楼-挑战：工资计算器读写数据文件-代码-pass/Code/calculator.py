#!/usr/bin/env python3

import sys
import csv
#读取配置文件类 返回文件路径
class Args(object):

    def __init__(self):
        self.args = sys.argv[1:]

    def get_config(self, param):
        index = self.args.index(param)
        self.configfile = self.args[index+1]
        try:
           f =  open(self.configfile)
           f.close() 
        except:
            print("Paramer Error")
        return self.configfile

#读取配置信息类 返回配置信息
class Config(object):

   # def __init__(self):
    #    self.config = self._read_config()

    def _read_config(self,configfile):
        config = {}
        
        configdata = []
        with open(configfile) as file:
            for x in file:
                try:
                    configdata = x.split("=")
                    configdata[0] = configdata[0].strip()          
                    configdata[1] = configdata[1].strip()
                    configdata[1] = float(configdata[1])
                except:
                    print("Formatting Error")
                config[configdata[0]] = configdata[1]

        return config

#读取员工信息类 返回员工信息
class UserData(object):

    #def __init__(self):
     #   self.userdata = self._read_users_data()

    def _read_users_data(self,configfile):
        userdata = []
        
        data = []
        with open(configfile) as file:
            for x in file:
                 try:
                    data = x.split(",")
                    data[0] = data[0].strip()
                    data[1] = data[1].strip()
                    data[0] = int(data[0])
                    data[1] = int(data[1])
                    
                   
                    userdata.append((data[0],data[1]))
                 except:
                    print("Formatting Error")

        return userdata

#计算税后工资、社保、个税类 返回员工工资条
class IncomeTaxCalculator(object):

    def calc_for_all_userdata(self, *userdata, **config):
        return_data = []
       # print(config)
        for key, value in config.items():
            if key == 'JiShuL':
                jishul = value
            elif key == 'JiShuH':
                jishuh = value
            elif key == 'YangLao':
                yanglao = value
            elif key == 'YiLiao':
                yiliao = value
            elif key == 'ShiYe':
                shiye = value
            elif key == 'GongShang':
                gongshang = value
            elif key == 'ShengYu':
                shengyu = value
            elif key == 'GongJiJin':
                gongjijin = value
            else:
                print('Config data error')

        #for data  in userdata:
            
        for data  in userdata:
            userID = data[0]
            salary = data[1]
            
            if salary <  jishul:
                security =  jishul * yanglao + jishul *yiliao + jishul * shiye + jishul * gongshang + jishul * shengyu + jishul * gongjijin
            elif salary > jishuh:
                security = jishuh * yanglao + jishuh * yiliao + jishuh * shiye + jishuh * gongshang + jishuh * shengyu + jishuh * gongjijin
            else:
                security = salary * yanglao + salary * yiliao + salary * shiye + salary * gongshang + salary * shengyu + salary * gongjijin
            
            taxable_income = salary - security - 3500
            if taxable_income <= 0:
                tax_payable = 0
            elif taxable_income <= 1500:
                tax_payable = taxable_income  * 0.03 - 0
            elif taxable_income <= 4500:
                tax_payable = taxable_income * 0.1 - 105
            elif taxable_income <= 9000:
                tax_payable = taxable_income * 0.2 - 555
            elif taxable_income <= 35000:
                tax_payable = taxable_income * 0.25 - 1005
            elif taxable_income <= 55000:
                tax_payable = taxable_income * 0.3 - 2755
            elif taxable_income <= 80000:
                tax_payable = taxable_income * 0.35 - 5505
            else:
                tax_payable = taxable_income * 0.45 - 13505
                                               
            after_tax_salary = salary - security - tax_payable
            
            row_data =[int(userID) ,int(salary),format(security,'.2f'),format(tax_payable, '.2f'),format(after_tax_salary,'.2f')]
            
           # row_data = ''.join(row_data)
            return_data.append(row_data)
        return return_data
		
	"""
    def export(self, default='csv'):
        result = self.calc_for_all_userdata()
        with open(default,'r') as f:
            writer = csv.writer(f)
            writer.writerows(result)
	"""


if __name__ == '__main__':
    args = Args()
    config_file = args.get_config('-c')
    users_file = args.get_config('-d')
    export_file = args.get_config('-o')

    config = Config()
    config_data = config._read_config(config_file)
   # print(config_data) 
    user = UserData()
    user_data = user._read_users_data(users_file)

    calculator = IncomeTaxCalculator()
    result = calculator.calc_for_all_userdata(*user_data, **config_data)
    with open(export_file, 'w') as f:
        writer = csv.writer(f)
        writer.writerows(result)
