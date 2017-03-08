#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2
import psycopg2.extras


def setup_tear_db(f):
    """Decorator responsible for creating and closing a connection to the DB

    Opens the connection to the DB and provides a function with a
    reference to the cursor and the DB. After the function is called,
    closes the DB connection and returns the function's return value."""
    def db_operation(*args):
        db = connect()
        c = db.cursor(cursor_factory=psycopg2.extras.DictCursor)
        res = f(*args, cursor=c, db=db)
        db.close()
        return res
    return db_operation


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


@setup_tear_db
def deleteMatches(**kw):
    """Remove all the match records from the database."""
    kw['cursor'].execute('delete from Matches')
    kw['db'].commit()


@setup_tear_db
def deletePlayers(**kw):
    """Remove all the player records from the database."""
    kw['cursor'].execute('delete from Players')
    kw['db'].commit()


@setup_tear_db
def countPlayers(**kw):
    """Returns the number of players currently registered."""
    kw['cursor'].execute('select count(*) as num_players from Players')
    row = kw['cursor'].fetchone()
    return int(row['num_players'])


@setup_tear_db
def registerPlayer(name, **kw):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
    kw['cursor'].execute('insert into Players (name) values (%s)', (name,))
    kw['db'].commit()


@setup_tear_db
def playerStandings(**kw):
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    kw['cursor'].execute('select * from Standings')
    return kw['cursor'].fetchall()


@setup_tear_db
def reportMatch(winner, loser, **kw):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    kw['cursor'].execute(
        'insert into Matches (winner, loser) values (%s, %s)', (winner, loser))
    kw['db'].commit()


@setup_tear_db
def swissPairings(**kw):
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    pairings = []
    cursor = kw['cursor']
    cursor.execute('select * from Standings')
    players = cursor.fetchmany(2)
    while players:
        (p1, p2) = players
        pairings.append((p1['id'], p1['name'], p2['id'], p2['name']))
        players = cursor.fetchmany(2)
    return pairings
