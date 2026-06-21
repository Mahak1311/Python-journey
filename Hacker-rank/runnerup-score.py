'''
Given the participants' score sheet for your University Sports Day, 
you are required to find the runner-up score.
 You are given  scores. Store them in a list
   and find the score of the runner-up.
'''
n = int(input())

scores = list(map(int, input().split()))

runner_up = sorted(set(scores))[-2]

print(runner_up)