matA=[[1,2],[3,4],[5,6]]
matB=[[10,20],[30,40],[50,60]]
matC = [] 
for i in range(len(matA)):
 csub = []
 for j in range(len(matA[i])):
 s = matA[i][j] + matB[i][j] ##공백이니까 c[][j]안돼 대괄호 하나 만들고 append
 csub.append(s)
 matC.append(csub) ##2번씩돌리고 최종~~
 
print(matC)
