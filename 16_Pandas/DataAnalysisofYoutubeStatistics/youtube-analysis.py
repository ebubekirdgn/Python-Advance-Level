from numpy import fabs
import pandas as pd
from pandas.core import groupby

df = pd.read_csv("youtube-ing.csv")
result = df

# 1- İlk 10 kayıt
result = df.head(10)

# 2- İkinci 5 kayıt
result = df[5:].head()

# 3- Dataset' de bulunan kolon isimleri ve sayısı
#result = df.count() 1. yontem
result = df.columns
result = len(df.columns)

# 4- Aşağıda bulunan bazı kolonları silin ve kalan kolonları listeleme
# (thumbnail_link,comments_disabled,ratings_disabled,video_error_or_removed,description)
df.drop(["thumbnail_link","comments_disabled","ratings_disabled","video_error_or_removed","description","trending_date"],axis=1,inplace=True)
result = df

# 5- Beğenme (like) ve beğenmeme (dislike) sayılarının ortalamasını bulma
result = df[["likes","dislikes"]].mean()

# 6- ilk 50 videonun like ve dislike kolonlarını getirme
result = df[["title","likes","dislikes"]].head(50)

# 7- En çok görüntülenen video
result = df[df["views"].max() == df["views"]]["title"].iloc[0]

# 8- En düşük görüntülenen video
result = df[df["views"].min() == df["views"]]["title"].iloc[0]

# 9- En fazla görüntülenen ilk 10 video
result = df.sort_values("views", ascending=False).head(10)[["title","views"]]

# 10- Kategoriye göre beğeni ortalamalarını sıralı şekilde getirme
result = df.groupby("category_id").mean().sort_values("likes")["likes"]

# 11- Kategoriye göre yorum sayılarını yukarıdan aşağıya sıralama
result = df.groupby("category_id").sum().sort_values("comment_count", ascending = False)["comment_count"]

# 12- Her kategoride kaç video var?
result = df["category_id"].value_counts()

# 13- Her videonun title uzunluğu bilgisini yeni bir kolonda gösterme
df["title_len"] = df["title"].apply(len)

# 14- Her video için kullanılan tag sayısını yeni kolonda gösterme
# df["tag_count"] = df["tags"].apply(lambda x: len(x.split('|')))

def tagCount(tag):
    return len(tag.split('|'))

df["tag_count"] = df["tags"].apply(tagCount)

# 15- En popüler videoları listeleyiniz.(like/dislike oranına göre)
def calculate_like_dislike_rate(dataset):
    likesList = list(dataset["likes"])
    dislikesList = list(dataset["dislikes"])

    list_of = list(zip(likesList,dislikesList))

    rangeList = []

    for like,dislike  in list_of: 
        if (like + dislike) == 0:
            rangeList.append(0)
        else:
            rangeList.append(like/(like+dislike))

    return rangeList

df["like_range"] = calculate_like_dislike_rate(df)

print(df.sort_values("like_range",ascending=False)[["title","likes","dislikes","like_range"]])