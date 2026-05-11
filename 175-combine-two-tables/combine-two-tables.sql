select firstName, lastName ,city, state from Person as a 
left join Address as b on a.personID=b.personID
