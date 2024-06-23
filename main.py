from metrics.utils import get_data
from metrics.pbv_pe import get_pbv_mulitplier
from metrics.pt_intrinsic_value import get_pt_intrinsic_value
from pandas import DataFrame 

symbols = ['AAPL', 'OXY']
df_obj = {}
for symbol in symbols:
    data = get_data(symbol)
    df_obj[symbol] = {}
    pbv = get_pbv_mulitplier(data)
    pl = get_pt_intrinsic_value(data)
    df_obj[symbol]['p_lynch'] = pl
    df_obj[symbol]['fep_pbv'] = pbv['fep_pbv']
    df_obj[symbol]['tep_pbv'] = pbv['tep_pbv']

df = DataFrame(df_obj)
# df.T switches rows and keys
print(df)
print(pbv)