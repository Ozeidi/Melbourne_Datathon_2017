#pip install geocoder
import geocoder
#Modify this to your own lookup folder
lookups = 'D:/Documents/IPython/Datathon/MelbDatathon2017/lookups/'
df_patients=pd.read_csv('{}patients.txt'.format(lookups), sep = '\t')
pc=df_patients.postcode.unique()

df_pc=pd.DataFrame(columns=['postcode'])
df_pc.postcode=pc

gc=Nominatim(view_box=(112.467,-55.050,168.000,-9.133),country_bias='Australia')


def get_cor(postcode):
    s_t=clock()
    loc=None
    while loc is None:
        try:
            loc=geocoder.google('{}, Australia'.format(postcode))
        except:
            print ("error")
        
    e_t=clock()
    time.append(e_t-s_t)
    print('{}:{}'.format(len(time),time[-1]),end=' , ')
    print ('{}'.format(postcode),end=',')
    print('{},{}'.format(loc.lng,loc.lat))
    return '{}#{}#{}'.format(loc.address,loc.lng,loc.lat)


df_pc=df_pc[:]
time=[]

df_pc['address,lon,lat']=df_pc['postcode'].apply(lambda x: get_cor(x))

df_pc['address'],df_pc['lon'],df_pc['lat']=df_pc['address,lon,lat'].str.split('#').str
df_pc=df_pc.drop('address,lon,lat',1)

# df_pc.lon=df_pc.lon.astype(float)
# df_pc.lat=df_pc.lat.astype(float)
df_pc
