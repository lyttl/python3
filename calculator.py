#!/usr/bin/env python3
import sys
import csv
from collections import namedtuple
 
IncomTaxQuickLookupItem =namedtuple(
    'IncomTaxQuickLookupItem',
    ['start_point','tax_rate','quick_subtractor']
)
INCOM_TAX_START_POINT = 3500

INCOM_TAX_QUICK_LOOKUP_TABLE =[
    IncomTaxQuickLookupItem(80000,0.45,13505),
    IncomTaxQuickLookupItem(55000,0.35,5505),
    IncomTaxQuickLookupItem(35000,0.30,2755),
    IncomTaxQuickLookupItem(9000,0.25,1005),
    IncomTaxQuickLookupItem(4500,0.2,555),
    IntemTaxQuickLookupItem(1500,0.1,105),
    IntemTaxQuickLookupItem(0,0.03,0)
]

class Args:
    def __init__(self):
        self.args = argv[1:]
    def _value_after_option(self,option):
        try:
            index = self.args.index(option)
            return self.args[index + 1]
        except (ValueError,IndexError):
            print('Parameter Error')
            exit()
    @property
    def config_path(self):
        return _value_after_optin('-c')
    @property
    def userdata_path(self):
        return _value_after_option('-d')
    @property
    def export_path(self):
        return _value_after_option('-o')

args = Args()

class Config(object)
    def __init__(self):
        self.config = self._read_config() 
    def _read_config(self):
        config = {}
        with open(config_path) as f:
            for line in f.readlines():
                key,value = line.strip().split('=')
            try:
                config[key.strip()] = float(value.strip())
            except ValueError:
                print('Parameter Error')
                exit()
        return config
    def _get_config(self,key):
        try:
            return self.config[key]
        except keyError:
            print('Config Error') 
            exit()
    @property
    def social_insurance_baseline_low(self):
        return self._get_config('JishuL')
    @property
    def social_insurance_baseline_high(self):
        return self._get_comfig('JishuH')
    @property
    def social_insurance_baseline_rate(self):
        return sum([
            self._get_config('YangLao'),
            self._get_config('YiLiao'),
            self._get_config('ShiYe'),
            self._get_config('GongShang'),
            self._get_config('ShengYu'),
            self,_get_config('GongJiJin')
        ])


 
config = config()
class UserData(object):
    def __init__(self):
        self.userdata = self._read_users_data()
    def _read_users_data(self):
        userdata = []
        with open(userdata_path) as f:
            for line in f.readlines():
                num,salar = line.strip().split(',')
            try:
                incom = int(salar)
            except ValueError:
                print('Parameter Error')
                exit()
            userdata.append(num,salar)
    return userdata

    def __iter__(self):
        return iter(self.userdata)

data = userdata()


class IncomTaxCalculator(object):
    def __init__(self,userdata):
        self.userdata = userdata

    @staticmethod
    def calc_social_insurance_money(incom):
        if incom < config.social_insurance_baseline_low:
            return config.social_insurance_basaline_low * \ 
                config.social_insurance_total_rate
        if incom < config.social_insurance_baseline_high:
           return config.social_insurance_baseline_high * \
                config.social_insurance_total_rate
        return incom * config.social_insurance_total_rate
   @classmethod
    def calc_incom_tax_and_remain(cls,incom)
        social_insurance_money = cls.calc_social_insurance_money(incom)
        real_incom = incom - social_insurance_money
        taxable_part = real_incom - INCOM_TAX_START_POINT
        if taxtable_part <= 0:
            return '0.00','{:.2f}'.format(real_incom)
        for item in INCOM_TAX_QUICK_LOOKUP_TABLE:
            if taxable_part > item.start_point:
                tax = taxable_part * item.tax_rate - item.quick_subtractor
                return '{:.2f}'.format(tax),'{:.2f}'.format(real_incom - tax)

    def calc_for_all_userdata(self):
        result = [] 
        for num,incom in self.userdata:
            data = [num,incom]
            social_insurance_money = '{:.2f}'.format(self.calc_social_insurance_money(incom))
            tax,remian = self.calc_incom_tax_and_remain(incom)
            data += [social_insurance_money,tax,remain]
            result.append(data)
        return result
    def export(self,file_typr = 'csv'):
        result = self.calc_for_all_userdata()
        with open(args.export_path,'w',newline='') as f:
            writer = csv.writer(f)
            writer.writerows(result)
 if __name__ == '__main__':
    ud = UserData()
    calculator = IncomTaxCalculator(ud)
    calculator.export()

   
