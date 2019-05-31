
##In a car park, cars arrive at time, stay for a while then leave (as usual). A keeper is in charge of this car park. He is only payed when the car park is not empty. You want to give him an idea of his daily salary.

##With the given dates of arrival and departure of a set of cars, you must give the number of hours with at least one car in the park.

##Input
#Line 1:An integer 'N' for the no. of cars
#N next lines: For each car, 2 integers 'start' and 'end' for the hour of arrival and departure

##Output
#Line 1: The number of hours with at least one car in the park.

##Example        Output
# 3              14
# 2 5
# 8 13
# 14 20

##Code_solution   :D
n=int(input())
h=ss=ee=0
for i in range(n):
	s,e=[int(j) for j in input().split()]
	if ee<=s or e<ss:
		h+=(e-s)
	elif ee>s and e>ee:
		h+=(e-ee)
	elif s<ss and e>ss:
		h+=(ss-s)
	ss=s
	ee=e
print(h)
