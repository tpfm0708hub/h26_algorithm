import sys

def func_01():
    input_01 = sys.stdin.read().split()
    
    for i in range(0, len(input_01), 2):
        n = int(input_01[i])
        s = int(input_01[i+1])
        
        print(s // (n + 1))

if __name__ == "__main__":
    func_01()