print("1부터 10까지의 합을 구하는 프로그램")
sum = 1;                                #초기 합을 1로 정한다 (1부터 1까지의 합)
for i in range(10-1):                   #9회동안 (i값에 차례로 0~8까지 대입이 된다)
    print (sum,'+',i+2,'=', sum+i+2)    #합에 i+2를 더하는 식을 print로 보여준다
    sum = sum+i+2                       #합에 i+2의 값을 더해준다
    pass                                #
