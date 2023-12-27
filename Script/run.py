#from script1 import playlist
from script2 import *
from script4 import Titles


# Access to the API
token = access_token()

# Request with the access token :
headers = {
    'Authorization': f'Bearer {token}',
}
"""
ids = [get_track_id('Lose Yourself', headers), get_track_id('Verona', headers)]
print(ids)

print(get_track_features(ids, headers))

playlist0 = playlist
#print(playlist0)
Titles = pd.DataFrame({'Title': playlist0})
#print(Titles)
"""

Features = get_features_labels(headers)
#print(Features)

"""
Titles['track_id'] = Titles['Title'].apply(get_track_id,args=(headers,))
"""

nb_musiques = len(Titles.index)
print("il y a", nb_musiques, "différentes musiques")
nb_utilisation_token = nb_musiques // 100 + int(nb_musiques % 100 =! 0)

for k in range(nb_utilisation_token-1):
    l = l + get_track_features(Titles['track_id'][10*k:10*(k+1)].tolist(),headers)
l = l +

"""
Titles['track_features'] = Titles['track_id'].apply(get_track_features,args=(headers,))
Titles['track_features'] = Titles['track_features'].apply(lambda x: x.get('audio_features'))
Titles['track_features'] = Titles['track_features'].apply(lambda x: x[0])

for feature in Features:
    Titles[feature] = Titles['track_features'].apply(lambda x: x.get(feature))
Titles.drop(columns=['track_features'], inplace = True)

print(Titles.head())
"""
"""
path = '/home/onyxia/work/Python-pour-la-Data-Science/Data/data/Titles.csv'
Titles.to_csv(path, index=False)
"""