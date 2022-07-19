cookie='khaos=L4JTW9ZG-11-E0LI; audit=1|2N/XRB8AvUKNwBNe0X1TG5C3OSmufUnm02eYs1wv6sPRp88VM5hoM1e/FpD/mR+rsGn3Vy1jqGciZ07GJqnMnjnLWfCJ7b188V0kxMR6Y5FQnzwZf+fkgQ=='
data=cookie.split('; ')

f={}
for i in data:
    j=i.split('=')
    f[j[0]]=j[1]

print(f)