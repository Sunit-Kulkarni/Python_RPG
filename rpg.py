# The hero is going to fight a goblin
# Our program will collect the hero's name.
# The hero will then have options of:
# 1. Attacking.
# 2. Stand there.
# 3. Run Away.

hero_health = 10;
hero_power = 6;
goblin_health = 8;
goblin_power = 4;

hero_name = raw_input("What is your name, brave adventurer?");

print "%s, have encountered a terrifying goblin" % hero_name;
while (hero_health > 0 and goblin_health > 0):
	print "%s have %d health and %d power." % (hero_name, hero_health, hero_power);
	print "The goblin has %d health and %d power." % (goblin_health, goblin_power)
	print "What action will you take?";
	print "1. Attack the goblin";
	print "2. Stand there. And get hit.";
	print "3. Run like a coward!";
	print "> ";

	user_input = raw_input();
	if user_input == "1":
		print "%s makes a daring attack!" % hero_name;
		goblin_health -= 1;
	elif user_input == "2":
		print "%s stands like a fool looking for an early grave." % hero_name
	elif user_input == "3":
		print "%s has run away like a fledging coward. At least you will live to fight another day!" % hero_name
		break;
	else:
		print "Invalid input %s" % user_input

	#goblin_health = 0;