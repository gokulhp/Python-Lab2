string = 'mashupstack'

rptrs = []

for i in string:
    if string.count(i) > 1:
     if i not in rptrs:
      rptrs.append(i)

print('The repeated characters are. : ',rptrs)    
print('No. of repeated characters. : ',len(rptrs))