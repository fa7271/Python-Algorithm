import sys
from collections import defaultdict

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

sys.setrecursionlimit(10**7)

folder_contents = defaultdict(set)   # key: 폴더 이름, value: 하위 폴더 이름 set
file_contents = defaultdict(set)     # key: 폴더 이름, value: 파일 이름 set

def init(parent_folder, name, is_folder):
    if is_folder == 1:
        folder_contents[parent_folder].add(name)
    else:
        file_contents[parent_folder].add(name)

def move_folder(from_folder, to_folder):
    if from_folder in folder_contents:
        folder_contents[to_folder].update(folder_contents[from_folder])
        del folder_contents[from_folder]
    if from_folder in file_contents:
        file_contents[to_folder].update(file_contents[from_folder])
        del file_contents[from_folder]

def find_files(folder, unique_files, total_files):
    if folder in folder_contents:
        for sub_folder in folder_contents[folder]:
            find_files(sub_folder, unique_files, total_files)
    if folder in file_contents:
        for file in file_contents[folder]:
            unique_files.add(file)
            total_files[0] += 1



N, M = map(int, input().split())

for _ in range(N + M):
    P, F, C = input().split()
    C = int(C)
    init(P, F, C)

K = int(input())
for _ in range(K):
    from_path, to_path = input().split()
    from_folder = from_path.split('/')[-1]
    to_folder = to_path.split('/')[-1]
    move_folder(from_folder, to_folder)

Q = int(input())
result = []
def solution(folder):
    unique_files = set()
    total_files = [0]
    find_files(folder, unique_files, total_files)
    return len(unique_files), total_files[0]

for _ in range(Q):
    start = input().strip().split('/')[-1]
    res_file_kind, res_file_all = solution(start)
    result.append(f"{res_file_kind} {res_file_all}")

print('\n'.join(result))