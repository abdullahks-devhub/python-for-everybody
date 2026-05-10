# Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
hourDict = dict()
#Retreiving hour from the file and making histogram for them
for line in handle:
    line = line.strip()
    if line.startswith("From "):
        words = line.split()
        time = words[-2]
        time = time.split(":")
        hour = time[0]
        hourDict[hour] = hourDict.get(hour, 0) + 1
#Sorting the list
sortedHourDict = sorted(hourDict.items())
for key, value in sortedHourDict:
    print(key, value)
    
