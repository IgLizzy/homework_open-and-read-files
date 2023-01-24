txt4 = []
with open('1.txt', 'rt', encoding='utf-8') as f:
    res1 = f.readlines()
    len1txt = len(res1)
    txt4.append(res1)

with open('2.txt', 'rt', encoding='utf-8') as f:
    res2 = f.readlines()
    txt4.append(res2)
    len2txt = len(res2)
 
with open('3.txt', 'rt', encoding='utf-8') as f:
    res3 = f.readlines()
    txt4.append(res3)
    len3txt = len(res3)

txt4.sort(key=len)

f = open('sum.txt', 'w', encoding='utf-8')
f.write('2.txt\n')
f.write(f"{str(len2txt)}\n")
f.write(f"{''.join(txt4[0])}\n")
f.write('1.txt\n')
f.write(f"{str(len1txt)}\n")
f.write(f"{''.join(txt4[1])}\n")
f.write('3.txt\n')
f.write(f"{str(len3txt)}\n")
f.write(f"{''.join(txt4[2])}\n")
f.close()