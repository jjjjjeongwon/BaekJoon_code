import sys
input = sys.stdin.readline

N = int(input())
dict_a = {}

for i in range(N):
    node_list = input().strip().split()
    # dict_a에 {'A':('B', 'C'), ....} 이런식으로 넣음
    dict_a[node_list[0]] = node_list[1], node_list[2]


def preorder(node):
    print(node, end='')
    if dict_a[node][0] != '.':
        preorder(dict_a[node][0])
    if dict_a[node][1] != '.':
        preorder(dict_a[node][1])


def inorder(node):
    if dict_a[node][0] != '.':
        inorder(dict_a[node][0])
    print(node, end='')
    if dict_a[node][1] != '.':
        inorder(dict_a[node][1])


def postorder(node):
    if dict_a[node][0] != '.':
        postorder(dict_a[node][0])
    if dict_a[node][1] != '.':
        postorder(dict_a[node][1])
    print(node, end='')


preorder('A')
print()
inorder('A')
print()
postorder('A')
