def solveMaze(maze):
    ans=[[0 for i in range(4)]for j in range(4)]
    if findMazePath(maze,0,0,ans)==False:
        print("Solution cannot be found")
        return False
    printMaze(ans)
    return True

def findMazePath(maze,x,y,ans):
    if(x==3 and y==3):
        ans[x][y]=1
        return True
    if isSafe(maze,x,y)==True:
        ans[x][y]=1
        if findMazePath(maze,x+1,y,ans)==True:
            return True
        if findMazePath(maze,x,y+1,ans)==True:
            return True
        ans[x][y]=0
        return False

def isSafe(maze,x,y):
    if 0<=x<4 and 0<=y<4 and maze[x][y]==1:
        return True
    return False

def printMaze(ans):
    for i in ans:
        for j in i:
            print str(j)+"",
        print("")


def main():
    maze=[ [1, 0, 0, 0], 
             [1, 1, 0, 1], 
             [0, 1, 0, 0], 
             [1, 1, 1, 1] ] 
    solveMaze(maze)

main()