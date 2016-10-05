from enum import Enum

Job = Enum ('Job', ('warrior','wizard','knight','pastor'))

for name, member in Job.__members__.items():
    print(name, '=>', member, ',', member.value)