Tournament Results
=====================

Python module that uses a PostgreSQL database to keep track of players and matches in a Swiss system game tournament.

The module provides the following functions:
- registerPlayer(playerName)
- countPlayers()
- reportMatch(winnerId, loserId)
- playerStandings()
- swissPairings()
- deleteMatches()
- deletePlayers()

## Setup

This project requires Python v2.7 and PostgreSQL v.9.3.16. Alternatively, it can be set up in a virtual machine using [Vagrant](https://www.vagrantup.com) + [VirtualBox](https://www.virtualbox.org).

To run this project inside a virtual machine using Vagrant (assuming that you have [Vagrant](https://www.vagrantup.com/downloads.html) and [VirtualBox](https://www.virtualbox.org/wiki/Downloads) installed), you will need to:

1) Clone the repository
```
$ git clone https://github.com/quiaro/fullstack-nanodegree-vm.git
```

2) Go to the root directory where the Vagrant config file is located
```
$ cd fullstack-nanodegree-vm/vagrant
```

3) Start a virtual machine using Vagrant
```
$ vagrant up
```

4) Connect to the virtual machine
```
$ vagrant ssh
```

5) Navigate to the project's directory in your virtual machine that is shared with your local file system
```
$ cd /vagrant/tournament
```

6) Create the database that the Tournament Results module will be querying
```
$ psql -f tournament.sql
```

That's it! The Tournament Results module is now ready to be used.

## Verify

If you wish to make sure that the Tournament Results module is working you can run `tournament_test.py` to test it:
```
$ python tournament_test.py
```

---

## License

This project is licensed under the terms of the [**MIT**](https://opensource.org/licenses/MIT) license.
