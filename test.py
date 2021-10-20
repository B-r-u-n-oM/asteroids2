#for tests

records = [line.split(",") for line in open("records.csv")]
records.sort(key=lambda x: -int(x[2]))
records = records[:5]
with open("records.csv", 'w') as data:
    for r in records:
        r[0] = records.index(r) + 1
        r[2] = str(r[2]) + "\n" if not "\n" in r[2] else r[2]
        line = str(r[0]) + "," + str(r[1]) + "," + r[2]
        data.write(line)

"""
1, fulano, 2005
2, bruno, 2003
3, conceicao, 1000
4,, 210
5, sebastiao, 105
"""

