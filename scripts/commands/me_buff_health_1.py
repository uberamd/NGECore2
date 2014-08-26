import sys

def setup(core, actor, buff):
	return
	
def run(core, actor, target, commandString):

	group = core.objectService.getObject(actor.getGroupId())
	
	if target and target.getSlottedObject("ghost"):
		if group and target in group.getMemberList():
			core.buffService.addGroupBuff(target, 'me_buff_health_0', actor)
		else:
			core.buffService.addBuffToCreature(target, 'me_buff_health_0', actor)
	else:
		core.buffService.addGroupBuff(actor, 'me_buff_health_0', actor)
		
	return
	