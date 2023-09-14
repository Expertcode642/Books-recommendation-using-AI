indices = pd.Series(data.index, 
                    index=data['book_title']).drop_duplicates()
def book_recommendation(title, similarity = similarity):
    index = indices[title]
    similarity_scores = list(enumerate(similarity[index]))
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)
    similarity_scores = similarity_scores[0:5]
    bookindices = [i[0] for i in similarity_scores]
    return data['book_title'].iloc[bookindices]

print(book_recommendation("Letters to a Secret Lover"))
