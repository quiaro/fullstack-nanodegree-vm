-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

-- Create database tournament. The schema currently supports only one
-- tournament at a time.
DROP DATABASE tournament;
CREATE DATABASE tournament;
\c tournament;

CREATE TABLE Players  (
  id SERIAL PRIMARY KEY,
  name TEXT
);

CREATE TABLE Matches (
  id SERIAL PRIMARY KEY,
  winner INTEGER REFERENCES Players(id) ON DELETE SET NULL,
  loser INTEGER REFERENCES Players(id) ON DELETE SET NULL
);

-- Returns a list of all the players with the number of wins
-- and losses respectively.
CREATE VIEW V_Players_Records AS
select Players.id,
       coalesce(wins.total, 0) as wins,
       coalesce(losses.total, 0) as losses
    from Players left join (
      select winner, count(*) as total
      from Matches
      group by winner
    ) as wins on Players.id = wins.winner
     left join (
      select loser, count(*) as total
      from Matches
      group by loser
    ) as losses on Players.id = losses.loser;

-- Returns a list of all the players with the number of wins
-- and total matches they've played sorted by number of wins.
CREATE VIEW V_Standings AS
  select Players.id,
         Players.name,
         V_Players_Records.wins,
         V_Players_Records.wins + V_Players_Records.losses as matches
    from Players, V_Players_Records
    where Players.id = V_Players_Records.id
    order by V_Players_Records.wins desc;
