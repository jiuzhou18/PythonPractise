from collections import namedtuple
Point = namedtuple ('Point', ['x','y'])
p = Point(1,2)
print(p.x,p.y)

from collections import defaultdict
dd = defaultdict(lambda: 'N/A')
dd[1] =15;
print(dd[2])

from collections import OrderedDict
od = OrderedDict([('b',2), ('c', 3), ('a', 1)])
print(od)

from collections import Counter
c = Counter()
for ch in 'knowledge':
    c[ch] = c[ch] +1
print(c)


