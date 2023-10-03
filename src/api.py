import pandas as pd

# Importamos los DF de los CSV
data_games = pd.read_csv("db/data_games.csv")
data_games_wr = pd.read_csv("db/data_games_wr.csv")
data_players = pd.read_csv("db/data_players.csv")
data_reviews = pd.read_csv("db/data_reviews.csv")
item_similarity_df = pd.read_csv("db/item_similarity_df.csv")

def PlayTimeGenre(genre: str):
    if genre in data_games.columns:
        games_genre = data_games.loc[(data_games[genre]==1)]
        games_genre_year = games_genre.groupby(by=['year']).sum()
        year = games_genre_year[games_genre_year['playtime_forever'] == games_genre_year['playtime_forever'].max()].index[0]
        return year
    else:
        return 0
    
def UserForGenre(genre: str):
    if genre in data_games.columns:
        players_genre = data_players.loc[(data_players[genre]==1)]
        players_genre_group = players_genre.groupby(by=['user_id']).sum()
        max_player = players_genre_group[players_genre_group['playtime_forever'] == players_genre_group['playtime_forever'].max()].index[0]
        max_player_genre_items = data_players.loc[(data_players[genre]==1) & (data_players['user_id']==max_player)]
        max_player_genre_group = max_player_genre_items.groupby(by=['year']).sum()
        max_player_genre_group = max_player_genre_group[(max_player_genre_group['playtime_forever'] != 0)]
        playtime_max_player_genre = max_player_genre_group['playtime_forever'].to_dict()
        response = {"Usuario con más horas jugadas para Género " + genre : max_player, "Horas jugadas":[playtime_max_player_genre]}
        return response
    else:
        return 0

def UsersRecommend(year: int):
    if year in data_games_wr['year'].values:
        data_games_wr_year = data_games_wr[data_games_wr['year'] == year]
        data_games_wr_year = data_games_wr_year.sort_values('recommend',ascending=False)
        recommended_games_list = data_games_wr_year['title'].head(3).tolist()
        response = [{"Puesto 1" : recommended_games_list[0]}, {"Puesto 2" : recommended_games_list[1]},{"Puesto 3" : recommended_games_list[2]}]
        return response
    else:
        return 0

def UsersNotRecommend(year: int):
    if year in data_games_wr['year'].values:
        data_games_wr_year = data_games_wr[data_games_wr['year'] == year]
        data_games_wr_year = data_games_wr_year.sort_values('recommend',ascending=True)
        not_recommended_games_list = data_games_wr_year['title'].head(3).tolist()
        response = [{"Puesto 1" : not_recommended_games_list[0]}, {"Puesto 2" : not_recommended_games_list[1]},{"Puesto 3" : not_recommended_games_list[2]}]
        return response
    else:
        return 0

def sentiment_analysis(year: int):
    if year in data_reviews['year'].values:
        if 0 in data_reviews['sentiment_analysis'].unique():
            neg = data_reviews['sentiment_analysis'].value_counts()[0]
        else:
            neg = 0
        if 1 in data_reviews['sentiment_analysis'].unique():
            neutr = data_reviews['sentiment_analysis'].value_counts()[1]
        else:
            neutr = 0
        if 2 in data_reviews['sentiment_analysis'].unique():
            pos = data_reviews['sentiment_analysis'].value_counts()[2]
        else:
            pos = 0
        response = {"Negative = " + str(neg), "Neutral = " + str(neutr), "Positive = " + str(pos)}
        return response
    else:
        return 0
    
def recomendacion_juego(id: int):
    if id in data_games_wr['id'].values:
        top_value = 5
        similar_items = item_similarity_df[id]
        similar_items = similar_items.sort_values(ascending=False)
        response = similar_items.drop(id).head(top_value).index.to_list()
        return response
    else:
        return 0