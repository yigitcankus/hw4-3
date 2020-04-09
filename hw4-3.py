import pandas as pd
import numpy as np
import scipy
import warnings
warnings.filterwarnings('ignore')

"""
Veri kümesinde yer alan değişkenlerinin tiplerini ve her bir değişkenin eksik (null) değer oranını bulun.
"""
"""
primary key, state ve, year kategorik değişkenler, diğerleri sürekli değişken.
"""
states = pd.read_csv("states_all.csv")
# print(states.info())
#print(states.isnull().sum())
#print(states.isnull().count())
# print(states.isnull().sum()/states.isnull().count()*100)

######2
"""
Verimizde yıl (year) sütunu olduğunu farketmişsinizdir.
Şimdilik yıl verisini unutun ve her bir gözlemin aynı yıl içerisinde yapıldığını farz edin. 
Her bir değişken için eksik değerleri nasıl doldurabileceğinizi düşünün. 
Eksik değerleri bir değerle doldurmak hangi değişkenler için anlamlı, hangileri için anlamsızdır?
"""
# #for sutun_adi in states:
# #     for deger in states[sutun_adi]:
# #         if pd.isna(deger):
# #             states[sutun_adi].fillna(states[sutun_adi].mean(), inplace=True)

"""
Sayısal olan sürekli değişkenler için mantıklı olabilir. Ama State ve primarykey için doğru olacğaını sanmıyorum.
"""

######3
"""
Şimdi zaman faktörünü dikkate alma zamanı! 
2. sorudaki cevabınızı tekrar gözden geçirin ve eksik verileri o yıl içerisinde gözlemlenen değerlere dayanarak doldurun. 
Örneğin, bir değeri ortalama değer ile doldurmak isterseniz, o yılın ortalamasını hesaplayın.
"""
# yillar = states["YEAR"].unique()
#
# for yil in yillar:
#     print(states[states["YEAR"] == yil])
#
#
# sutun_list = states.columns
# print(sutun_list)
#
# for sutun in sutun_list:
#     if states[sutun].dtype == float:
#         states.fillna(states.mean(), inplace=True)
#
#
#
#
# print(states.isnull().sum()/states.isnull().count()*100)
# print(states.head(20))


#######4
"""
Bu sefer, eksik değerleri enterpolasyon yaparak doldurun.
"""

states = states.interpolate()
print(states.head(20))