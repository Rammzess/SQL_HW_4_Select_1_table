/*количество исполнителей в каждом жанре;*/
SELECT Genre.GenreName, COUNT(MusicianGenre.MusicianID)
FROM Genre
LEFT JOIN MusicianGenre ON MusicianGenre.GenreID = Genre.ID
GROUP BY GenreName
	
/*количество треков, вошедших в альбомы 2019-2020 годов
Взамен указал года 1977, 1975, 1971;*/
SELECT Album.ReleaseYear, count(Tracks) FROM Tracks
JOIN Album on Tracks.AlbumID = Album.ID
	WHERE Album.ReleaseYear IN (1971, 1975, 1977) 
	GROUP BY ReleaseYear;

/*средняя продолжительность треков по каждому альбому;*/
SELECT Album.AlbumName, AVG(TrackDuration) FROM Tracks
JOIN Album ON Tracks.AlbumID = Album.ID 
	GROUP BY AlbumName;

/*все исполнители, которые не выпустили альбомы в 2020 году;
Взамен указал тех, кто не выпускал альбомы в 70х годах*/
SELECT Musician.MusName, Album.ReleaseYear FROM Musician
JOIN MusicianAlbum ON Musician.ID = MusicianAlbum.MusicianID
JOIN Album ON MusicianAlbum.AlbumID = Album.ID
	WHERE Album.ReleaseYear NOT BETWEEN 1970 AND 1979
	GROUP BY Musician.MusName, Album.ReleaseYear;

/*названия сборников, в которых присутствует конкретный исполнитель (выберите сами);*/
SELECT MusSets.Setname FROM MusSets
JOIN TrackMusSets ON MusSets.ID = TrackMusSets.SetID
JOIN Tracks ON TrackMusSets.TrackID = Tracks.ID
JOIN Album ON Tracks.AlbumID = Album.ID
JOIN MusicianAlbum ON Album.ID = MusicianAlbum.AlbumID
JOIN Musician ON MusicianAlbum.MusicianID = Musician.ID
	WHERE Musician.MusName ILIKE '%%Metallica%%'
	GROUP BY MusSets.Setname;

/*название альбомов, в которых присутствуют исполнители более 1 жанра;*/
SELECT Album.AlbumName FROM Album
JOIN MusicianAlbum ON Album.ID = MusicianAlbum.AlbumID
JOIN Musician ON MusicianAlbum.MusicianID = Musician.ID
JOIN MusicianGenre ON Musician.ID = MusicianGenre.MusicianID
	GROUP BY Album.AlbumName
	HAVING COUNT(MusicianGenre.MusicianID) > 1;

/*наименование треков, которые не входят в сборники;*/
SELECT Tracks.TrackName FROM Tracks
LEFT JOIN TrackMusSets TMS ON Tracks.ID = TMS.TrackID
	WHERE Tracks.ID NOT IN(SELECT TrackID FROM TrackMusSets)
	GROUP BY Tracks.TrackName, Tracks.ID;

/*исполнителя(-ей), написавшего самый короткий по продолжительности трек
(теоретически таких треков может быть несколько);*/
SELECT Musician.MusName, Tracks.TrackDuration FROM Musician
JOIN MusicianAlbum MA ON Musician.ID = MA.MusicianID
JOIN Album ON MA.AlbumID = Album.ID
JOIN Tracks ON Album.ID = Tracks.AlbumID
	GROUP BY Musician.MusName, Tracks.TrackDuration
	ORDER BY Tracks.TrackDuration ASC
	LIMIT 2;

/*название альбомов, содержащих наименьшее количество треков.*/
SELECT Album.AlbumName,  COUNT(Tracks.AlbumID) FROM Album
JOIN Tracks ON Album.ID = Tracks.AlbumID
	GROUP BY Album.AlbumName, Tracks.AlbumID
	ORDER BY COUNT(Tracks.AlbumID) ASC
	LIMIT 5;
	
/* На форумах писали, что такая конструкция должна работать, но у меня не сработала
having COUNT(Tracks.AlbumID) = (select MIN(COUNT(Tracks.AlbumID)) 
from Tracks group by Tracks.AlbumID); */

