from typing import List

## Sample input to test the code
T = 1
case = 1
N = 3
citations_test = [5, 1, 2]
case = 2
N = 6
citations_test = [1, 3, 3, 2, 2, 15]


# function to solve the problem                                                                                                                                                                             
def h_index_calculator(citations: List) -> str:
    papers = []
    ans = []
    hindex = 0
    for i in citations:
        papers.append(i)
        if sorted(papers, reverse=True)[hindex] > hindex:
            hindex+=1
        ans.append(str(hindex))

    return ' '.join(ans)
    

# Submission code
"""
if __name__ == '__main__':
    
    T = int(input())
    for case in range(1, T+1):
        papers = int(input())
        citations = list(map(int, input().split()))
        print(f"Case #{case}: {h_index_calculator(papers, citations)}")
"""

# Test code

if __name__ == '__main__':

    for case in range(1, T+1):
        papers = N
        citations = citations_test
        print(f"Case #{case}: {h_index_calculator(papers, citations)}")
