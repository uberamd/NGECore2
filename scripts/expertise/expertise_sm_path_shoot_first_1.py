import sys

def addAbilities(core, actor, player):
	if actor.getLevel() >= 34:
		actor.addAbility("sm_shoot_first_1")
	if actor.getLevel() >= 46:
		actor.addAbility("sm_shoot_first_2")
	if actor.getLevel() >= 62:
		actor.addAbility("sm_shoot_first_3")
	if actor.getLevel() >= 74:
		actor.addAbility("sm_shoot_first_4")
	if actor.getLevel() >= 90:
		actor.addAbility("sm_shoot_first_5")
	return

def removeAbilities(core, actor, player):
	actor.removeAbility("sm_shoot_first_1")
	actor.removeAbility("sm_shoot_first_2")
	actor.removeAbility("sm_shoot_first_3")
	actor.removeAbility("sm_shoot_first_4")
	actor.removeAbility("sm_shoot_first_5")
	return
