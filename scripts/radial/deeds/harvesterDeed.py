from resources.common import RadialOptions
import sys

def createRadial(core, owner, target, radials):
	radials.clear()
	radials.add(RadialOptions(0, 21, 3, 'Use Deed'))
	#radials.add(RadialOptions(0, 7, 1, '111111'))
	#radials.add(RadialOptions(0, 15, 1, ''))
	#radials.add(RadialOptions(0, 61, 1, ''))
	return
	
def handleSelection(core, owner, target, option):
	if option == 21 and target:
		core.objectService.useObject(owner, target)
		core.harvesterService.enterStructurePlacementMode(owner, target)
	if option == 61 and target:
		object5 = core.harvesterService.constructionSite(owner, target)
	if option == 15 and target:
		core.objectService.destroyObject(target)
	return
	