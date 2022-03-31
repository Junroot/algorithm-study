n, m = map(int, list(input().split()))

truth = set()
ans = 0

temp = input().split()

for i in range(1, int(temp[0])+1):
    truth.add(temp[i])
#print(truth)
party_member = []

for i in range(m):
    set_temp = set()
    temp = input().split()
    for j in range(1, int(temp[0])+1):
        set_temp.add(temp[j])
    party_member.append(set_temp)
#print(party_member)
cnt = 0
while cnt < m:
    for i in range(m):
        if len(truth & party_member[i]) > 0:
            truth|=party_member[i]
    cnt+=1
#print(truth)
for i in range(m):
    if len(truth & party_member[i]) == 0:
        ans+=1

print(ans)