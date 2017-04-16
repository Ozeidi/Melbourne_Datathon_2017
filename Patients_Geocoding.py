pc=df_patients.postcode.unique()

df_pc=pd.DataFrame(columns=['postcode'])
df_pc.postcode=pc

def get_cor(postcode):
    s_t=clock()
    loc=None
    while loc is None:
        try:
            loc=geo.geocode('{}, Australia'.format(postcode))
        except:
            print ("error")
        
    e_t=clock()
    time.append(e_t-s_t)
    print('{}:{}'.format(len(time),time[-1]),end=' , ')
    print ('{}'.format(postcode),end=',')
    print('{},{}'.format(loc.longitude,loc.latitude))
    return '{}#{}#{}'.format(loc.address,loc.longitude,loc.latitude)


df_pc=df_pc[:]
time=[]

df_pc['address,lon,lat']=df_pc['postcode'].apply(lambda x: get_cor(x))

df_pc['address'],df_pc['lon'],df_pc['lat']=df_pc['address,lon,lat'].str.split('#').str
df_pc=df_pc.drop('address,lon,lat',1)

df_pc.lon=df_pc.lon.astype(float)
df_pc.lat=df_pc.lat.astype(float)
df_pc
