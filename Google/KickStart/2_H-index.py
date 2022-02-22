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
def h_index_calculator(papers: int, citations: List) -> str:
    h_index = 0
    rolling_citations = []
    h_index_evolution = []

    for paper in range(1, papers+1):
        
        paper_citation = citations[paper-1]
        
        if paper_citation > paper:
            rolling_citations.append(paper_citation)
            rolling_citations = [cit for cit in rolling_citations if cit > h_index]
            if len(rolling_citations) > h_index:
                h_index += 1

        elif paper_citation > h_index:
            rolling_citations.append(paper_citation)
            if len(rolling_citations) > h_index:
                h_index += 1
            
            rolling_citations = [cit for cit in rolling_citations if cit > h_index]
        
        
        h_index_evolution.append(h_index)

    #return "Case #{}: {}".format(case, *h_index_evolution)
    return ' '.join(map(str, h_index_evolution))
    

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
