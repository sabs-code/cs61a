.read lab13.sql

CREATE TABLE su19favpets AS
  SELECT pet, count(*) from students group by pet order by count(*) DESC LIMIT 10;


CREATE TABLE su19dog AS
  SELECT pet, count(*) from students group by pet having pet='dog';


CREATE TABLE obedienceimages AS
  SELECT seven, instructor, count(*) from students where seven='7' group by instructor;
