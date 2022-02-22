from typing import List
import heapq

## Sample input to test the code
T = 1
case = 1
N = 3
citations_test = [5, 1, 2]
case = 2
N = 6
citations_test = [1, 3, 3, 2, 2, 15]


# function to solve the problem                                                                                                                                                                             
def calculate_hindex(N: int citations: List) -> str:
    minH = []
    ans = []
    hindex = 0
    for i in range(N):
      if citations[i]>hindex:
        heapq.heappush(minH,citations[i])
      while minH and minH[0] <= hindex:
        heapq.heappop(minH)
      if len(minH) >= hindex+1:
        hindex += 1
        ans.append(hindex)

    return ans
    

# Submission code
"""
if __name__ == '__main__':
    
    T = int(input())
    for case in range(1, T+1):
        papers = int(input())
        citations = list(map(int, input().split()))
        print(f"Case #{case}: {calculate_hindex(papers, citations)}")
"""

# Test code

if __name__ == '__main__':

    for case in range(1, T+1):
        papers = N
        citations = citations_test
        print(f"Case #{case}: {calculate_hindex(papers, citations)}")
