import argparse

parser = argparse.ArgumentParser()
parser.add_argument('nums', nargs = '*')
args = parser.parse_args()

sqr = []
num = []


for i in args.nums:
    try:
        i = int(i)
        sqr.append(i**2)
        num.append(i)
    except:
        pass
    
    

print(sqr)
a = [i for i in num if i<0]
if a: print(max(a))

