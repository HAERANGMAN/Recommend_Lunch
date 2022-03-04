import pandas as pd

aa = [[1,2,3,], [4,5,6],[7,8,9]]
bb = ['a','b','c']
cc = ['A','B','C']

dd = ['aa', 'bb', 'cc']
ee = ['index','columns','values']

pd_abc=pd.DataFrame(aa, index=bb, columns=cc)
pd_val = pd_abc.values

print(pd_abc)

print("ASDf", pd_abc.index)

print("="*60)

for i in ee:
    pp=pd_abc+i
    print("Result of %s in DataFrame : " %i + pp)
