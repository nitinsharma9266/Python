from fpdf import FPDF

# Create PDF class object
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

# Title
pdf.set_font("Arial", 'B', 14)
pdf.cell(200, 10, txt="Category 12: Algorithms (100 Questions)", ln=True, align='C')
pdf.ln(10)

# Reset font for content
pdf.set_font("Arial", size=11)

# Content (all 100 questions)
content = """Category 12: Algorithms (100 questions, intermediate-hard)

1. Implement linear search.
2. Implement binary search.
3. Implement jump search.
4. Implement interpolation search.
5. Implement exponential search.
6. Implement bubble sort.
7. Implement selection sort.
8. Implement insertion sort.
9. Implement merge sort.
10. Implement quick sort.
11. Implement heap sort.
12. Implement counting sort.
13. Implement radix sort.
14. Implement bucket sort.
15. Find kth smallest element using sorting.
16. Find kth largest element using heap.
17. Find majority element in array.
18. Find missing number in 1 to N.
19. Find duplicate number in array.
20. Find all duplicates in array.
21. Find subarray with given sum.
22. Find maximum subarray sum (Kadane’s algorithm).
23. Find minimum subarray sum.
24. Find longest increasing subsequence.
25. Find longest decreasing subsequence.
26. Find longest common subsequence.
27. Find longest common substring.
28. Find edit distance between two strings.
29. Find minimum insertions to make string palindrome.
30. Find minimum deletions to make string palindrome.
31. Generate all subsets of a set.
32. Generate all permutations of a string.
33. Generate all combinations of numbers.
34. Solve N-Queens problem.
35. Solve Rat in a Maze problem.
36. Solve Sudoku puzzle.
37. Implement Tower of Hanoi.
38. Find shortest path in graph using BFS.
39. Find shortest path in weighted graph using Dijkstra.
40. Find shortest path in graph with negative weights using Bellman-Ford.
41. Find all-pairs shortest path using Floyd-Warshall.
42. Implement Prim’s algorithm for MST.
43. Implement Kruskal’s algorithm for MST.
44. Detect cycle in undirected graph using DFS.
45. Detect cycle in directed graph using DFS.
46. Check if graph is bipartite.
47. Count connected components in graph.
48. Find topological ordering of graph.
49. Find strongly connected components (Kosaraju’s algorithm).
50. Implement union-find (disjoint set).
51. Find minimum spanning tree weight.
52. Count number of islands in a grid.
53. Solve word search in a grid.
54. Find maximum area of island in grid.
55. Find surrounded regions in matrix.
56. Implement binary tree traversal (inorder).
57. Implement binary tree traversal (preorder).
58. Implement binary tree traversal (postorder).
59. Implement level order traversal.
60. Find height of binary tree.
61. Find diameter of binary tree.
62. Check if binary tree is balanced.
63. Find lowest common ancestor in binary tree.
64. Find lowest common ancestor in BST.
65. Serialize and deserialize binary tree.
66. Check if two trees are identical.
67. Check if tree is symmetric.
68. Find maximum path sum in binary tree.
69. Convert sorted array to BST.
70. Convert sorted linked list to BST.
71. Implement trie insert and search.
72. Find longest prefix match using trie.
73. Count distinct substrings using trie.
74. Find shortest unique prefix for each word.
75. Implement hash table using chaining.
76. Implement hash table using open addressing.
77. Find two sum problem.
78. Find three sum problem.
79. Find four sum problem.
80. Find maximum product subarray.
81. Find minimum product subarray.
82. Find maximum circular subarray sum.
83. Find maximum sum rectangle in 2D matrix.
84. Find largest square of 1’s in binary matrix.
85. Find largest rectangle in histogram.
86. Find largest rectangle of 1’s in binary matrix.
87. Implement LRU cache.
88. Implement LFU cache.
89. Find median of data stream.
90. Find kth largest element in data stream.
91. Implement heap with insert and extract.
92. Implement priority queue.
93. Implement segment tree for sum queries.
94. Implement segment tree for min queries.
95. Implement Fenwick tree (Binary Indexed Tree).
96. Implement sparse table for RMQ.
97. Find longest palindromic substring.
98. Find longest palindromic subsequence.
99. Find minimum cuts for palindrome partitioning.
100. Implement Rabin-Karp algorithm for substring search.
"""

# Add text to PDF
pdf.multi_cell(0, 8, content)

# Save PDF
pdf.output("Category_12_Algorithms.pdf")

print("✅ PDF generated successfully: Category_12_Algorithms.pdf")