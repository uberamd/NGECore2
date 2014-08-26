import sys

def addAbilities(core, actor, player):
	if actor.getLevel() >= 10:
		actor.addAbility("me_enhance_precision_1")
	if actor.getLevel() >= 34:
		actor.addAbility("me_enhance_precision_2")
	if actor.getLevel() >= 62:
		actor.addAbility("me_enhance_precision_3")
	return

def removeAbilities(core, actor, player):
	actor.removeAbility("me_enhance_precision_1")
	actor.removeAbility("me_enhance_precision_2")
	actor.removeAbility("me_enhance_precision_3")
	return
