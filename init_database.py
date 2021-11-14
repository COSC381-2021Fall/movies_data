import csv, sqlite3

con = sqlite3.connect("movies.db")
cur = con.cursor()
cur.execute('''CREATE TABLE movies (
        adult, belongs_to_collection, budget, genres, homepage, id, imdb_id, original_language, original_title, 
        overview, popularity, poster_path, production_companies, production_countries, release_date, revenue,
        runtime, spoken_languages, status, tagline, title, video, vote_average, vote_count
    )''')

with open('movies.csv','r') as fin: 
    dr = csv.DictReader(fin)
    to_db = [
        (i['adult'], i['belongs_to_collection'], i['budget'], i['genres'], 
        i['homepage'], i['id'], i['imdb_id'], i['original_language'], i['original_title'], 
        i['overview'], i['popularity'], i['poster_path'], i['production_companies'], 
        i['production_countries'], i['release_date'], i['revenue'],
        i['runtime'], i['spoken_languages'], i['status'], i['tagline'], i['title'], 
        i['video'], i['vote_average'], i['vote_count']) for i in dr ]
    
cur.executemany('''INSERT INTO movies (
        adult, belongs_to_collection, budget, genres, homepage, id, imdb_id, original_language, original_title, 
        overview, popularity, poster_path, production_companies, production_countries, release_date, revenue,
        runtime, spoken_languages, status, tagline, title, video, vote_average, vote_count
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, 
        ?, ?, ?, ?, ?, ?, ?,
        ?, ?, ?, ?, ?, ?, ?, ?)''', to_db)
con.commit()
con.close()