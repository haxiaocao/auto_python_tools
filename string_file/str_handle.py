
res={}
voter=[]
file_name="sample.txt"

for line in open(file_name,'r'):
    s=line.capitalize().strip()
    name,vote=s.split(" - ")
    # print '{},{}'.format(name,vote)
    if name in voter:
        print 'Warning, the person want to vote twice, I will pass it any way:{}'.format(name)
        continue
    if vote not in res:
        res[vote]=0
    res[vote]+=1
    voter.append(name)

print res.keys().count
for k in res.keys():
    print 'name:{}, its Count:{}'.format(k,res[k])
