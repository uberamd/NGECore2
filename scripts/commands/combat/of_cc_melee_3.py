import sys

def setup(core, actor, target, command):
	core.buffService.addBuffToCreature(target, 'of_cc_melee_3', actor)
	return
	
def preRun(core, actor, target, command):
	return

def run(core, actor, target, commandString):
	return