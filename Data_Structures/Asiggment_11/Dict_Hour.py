"""
    Write a program to read through the mbox-short.txt and figure out the distribution by hour of 
    the day for each of the messages. You can pull the hour out from the 'From ' line by finding 
    the time and then splitting the string a second time using a colon.

    From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

    Once you have accumulated the counts for each hour, print out the counts, sorted by hour as 
    shown below.
"""
fname = input("Enter file name: ") # mbox-short.txt
fh = open('./'+fname)
counts=dict()
for line in fh:
    line = line.rstrip()
    if not line.startswith('From '): continue
    words = (line.split()[5]).split(':')
    counts[words[0]]=counts.get(words[0],0)+1

counts_hours = {k: v for k, v in sorted(counts.items())}

for p , v in counts_hours.items():
    print(p , v)