I = float(input("公里数:(单位：公里)："))
prize = 0
totalPrize = 0
benefit = [6,4,2,0]
rat = [6,4,2,2]
for i in range(len(benefit)):    
    if I > benefit[i]:        
        prize = prize+(I-benefit[i])*rat[i]        
        I = benefit[i]        
        totalPrize = totalPrize + prize
        print("应发奖金为：{}元".format(totalPrize))