#Problem F (PUBG BATTLE GROUND) By Shreyansh

#code to take input from input.txt
#and display output on output.txt 
import sys
sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt','w')

#python3 code
#to take input of no. of test cases
t=int(input())
#looping for the t test cases
while t:
    t=t-1
    # n here is no of players
    n=int(input())
    # taking input of array (List in pythyon) 'strength'
    # which stores the initial strength of the players
    strength=list(map(int,input().split()))
    #casting that array into set 's'
    #set is a data structure where no duplicate entries are allowed
    s=set(strength)
    #looping till the length of set 's' is not equal to 1
    while(len(s)!=1):
        # 'm' stores the minimmum value stored in set 's' 
        m=min(s)
        ''' here 'z' is referring to the copy created
            of the set 's'
            whenever we are entering into the loop
        '''
        z=s.copy()
        # iterating through all the elements in z
        for i in z:
            if i==m:
                continue
            s.remove(i)
            s.add(i%m)
        # removing zero present inside our set
        if 0 in s:
            s.remove(0)
    # once we get the now there is only one element in the set
    #we print that element
    print(list(s)[0])
