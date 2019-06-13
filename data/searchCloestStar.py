def searchCloestStar(x,y,database):
    #figsize
    file_name_dict={'BSC':"./BSC.csv",'Hipparcos':'./hip_small.csv'}
    file_name=file_name_dict[ database]
    df=pd.read_csv(file_name)
    select=df[(df['J2000_a']<=(np.round(x,2)+1)) & (df['J2000_a']>(np.round(x,2))) 
              & (df['J2000_d']<=(np.round(y,2)+1)) & (df['J2000_d']>(np.round(x,2)))]
    if len(select)==0:
        return None
    select=select[select.Vmag==max(select.Vmag)]
    d={}
    if database=='BSC':
        d['Number']='SAO '+str(select['SAO'].tolist()[0])
        d['Name']=str(select['name'].tolist()[0])
    elif database=='Hipparcos':
        d['HIP CODE']=str(select['Hcode'].tolist()[0])
    d['B-V']=str(round(select['BV'].tolist()[0],4))
    d['SPtype']=str(select['SPtype'].tolist()[0])
    d['RAhms']=str(select['RAhms'].tolist()[0])
    d['DEdms']=str(select['DEdms'].tolist()[0])
    d['GLON']=str(select['l'].tolist()[0])
    d['GLAT']=str(select['b'].tolist()[0])
    return d