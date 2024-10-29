import yfinance as yf
import pandas as pd
import plotly.express as px

scrip = "ITC.NS TCS.NS LTFOODS.NS"

returns = []
scrips = scrip.split(" ") 
itr  = len(scrip.split(" "))

for its in range(itr):
    print(its)


df = yf.download(scrip, period="1y")

#print(df)

df2=df.reset_index()

# print("Convert multi level indexes to columns:\n", df2)

df.index = df.index.set_names(['new_index1'])

df2 = df.reset_index(level=[0])
# # print("Convert multi level indexes to single index:\n", df2)

df.index = df.index.set_names(['new_index1'])

df2 = df.reset_index(level=[0])
# # print("Convert multi level indexes to single index:\n", df2)

df2 = df.reset_index(level=[0], drop=True)
# # print(df2)

df.columns = df.columns.get_level_values(1)
#print(df.iloc[:, 0])
df.reset_index(drop=True, inplace=True)
# val = df.iloc[:, 0]

# #print(val[0])
# last_val = round(val.tail(1).item())
# print(last_val)

for its in range(itr):
    val = df.iloc[:, its]
    first_val = round(val[0])
    last_val = round(val.tail(1).item())
    #print(first_val)
    #print(last_val)
    change = round((last_val-first_val)/first_val*100)
    print(change)
    returns.append(change)


# print(scrips)
# print(returns)



df3 = pd.DataFrame(list(zip(scrips, returns)),columns =['Stock', 'Return'])

#print(df3)

fig = px.bar(df3, x='Stock',y='Return',color=scrips,width=800,height=600).update_traces(width=0.2)
fig.update_layout(bargap=0.0,bargroupgap=0)
fig.update_yaxes(automargin=True)
fig.show()
# for x in val.values:
#     print(x)

# for x in val1.values:
#     print(type(x))

