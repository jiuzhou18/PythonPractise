# verify email format
import re

re_email = re.compile(r'^([0-9a-zA-Z\_\.]+)@([0-9a-zA-Z]+\.[a-z]+)$')
s1 = 'someone@gmail.com'
s2 = 'bill.gates@microsoft.com'
print('Match s1:', re_email.match(s1).groups())
print('Match s2:', re_email.match(s2).groups())

re_emailv2 = re.compile(r'^<([a-zA-Z]+)\s+([a-zA-Z]+)>\s+[0-9a-zA-Z\_\.]+@[0-9a-zA-Z]+\.\w{2,4}$')
s3 = '<Tom Paris> tom@voyager.org'
m1 = re_emailv2.match(s3)
print('The master of s3:', m1.group(1), m1.group(2))


