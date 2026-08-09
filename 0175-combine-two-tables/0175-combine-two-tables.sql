-- select firstName, lastName ,city, state from Person as a 
-- left join Address as b on a.personID=b.personID;


select firstName, lastName, city, state
from Person as p
left join Address as a
on p.personId = a.personId;

