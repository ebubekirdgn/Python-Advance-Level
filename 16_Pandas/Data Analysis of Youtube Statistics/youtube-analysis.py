from numpy import fabs
import pandas as pd
from pandas.core import groupby

df = pd.read_csv("youtube-ing.csv")
result = df

# 1- İlk 10 kaydı getiriniz.
result = df.head(10)

# 2- İkinci 5 kaydı getiriniz.
result = df[5:].head()

# 3- Dataset' de bulunan kolon isimleri ve sayısını bulunuz.
#result = df.count() 1. yontem
result = df.columns
result = len(df.columns)

# 4- Aşağıda bulunan bazı kolonları silin ve kalan kolonları listeleyiniz.
# (thumbnail_link,comments_disabled,ratings_disabled,video_error_or_removed,description)
df.drop(["thumbnail_link","comments_disabled","ratings_disabled","video_error_or_removed","description","trending_date"],axis=1,inplace=True)
result = df

# 5- Beğenme (like) ve beğenmeme (dislike) sayılarının ortalamasını bulunuz.
result = df[["likes","dislikes"]].mean()

# 6- ilk 50 videonun like ve dislike kolonlarını getiriniz.
result = df[["title","likes","dislikes"]].head(50)

# 7- En çok görüntülenen video hangisidir ?
result = df[df["views"].max() == df["views"]]["title"].iloc[0]

# 8- En düşük görüntülenen video hangisidir?
result = df[df["views"].min() == df["views"]]["title"].iloc[0]

# 9- En fazla görüntülenen ilk 10 video hangisidir ?
result = df.sort_values("views", ascending=False).head(10)[["title","views"]]

# 10- Kategoriye göre beğeni ortalamalarını sıralı şekilde getiriniz.
result = df.groupby("category_id").mean().sort_values("likes")["likes"]

# 11- Kategoriye göre yorum sayılarını yukarıdan aşağıya sıralayınız.
result = df.groupby("category_id").sum().sort_values("comment_count", ascending = False)["comment_count"]

# 12- Her kategoride kaç video vardır ?
result = df["category_id"].value_counts()

# 13- Her videonun title uzunluğu bilgisini yeni bir kolonda gösteriniz.
df["title_len"] = df["title"].apply(len)

# 14- Her video için kullanılan tag sayısını yeni kolonda gösteriniz.
# df["tag_count"] = df["tags"].apply(lambda x: len(x.split('|')))

def tagCount(tag):
    return len(tag.split('|'))

df["tag_count"] = df["tags"].apply(tagCount)


# 15- En popüler videoları listeleyiniz.(like/dislike oranına göre)

def calculate_like_dislike_rate(dataset):
    likesList = list(dataset["likes"])
    dislikesList = list(dataset["dislikes"])

    liste = list(zip(likesList,dislikesList))

    oranListesi = []

    for like,dislike  in liste: 
        if (like + dislike) == 0:
            oranListesi.append(0)
        else:
            oranListesi.append(like/(like+dislike))

    return oranListesi

df["like_range"] = calculate_like_dislike_rate(df)

print(df.sort_values("like_range",ascending=False)[["title","likes","dislikes","like_range"]])