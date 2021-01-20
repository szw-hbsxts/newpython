import re
import json
import csv
import os


class shag():

    def zzpp(self,text):
        a = r'.*?(var meta.+"resourceId":\d+}};).*'
        b = re.search(a,text)
        c = b.group(1)
        m = c.replace('var meta = ', '')
        m = m.replace(';', '')
        m = json.loads(m)
        return m
    def tiqu(self,zz,text):
        b = re.search(zz,text)
        c = b.group(1)
        c = json.loads(c)
        return c

    def tiancong(self,cp):
        pass
        a0 = '0'
        a1 = '1'
        a2 = 'visible'
        a3 = 'taxable'
        ak = ''
        if cp[1] == 'variable':
            gf_cp = [cp[0],cp[1],cp[2],cp[3],a1,a0,a2,cp[4],cp[5],ak,ak,a3,ak,a1,ak,a0,a0,ak,ak,ak,ak,a1,ak,ak,ak,cp[6],ak,ak,cp[7],ak,ak,ak,ak,ak,ak,ak,ak,a0]
            su = cp[8]
            for i in range(len(su)):
                gf_cp.append(su[i])
                uy = ''
                nm = cp[9][i]
                for j in range(len(nm)):
                    if j == len(nm) -1:
                        gm = nm[j].replace('（', ' (')
                        gm = gm.replace('）', ')')
                        uy += gm
                    else:
                        gm = nm[j].replace('（',' (')
                        gm = gm.replace('）', ')')
                        uy += gm + ', '
                uy.encode()
                gf_cp.append(uy)
                gf_cp.append(a1)
                gf_cp.append(a1)

            for n in range(12 - len(su)*4):
                gf_cp.append(ak)
            gf_cp.append(a1)
            f = self.svc(gf_cp)
            return gf_cp


        elif cp[1] == 'variation':
            pass
            jc = '.'
            xj = str(cp[4])
            yj = str(cp[5])
            if jc not in xj:
                # xj = '25.23'
                list_i = list(xj)
                list_i.insert(-2,'.')
                xj = ''.join(list_i)
            if yj == 'None':
                yj = xj
            else:
                if jc not in yj:
                    list_y = list(yj)
                    list_y.insert(-2, '.')
                    yj = ''.join(list_y)


            gf_cp = [cp[0],cp[1],cp[2],cp[3],a1,a0,a2,ak,ak,ak,ak,a3,ak,a1,ak,a0,a0,ak,ak,ak,ak,a0,ak,xj,yj,ak,ak,ak,cp[6],ak,ak,cp[7],ak,ak,ak,ak,ak,a0]
            su = cp[8]
            for i in range(len(su)):
                gf_cp.append(su[i])
                uy = ''
                nm = cp[9][i]
                gf_cp.append(nm)
                gf_cp.append(ak)
                gf_cp.append(a1)

            for n in range(12 - len(su)*4):
                gf_cp.append(ak)
            f = self.svc(gf_cp)
            return gf_cp

        elif cp[1] == 'simple':
            pass
            jc = '.'
            xj = str(cp[6])
            yj = str(cp[7])
            if jc not in xj:
                # xj = '25.23'
                list_i = list(xj)
                list_i.insert(-2, '.')
                xj = ''.join(list_i)
            if yj == 'None':
                yj = xj
            else:
                if jc not in yj:
                    list_y = list(yj)
                    list_y.insert(-2, '.')
                    yj = ''.join(list_y)

            gf_cp = [cp[0],cp[1],cp[2],cp[3],a1,a1,a2,cp[4],cp[5],ak,ak,a3,ak,a1,ak,a0,a0,ak,ak,ak,ak,a1,ak,xj,yj,cp[8],ak,ak,cp[9],ak,ak,ak,ak,ak,ak,ak,ak,a0]
            for n in range(12):
                gf_cp.append(ak)
            gf_cp.append(a1)
            f = self.svc(gf_cp)
            return gf_cp

    def svc(self,data):
        url_fd = os.getcwd()
        # 1. 创建文件对象
        f = open('./all/betting_new_a.csv','a',encoding='UTF-8-SIG',newline="")
        # 2. 基于文件对象构建 csv写入对象
        csv_writer = csv.writer(f)
        # 3. 构建列表头
        # csv_writer.writerow(["姓名", "年龄", "性别"])
        # 4. 写入csv文件内容
        csv_writer.writerow(data)
        # 5. 关闭文件
        f.close()