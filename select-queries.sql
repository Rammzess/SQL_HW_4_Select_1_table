 /*Извлечение по году 1986 (выбрано взамен 2018)*/
SELECT AlbumName, ReleaseYear FROM Album
                    WHERE ReleaseYear = 1986;

/*название и продолжительность самого длительного трека*/
SELECT TrackName, TrackDuration FROM Tracks
                    WHERE TrackDuration = (
                    SELECT MAX(TrackDuration)
                    FROM Tracks);

/*название треков, продолжительность которых не менее 3,5 минуты;*/
SELECT TrackName, TrackDuration FROM Tracks
                    WHERE NOT TrackDuration < 3.5;

/*названия сборников, вышедших в период 
с 1988 по 1997 год включительно (взамен 2018 - 2020)*/
SELECT SetName, ReleaseYear FROM MusSets
                    WHERE ReleaseYear BETWEEN 1988 AND 1997;

/*исполнители, чье имя состоит из 1 слова;*/
SELECT id, MusName FROM Musician
                    WHERE MusName NOT LIKE '%% %%';

/*название треков, которые содержат слово "you" или "Ты" (взамен "my"/"My");*/
SELECT id, TrackName FROM Tracks
                    WHERE TrackName ILIKE '%%You%%' OR '%%Ты%%';

