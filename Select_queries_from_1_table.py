import sqlalchemy
import os
import pandas as pd
from dotenv import load_dotenv



class DB_operator:
    def insertdata(connect):
        con.execute(f"""
                INSERT INTO {tab_names[0]}
                    (ID, MusName) VALUES
                    (1, 'Jimmy Hedrix'),
                    (2, 'Led Zeppelin'),
                    (3, 'Metallica'),
                    (4, 'Blur'),
                    (5, 'Pink Floyd'),
                    (6, 'Sex Pistols'),
                    (7, 'Iron Maiden'),
                    (8, 'Black Sabbath');
                    """)
        con.execute(f"""
                INSERT INTO {tab_names[1]}
                    (ID, GenreName) VALUES
                    (1, 'Trash Metal'),
                    (2, 'Indie Rock'),
                    (3, 'Psychedelic Rock'),
                    (4, 'Hard Rock'),
                    (5, 'Heavy Metal'),
                    (6, 'Punk Rock'),
                    (7, 'Blues');
                    """)
        con.execute(f"""
                INSERT INTO {tab_names[2]}
                    (ID, MusicianID, GenreID) VALUES
                    (1, 1, 3),
                    (2, 1, 7),
                    (3, 2, 4),
                    (4, 3, 1),
                    (5, 4, 2),
                    (6, 5, 3),
                    (7, 5, 7),
                    (8, 6, 6),
                    (9, 7, 5),
                    (10, 8, 5),
                    (11, 8, 7);
                    """)
        con.execute(f"""
                INSERT INTO {tab_names[3]}
                    (ID, AlbumName, ReleaseYear) VALUES
                    (1, 'The Dark Side of the Moon', 1973),
                    (2, 'Master of Puppets', 1986),
                    (3, 'Wish You Were Here', 1975),
                    (4, 'Never Mind the Bollocks', 1977), /*Sex Pistols */
                    (5, 'Parklife', 1994), /*Blur */
                    (6, 'Seventh Star', 1986), /*Black sabbath */
                    (7, 'Are You Experienced', 1967), /*Hendrix */
                    (8, 'The Number of The Beast', 1982), /*Iron Maiden */
                    (9, 'Led Zeppelin 3', 1970), /*Led Zeppelin */
                    (10, 'Led Zeppelin 4', 1971), /*Led Zeppelin */
                    (11, 'Blur', 1997);
                    """)
        con.execute(f"""
                INSERT INTO {tab_names[4]}
                    (ID, MusicianID, AlbumID) VALUES
                    (1, 1, 7),
                    (2, 2, 9),
                    (3, 2, 10),
                    (4, 3, 2),
                    (5, 4, 5),
                    (6, 4, 11),
                    (7, 5, 1),
                    (8, 5, 3),
                    (9, 6, 4),
                    (10, 7, 8),
                    (11, 8, 6);
                    """)
        con.execute(f"""
                INSERT INTO {tab_names[5]}
                    (ID, TrackName, AlbumID, TrackDuration) VALUES
                    (1, 'Song 2', 11, 02.02),
                    (2, 'Stairway to Heaven', 10, 07.55),
                    (3, 'Hallowed Be Thy Name', 8, 07.08),
                    (4, 'Shine On You Crazy Diamond (Parts VI???IX)', 1, 12.28),
                    (5, 'Foxey Lady', 7, 03.10),
                    (6, 'Wish You Were Here', 3, 05.35),
                    (7, 'Seventh Star', 6, 05.20),
                    (8, 'Immigrant Song', 9, 02.26),
                    (9, 'Orion', 2, 08.36),
                    (10, 'Girls&Boys', 5, 04.50),
                    (11, 'Shine On You Crazy Diamond (Parts I???V)', 1, 13.32),
                    (12, '22 Acacia Avenue', 8, 06.34),
                    (13, 'Heart Like a Wheel', 6, 06.35),
                    (14, 'Anarchy in the UK', 4, 03.31),
                    (15, 'Welcome Home (Sanitarium)', 2, 06.27);
                    """)
        con.execute(f"""
                INSERT INTO {tab_names[6]}
                    (ID, SetName, ReleaseYear) VALUES
                    (1, 'Rolling Stone top 100 songs', 1997),
                    (2, 'Classics of Rock Music', 2005),
                    (3, 'Best of Blues-Rock', 1989),
                    (4, 'The Heaviest of Heavy', 2001),
                    (5, 'Top 100 tracks that Rocks', 1999),
                    (6, 'Best of Jimmy Hendrix', 1988),
                    (7, 'Top 20 Rock Ballads', 2012),
                    (8, 'Golden Age of Metal', 1997);
                    """)
        con.execute(f"""
                INSERT INTO {tab_names[7]}
                    (ID, TrackID, SetID) VALUES
                    (1, 1, 5),
                    (2, 2, 1),
                    (3, 2, 7),
                    (4, 3, 4),
                    (5, 3, 8),
                    (6, 4, 2),
                    (7, 5, 6),
                    (8, 6, 1),
                    (9, 6, 2),
                    (10, 6, 7),
                    (11, 7, 7),
                    (12, 7, 8),
                    (13, 8, 1),
                    (14, 8, 3),
                    (15, 9, 5),
                    (16, 9, 8),
                    (17, 10, 5),
                    (18, 11, 2),
                    (19, 12, 4),
                    (20, 12, 5),
                    (21, 13, 3),
                    (22, 13, 7),
                    (23, 14, 1),
                    (24, 15, 2),
                    (25, 15, 7),
                    (26, 15, 8);
                    """)

    def selector(connect):
        # ???????????????????? ???? ???????? 1986 (?????????????? ???????????? 2018)
        con.execute("""
                SELECT AlbumName, ReleaseYear FROM Album
                    WHERE ReleaseYear = 1986;
                    """).fetchall()
        # ???????????????? ?? ?????????????????????????????????? ???????????? ?????????????????????? ??????????;
        con.execute("""
                SELECT TrackName, TrackDuration FROM Tracks
                    WHERE TrackDuration = (
                        SELECT MAX(TrackDuration)
                        FROM Tracks);
                    """)
        # ???????????????? ????????????, ?????????????????????????????????? ?????????????? ???? ?????????? 3,5 ????????????;
        con.execute(f"""
                SELECT TrackName, TrackDuration FROM Tracks
                    WHERE NOT TrackDuration < 3.5;
                     """).fetchall()
        # ???????????????? ??????????????????, ???????????????? ?? ???????????? 
        # ?? 1988 ???? 1997 ?????? ???????????????????????? (???????????? 2018 - 2020)
        con.execute(f"""
                SELECT SetName, ReleaseYear FROM MusSets
                    WHERE ReleaseYear BETWEEN 1988 AND 1997;
                     """).fetchall()
        # ??????????????????????, ?????? ?????? ?????????????? ???? 1 ??????????;
        con.execute(f"""
                SELECT id, MusName FROM Musician
                    WHERE MusName NOT LIKE '%% %%';
                     """).fetchall()
        # ???????????????? ????????????, ?????????????? ???????????????? ?????????? "you" (???????????? "my"/"My");
        con.execute(f"""
                SELECT id, TrackName FROM Tracks
                    WHERE TrackName ILIKE '%%You%%';
                     """).fetchall()


if __name__ == '__main__':
    dotenv_path = os.path.join(os.path.dirname(__file__), 'config.env')
    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path)
    password = os.getenv('DB_PASS')
    engine = sqlalchemy.create_engine('postgresql://ramses:'
                                      + f'{password}'
                                      + '@localhost:5432/mus_shop_v2')
    con = engine.connect()
    tab_names = (['Musician', 'Genre', 'MusicianGenre', 'Album',
                  'MusicianAlbum', 'Tracks', 'MusSets', 'TrackMusSets'])
    DB_operator.insertdata(con) # ???????????????????? ????????????
    DB_operator.selector(con) # select ??????????????