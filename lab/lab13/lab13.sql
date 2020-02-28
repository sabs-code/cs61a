.read su19data.sql

CREATE TABLE obedience AS
  SELECT seven, instructor FROM students;

CREATE TABLE smallest_int AS
  SELECT time, smallest FROM students where smallest>2 order by smallest LIMIT 20;

CREATE TABLE matchmaker AS
  SELECT a.pet, a.song, a.color, b.color from students AS a, students AS b
          where a.pet = b.pet and a.song = b.song and a.time<b.time;

CREATE TABLE smallest_int_having AS
  SELECT time, smallest from students group by smallest having count(*)=1;
