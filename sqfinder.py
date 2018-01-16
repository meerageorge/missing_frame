#!/usr/bin/python2.7
import os
import subprocess as lx

filepath = raw_input("please enter file path: ")#fetch file folder to the anim seq
seq_lst=os.listdir(filepath)
temp=[]
#retriving the seq num on the file name
for item in seq_lst:
	s=item.split(".")
	temp.append(s[1])
temp=temp[1:]
seq_of_render=[]

#converting seq list to int and sorting 
for item in temp:
	seq_of_render.append(int(item))
seq_of_render.sort()

#creating list of initial and final range in between missing seq
ranges = sum((list(t) for t in zip(seq_of_render, seq_of_render[1:]) if t[0]+1 != t[1]), [])
#print str(ranges)
Newls=seq_of_render[0:1] + ranges + seq_of_render[-1:]
#print Newls


#making the req list of frame range excluding missing frame range
L1=[]

count =0
while count < len(Newls):
	if Newls[count]==Newls[count+1]:
		L1.append(Newls[count])
		count=count+1
	else:
		L1.append(str(Newls[count])+'-'+str(Newls[count+1]))
		count=count+1
	count=count+1
		
		


print str(L1)

