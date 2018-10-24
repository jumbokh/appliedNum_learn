#http://xiaorui.cc

#coding:utf-8
from prettytable import PrettyTable

a = {'20160202': 48519,
 '20160203': 65883,
 '20160206': 2290,
 '20160210': 2115,
 '20160212': 2406,
 '20160213': 2105}

for i,j in a.items():
    print '-----------------------------'
    print '|__%s__|_____%s_____|'%(i,j)


x = PrettyTable(["datetime","count" ])
x.padding_width = 1
for i,j in a.items():
    x.add_row([i,j])
print x


col = PrettyTable()
col.add_column("City name",["Adelaide","Brisbane","Darwin","Hobart","Sydney","Melbourne","Perth"])
col.add_column("Area", [1295, 5905, 112, 1357, 2058, 1566, 5386])
col.add_column("Population", [1158259, 1857594, 120900, 205556, 4336374, 3806092, 1554769])
col.add_column("Annual Rainfall",[600.5, 1146.4, 1714.7, 619.5, 1214.8, 646.9, 869.4])
print col

mix = PrettyTable()
mix.field_names = ["City name", "Area"]
mix.add_row(["Adelaide",1295])
mix.add_row(["Brisbane",5905])
mix.add_row(["Darwin", 112])
mix.add_row(["Hobart", 1357])
mix.add_row(["Sydney", 2058])
mix.add_row(["Melbourne", 1566])
mix.add_row(["Perth", 5386])
mix.add_column("Population", [1158259, 1857594, 120900, 205556, 4336374, 3806092, 1554769])
mix.add_column("Annual Rainfall",[600.5, 1146.4, 1714.7, 619.5, 1214.8, 646.9, 869.4])

print mix