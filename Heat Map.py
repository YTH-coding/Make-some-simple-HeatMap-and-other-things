import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib

matplotlib.rc("font",family='MicroSoft YaHei',weight="bold")

data = pd.read_excel('空气质量指数.xlsx',sheet_name = 'Sheet1')

a = [i for i in range(0,76,1)]  #构建索引

dataa = data.loc[data.index[a]]     #根据索引进行切片

data_array = dataa.values.T

cities = list()
city = ['福州','莆田','三明','泉州','漳州','南平','龙岩','宁德',]
city_num = [7,1,10,8,9,9,6,8]
a =0
for i in range(len(city)):
    for j in range(city_num[i]):
        cities.append("{} {}".format(city[i], data.columns[a]))
        a = a+1
        
months = list()
year = [24,23,22,21,20,19,18]
y_m = [4,12,12,12,12,12,12]
for i in range(len(year)):
    for j in reversed(range(y_m[i])):
        months.append("{}\n年\n{}\n月".format(year[i], j+1))
print(months)

plt.xticks(np.arange(len(months)), labels = months, fontsize=3)
plt.yticks(np.arange(len(cities)),labels=cities, fontsize=3.5)

plt.title("城市-月份-优良天数占比 Heat Map\n资料来源：福建省生态环境厅\n厦门,平潭资料暂缺(网站上没找到啊……)")

plt.imshow(data_array, cmap='RdYlGn_r')
plt.colorbar()
#plt.tight_layout()

plt.savefig("Figure-n.png", dpi=2000)

plt.show()
