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

has_potion = False;
has_magic_sword = False;

def shop():
	print "This is the shop function";
	still_shopping = True;
	global has_potion;
	global has_magic_sword;
	while still_shopping:
		print "You have entered the shop.";
		print " What do you want to buy";
		print "1. Health Potion"
		print "2. Magic Sword"
		print "3 Leave the shop"
		print "4. Flex your muscles"
		print "> "
		user_input = raw_input();
		if user_input == "1":
			has_potion = True;
		elif user_input == "2":
			has_magic_sword = True;
		elif user_input == "3":
			still_shopping = False;
		elif user_input == "4":
			print "The shopkeeper is disgusted by your arrogance and throws you out";
			still_shopping = False;
		else:
			print "The shopkeeper gruntles at your nonsense"

hero_name = raw_input("What is your name, brave adventurer?");

shop();

print "%s, have encountered a terrifying goblin" % hero_name;
while (hero_health > 0 and goblin_health > 0):
	print "%s have %d health and %d power." % (hero_name, hero_health, hero_power);
	print "The goblin has %d health and %d power." % (goblin_health, goblin_power)
	print "What action will you take?";
	print "1. Attack the goblin";
	print "2. Stand there. And get hit.";
	print "3. Run like a coward!";
	if (has_potion):
		print "4. Use Potion";
	print "> ";

	user_input = raw_input();
	if user_input == "1":
		print "%s makes a daring attack!" % hero_name;

		if has_magic_sword:
			print "The goblin takes %d damage! and another 5 from the magic sword" % hero_power;
		else:
			print "The goblin takes %d damage!" % hero_power;
		if has_magic_sword:
			goblin_health -= hero_power + 5;
		else:
			goblin_health -= hero_power;
	elif user_input == "2":
		print "%s stands like a fool looking for an early grave." % hero_name
	elif user_input == "3":
		print "%s has run away like a fledging coward. At least you will live to fight another day!" % hero_name
		break;
	elif user_input == "4" and has_potion:
		print "You use the health potion and gain 20 health";
		hero_health += 20;
	else:
		print "Invalid input %s" % user_input

	#Its the goblins turn assuming he is still alive
	if goblin_health > 0:
		print "The goblin snarls and lashes out at %s" % hero_name
		print "The goblin does %d damage" % goblin_power;
		hero_health -= goblin_power;
	if hero_health <= 0:
		print "You have been defeated by the pathetic goblin."
	elif goblin_health <= 0:
		print "You have conquered the golbin!"

	#goblin_health = 0;