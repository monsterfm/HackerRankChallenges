# Enter your code here. Read input from STDIN. Print output to STDOUT

nAndm = list(raw_input().split())
nIntegers = list(raw_input().split())
mA = set(raw_input().split())
mB = set(raw_input().split())
hapiness=0
for x in nIntegers:
 if x in mA:
  hapiness += 1
 elif x in mB:
  hapiness -= 1

print(hapiness)
