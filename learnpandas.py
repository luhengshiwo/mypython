from pandas import Series,DataFrame
import pandas as pd
import numpy as np
obj = Series([1,2,-3,4])
print obj
print obj.values
print obj.index
obj2 = Series([1,2,-3,4],index = ["a","d","b","c"])
print obj2
obj3=obj2.reindex(list("abcd"))
print obj3
obj4= DataFrame(np.random.randn(4,6),columns=list("abcdef"),index=list("love"))
print obj4