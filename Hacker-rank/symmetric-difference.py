'''
Given 2 sets of integers, M and N, print their symmetric difference in ascending order.
 The term symmetric difference indicates those values that exist in either M or N but do not exist in both.
 input format:
   The first line of input contains an integer,M . 
   The second line contains M space-separated integers. 
   The third line contains an integer,N . 
   The fourth line contains N space-separated integers.

'''
m = int(input())
A = set(map(int, input().split()))

n = int(input())
B = set(map(int, input().split()))

result = sorted(A ^ B)

for num in result:
    print(num)