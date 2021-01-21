import sys,os
print(sys.getdefaultencoding())
import chardet
import pandas as pd
import csv

class ghyhdgshay():
    def __init__(self):
        # 获取当前文件位置
        yth = os.getcwd()
        path = yth + "\\data\\betting_new.csv"
        fsdfdssd = open(path, 'rb')
        dataasdas = fsdfdssd.read()
        print(chardet.detect(dataasdas))
        xg_jh = pd.read_csv(path)  # 读取csv文件

        dss = []
        for numh in range(len(xg_jh.loc[0:])):
            dss.append(numh)
        # dss.append(256)
        # dss.append(259)
        # dss.append(262)
        print(dss)
        data_new = xg_jh.drop(dss)

        new_txt = yth+"\\data\\betting_new_a.csv"
        data_new.to_csv(new_txt,encoding='UTF-8-SIG',index=0)
        print(chardet.detect(open(new_txt, 'rb',).read()))

        df_org = pd.read_csv(yth+"\\data\\betting_new.csv")
        print(df_org.columns)




if __name__ == '__main__':
    ghyhdgshay()