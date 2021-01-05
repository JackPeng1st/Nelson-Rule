'''Coding by JackPeng 彭家祐 '''
# return True: 代表違反該rule --> 製程失控
def nelson1(series):
    #任一點超過 平均加減3個標準差
    stddev = np.std(series)
    mean = np.mean(series)
    tf = (np.abs((series - mean)) > 3.0*stddev).any()

    return tf

def nelson2(series):
    #連續9點都在平均之上or下
    mean = series.mean()
    #print("Mean:",mean)
    roll_mean = series.rolling(window=9).mean()
    for i in range(8,len(series)):
        if(series[i-8]>roll_mean[i] and series[i-7]>roll_mean[i] and series[i-6]>roll_mean[i] and series[i-5]>roll_mean[i] and series[i-4]>roll_mean[i]and series[i-3]>roll_mean[i]and series[i-2]>roll_mean[i]and series[i-1]>roll_mean[i]and series[i]>roll_mean[i]):
            return True
        elif(series[i-8]<roll_mean[i] and series[i-7]<roll_mean[i]and series[i-6]<roll_mean[i]and series[i-5]<roll_mean[i]and series[i-4]<roll_mean[i]and series[i-3]<roll_mean[i]and series[i-2]<roll_mean[i]and series[i-1]<roll_mean[i]and series[i]<roll_mean[i]):
            return True
        else : return False
        
def nelson3(series):
    for i in range(5,len(series)):
        if(series[i-5]<series[i-4]<series[i-3]<series[i-2]<series[i-1]<series[i]):
            return True
        elif(series[i-5]>series[i-4]>series[i-3]>series[i-2]>series[i-1]>series[i]):
            return True
        else: return False

def nelson4(series):
    for i in range(13,len(series)):
        if(series[i-13]>series[i-12] and series[i-12]<series[i-11] and series[i-11]>series[i-10] and series[i-10]<series[i-9] and series[i-9]>series[i-8] and series[i-8]<series[i-7]  and series[i-7]>series[i-6]  and series[i-6]<series[i-5] and  series[i-5]>series[i-4]  and series[i-4]<series[i-3]  and series[i-3]>series[i-2]  and series[i-2]<series[i-1]  and series[i-1]>series[i]):
            return True
        elif(series[i-13]<series[i-12] and series[i-12]>series[i-11] and series[i-11]<series[i-10] and series[i-10]>series[i-9] and series[i-9]<series[i-8]  and series[i-8]>series[i-7] and series[i-7]<series[i-6]  and series[i-6]>series[i-5]  and series[i-5]<series[i-4]  and series[i-4]>series[i-3]  and series[i-3]<series[i-2]  and series[i-2]>series[i-1]  and series[i-1]<series[i]):
            return True
        else: return False
        
def nelson5(series):
    stddev = np.std(series)
    mean = np.mean(series)
    threshold_up=2*stddev+mean
    threshold_down=mean-2*stddev
    for i in range(2,len(series)):
        num=0
        if(series[i-2]>threshold_up or series[i-2]<threshold_down): num+=1
        if(series[i-1]>threshold_up or series[i-1]<threshold_down): num+=1
        if(series[i]>threshold_up or series[i]<threshold_down): num+=1
        if(num>=2): return True
        return False
    
def nelson6(series):
    stddev = np.std(series)
    mean = np.mean(series)
    threshold_up=stddev+mean
    threshold_down=mean-stddev
    for i in range(4,len(series)):
        num=0
        if(series[i-4]>threshold_up or series[i-4]<threshold_down): num+=1
        if(series[i-3]>threshold_up or series[i-3]<threshold_down): num+=1
        if(series[i-2]>threshold_up or series[i-2]<threshold_down): num+=1
        if(series[i-1]>threshold_up or series[i-1]<threshold_down): num+=1
        if(series[i]>threshold_up or series[i]<threshold_down): num+=1
        if(num>=4): return True
        return False
    
def nelson7(series):
    stddev = np.std(series)
    mean = np.mean(series)
    threshold_up=stddev+mean
    threshold_down=mean-stddev
    for i in range(14,len(series)):
        if(threshold_down<series[i-14]< threshold_up and threshold_down<series[i-13]< threshold_up and threshold_down<series[i-12]< threshold_up and threshold_down<series[i-11]< threshold_up and threshold_down<series[i-10]< threshold_up and threshold_down<series[i-9]< threshold_up and threshold_down<series[i-8]< threshold_up and threshold_down<series[i-7]< threshold_up and threshold_down<series[i-6]< threshold_up and threshold_down<series[i-5]< threshold_up and threshold_down<series[i-4]< threshold_up and threshold_down<series[i-3]< threshold_up and threshold_down<series[i-2]< threshold_up and threshold_down<series[i-1]< threshold_up and threshold_down<series[i]< threshold_up):
            return True
    return False

def nelson8(series):
    stddev = np.std(series)
    mean = np.mean(series)
    threshold_up=stddev+mean
    threshold_down=mean-stddev
    for i in range(7, len(series)):
        if((series[i-7]>threshold_up or series[i-7]<threshold_down) and (series[i-6]>threshold_up or series[i-6]<threshold_down) and (series[i-5]>threshold_up or series[i-5]<threshold_down) and (series[i-4]>threshold_up or series[i-4]<threshold_down) and (series[i-3]>threshold_up or series[i-3]<threshold_down) and (series[i-2]>threshold_up or series[i-2]<threshold_down) and (series[i-1]>threshold_up or series[i-1]<threshold_down)and (series[i]>threshold_up or series[i]<threshold_down)):
            return True
    return False
