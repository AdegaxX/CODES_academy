from enum import Enum

Names = Enum('Names', [('Waiz',8),('Tom',5),('Sara',7),('Lee',6)])

print(Names.Sara.value)
print(Names.Waiz.value)