#learn how to declare and use classes and functions in python
from similarity import hamming,jaccard,simpson
# import similarity

A = input("Input A:")
B = input("Input B:")

ans = jaccard.jaccard
print("The Jaccard coeffcient between",A,"and",B, "is",ans.calc(list(A), list(B)),".")

ans = simpson.simpson
print("The Overlap coeffcient between",A,"and",B, "is",ans.calc(list(A), list(B)),".")

ans = hamming.hamming
print("The Hamming coeffcient between",A,"and",B, "is",ans.calc(A,B),".")
