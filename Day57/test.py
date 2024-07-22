

labor = [[34,63],[35,55],[41,63],[43,63],[39,50],[37,47],[48,58],[44,50],[46,50],[48,61]]
tory = [[44,56],[42,49],[37,51],[36,47],[42,52],[42,58],[42,61],[46,52],[49,58],[50,55],[48,51]]

total = 0
for i in labor:
    total +=i[1] - i[0]
totalLabor = total/(len(labor))


total = 0
for i in tory:
    total +=i[1] - i[0]
totalTory= total/(len(labor))

print(f"The total for tories is {totalTory} ")
print(f"The total for labor is {totalLabor}")