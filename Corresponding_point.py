import glob



def check_dis(dis , num , n):
    for i in range(n):
        if dis[i] == num:
            return 0
    return 1

def eight_q(min_sum , rec_dis , dis , dis_2 , line , n , m , sum, test):
    if line == n:
        return
    for i in range(m):
        if check_dis(dis , i , n):
            
            dis[line] = i
            sum += dis_2[line][i]
            if line == (n - 1):
                if min_sum[0] == -1 or min_sum[0] > sum:
                    test=test+1
                    for j in range(n):
                        rec_dis[j] = dis[j]
                    min_sum[0] = sum
                dis[line] = -1
                sum -= dis_2[line][i]
                continue
            test = eight_q(min_sum , rec_dis , dis , dis_2 , line + 1 , n , m , sum, test)
            dis[line] = -1
            sum -= dis_2[line][i]
            
    return test

def match_point():

    pre_x = [258,288,385,277,330]
    pre_y = [263,279,255,307,371]

    mak_x = [391,261,284,292,338]
    mak_y = [250,266,310,282,373]
        
    pre_sum = len(pre_x)
    mak_sum = len(mak_x)
    result_num = pre_sum -  mak_sum   # 0為偵測跟標記數量一樣 >0為偵測數量較多 <0為標記數量較多
    
    n = min(pre_sum , mak_sum)
    m = max(pre_sum , mak_sum)
    dis = [-1 for _ in range(n)]
    dis_2 = [[0 for _ in range(m)] for _ in range(n)]
    
    if pre_sum <= mak_sum:
        for i in range(pre_sum):
            for j in range(mak_sum):
                dis_2[i][j] = (pre_x[i] - mak_x[j]) ** 2 + (pre_y[i] - mak_y[j]) ** 2
    else:
        for i in range(mak_sum):
            for j in range(pre_sum):
                dis_2[i][j] = (pre_x[j] - mak_x[i]) ** 2 + (pre_y[j] - mak_y[i]) ** 2
    
    min_sum = []
    min_sum.append(-1)
    rec_dis = [-1 for _ in range(n)]
    
    test= 0
    test = eight_q(min_sum , rec_dis , dis , dis_2 , 0 , n , m , -1, test)
    print(test)
    
    return result_num , rec_dis , dis_2, n , m

def mre():
    return
      


result_sum , rec_dis , dis_2, n , m = match_point()
print(rec_dis)
print(dis_2)


'''
    708.txt
    pre_x = [258,288,385,277,330]
    pre_y = [263,279,255,307,371]

    mak_x = [391,261,284,292,338]
    mak_y = [250,266,310,282,373]



    725.txt
    pre_x = [450,305,348,460,396,280,371,349,280]
    pre_y = [381,437,395,419,478,353,406,360,412]

    mak_x = [277,349,349,332,280,304,450,370,458,395]
    mak_y = [354,361,395,405,412,436,384,406,421,481]

    738.txt
    pre_x = [291,303,342,281,385,336,334,276,294]
    pre_y = [282,217,352,382,376,320,246,364,294]

    mak_x = [399,332,337,356,418,353,380,434,389,362,391,331,339,277,290,287,309,291,318]
    mak_y = [249,302,312,328,345,345,354,417,401,396,425,390,420,393,406,367,395,355,373]

'''

  
