import sys

def addAbilities(core, actor, player):
	if actor.getLevel() >= 26:
		actor.addAbility("of_focus_fire_1")
	if actor.getLevel() >= 34:
		actor.addAbility("of_focus_fire_2")
	if actor.getLevel() >= 48:
		actor.addAbility("of_focus_fire_3")
	if actor.getLevel() >= 62:
		actor.addAbility("of_focus_fire_4")
	if actor.getLevel() >= 76:
		actor.addAbility("of_focus_fire_5")
	if actor.getLevel() >= 90:
		actor.addAbility("of_focus_fire_6")
	return

def removeAbilities(core, actor, player):
	actor.removeAbility("of_focus_fire_1")
	actor.removeAbility("of_focus_fire_2")
	actor.removeAbility("of_focus_fire_3")
	actor.removeAbility("of_focus_fire_4")
	actor.removeAbility("of_focus_fire_5")
	actor.removeAbility("of_focus_fire_6")
	return
