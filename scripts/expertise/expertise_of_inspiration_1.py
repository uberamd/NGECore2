import sys

def addAbilities(core, actor, player):
	if actor.getLevel() >= 26:
		actor.addAbility("of_inspiration_1")
	if actor.getLevel() >= 34:
		actor.addAbility("of_inspiration_2")
	if actor.getLevel() >= 48:
		actor.addAbility("of_inspiration_3")
	if actor.getLevel() >= 62:
		actor.addAbility("of_inspiration_4")
	if actor.getLevel() >= 76:
		actor.addAbility("of_inspiration_5")
	if actor.getLevel() >= 90:
		actor.addAbility("of_inspiration_6")
	return

def removeAbilities(core, actor, player):
	actor.removeAbility("of_inspiration_1")
	actor.removeAbility("of_inspiration_2")
	actor.removeAbility("of_inspiration_3")
	actor.removeAbility("of_inspiration_4")
	actor.removeAbility("of_inspiration_5")
	actor.removeAbility("of_inspiration_6")
	return
