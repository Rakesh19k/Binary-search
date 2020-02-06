pos=-1
def search(list1,n):
	low=0
	high=len(list1)-1
	Found=False
	while low<=high and not Found:
		mid = (low+high)//2
		if list1[mid] == n:
			globals()["pos"] = mid
			Found = True
		elif list1[mid]<n:
			low=mid+1
		else:
			high=mid-1
	if Found==True:
		print ("Found at and position is", pos+1)
	else:
		print ("Not Found")
list1=[89465,4,7,8,12,45,99,1236,89510,57469]
list1.sort()
n=int(input("enter the number: "))
search(list1,n)