import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler, MultiLabelBinarizer
from sklearn.cluster import KMeans
from sklearn.metrics.pairwise import euclidean_distances

# Load and process data
df = pd.read_csv("anime.csv")
df["genre"] = df["genre"].fillna('')
df["genre"] = df["genre"].apply(lambda x: [i.strip() for i in x.split(",")])

mlb = MultiLabelBinarizer()
genre_dummy = pd.DataFrame(mlb.fit_transform(df["genre"]), columns=mlb.classes_)

type_dummy = pd.get_dummies(df["type"], prefix="type").astype(int)

df['episodes'] = df['episodes'].replace('Unknown', np.nan)
df['episodes'] = pd.to_numeric(df['episodes'], errors='coerce').fillna(0).astype(int)
df['rating'] = df['rating'].fillna(df["rating"].median())
df['members'] = df['members'].fillna(df['members'].median())

sc = StandardScaler()
scaled = pd.DataFrame(sc.fit_transform(df[["episodes", "rating", "members"]]), columns=['episodes', 'rating', 'members'])

features = pd.concat([genre_dummy, type_dummy, scaled], axis=1)

km = KMeans(n_clusters=22)
df["cluster"] = km.fit_predict(features)


def recommend(aname):
    aname = aname.upper()
    if aname not in df["name"].str.upper().values:
        return [f"{aname} not found"], False

    ind = df[df["name"].str.upper() == aname].index[0]
    cluster = df.loc[ind, "cluster"]
    similar = df[(df["cluster"] == cluster) & (df.index != ind)]
    dist = euclidean_distances([features.loc[ind]], features.loc[similar.index])[0]
    answer = similar.iloc[dist.argsort()[:5]]
    return answer[["name", "rating", "episodes"]].to_dict(orient="records"), True
