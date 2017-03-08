-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

DROP DATABASE tournament;
CREATE DATABASE tournament;
\c tournament;

CREATE TABLE player  (
  id SERIAL PRIMARY KEY,
  name TEXT
);

CREATE TABLE match (
  id SERIAL PRIMARY KEY,
  winner INTEGER REFERENCES player(id) ON DELETE SET NULL,
  loser INTEGER REFERENCES player(id) ON DELETE SET NULL
);

-- Returns a list of all the players with the number of wins
-- and losses respectively.
CREATE VIEW player_record AS
select player.id,
       coalesce(wins.total, 0) as wins,
       coalesce(losses.total, 0) as losses
    from player left join (
      select winner, count(*) as total
      from match
      group by winner
    ) as wins on player.id = wins.winner
     left join (
      select loser, count(*) as total
      from match
      group by loser
    ) as losses on player.id = losses.loser;

-- Returns a list of all the players with the number of wins
-- and total matches they've played sorted by number of wins.
CREATE VIEW standings AS
  select player.id,
         player.name,
         player_record.wins,
         player_record.wins + player_record.losses as matches
    from player, player_record
    where player.id = player_record.id
    order by player_record.wins desc;
