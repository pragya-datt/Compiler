var = []
rules = []

f = open('C:\Pragya\Sem5\compilerLab\gram', "r")
for line in f.readlines():
    for i in range(len(line)):
        if line[i] == '\'':
            if (line[i-1]+"'") not in var:
                var.append(line[i-1]+"'")
        if ord(line[i])>=65 and ord(line[i])<=90 and line[i] not in var:
            var.append(line[i])
    rule = line[:-1].split('=')
    if ("/" in rule[1]):
        gen = rule[1].split('/')
        for x in gen:
            rules.append([rule[0].strip(), x.strip()])
    else:
        rule[0] = rule[0].strip()
        rule[1] = rule[1].strip()
        rules.append(rule)
f.close()

first = {}
for a in rules:
    x = []
    for i in rules:
        if a[0] == i[0]:
            if a[1][0] not in x and a[1][0] not in var:
                x.append(i[1][0])
            if a[1][0] in var:
                found = False
                v = a[1][0]
                while(found==False):
                    for q in rules:
                        if q[0] == v and q[1][0] in var:
                            v = q[1][0]
                        if q[0] == v and q[1][0] not in var:
                            x.append(q[1][0])
                            found = True
    first[a[0]] = x

print("\n".join("{}: {}".format(k, v) for k, v in first.items()))
