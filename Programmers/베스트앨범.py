def solution(genres, plays):
    genres_total_plays = dict()
    answer = []
    # 장르별로 속한 노래 총합 수 구하기
    for idx, genre in enumerate(genres):
        try:
            genres_total_plays[genre] += plays[idx]
        except:
            genres_total_plays[genre] = plays[idx]
    
    # 가장 많은 곡이 속한 장르 구하기
    many_plays_genres = sorted(list(genres_total_plays.items()), key = lambda x : x[1], reverse = True)
    
    
    while many_plays_genres:
        many_plays_genre = many_plays_genres[0][0]
        temp_genre_plays = []
        
        # 장르 별 play 수 추출하기
        for idx, genre in enumerate(genres):
            if genre == many_plays_genre:
                temp_genre_plays.append([idx, plays[idx]])
        
        # 정렬 및 장르별 2개 까지 제한
        temp_genre_plays = sorted(temp_genre_plays, key = lambda x : x[1], reverse = True)[:2]
        
        
        for genre_index in temp_genre_plays:
            answer.append(genre_index[0])
            
        many_plays_genres.pop(0)

    return answer
