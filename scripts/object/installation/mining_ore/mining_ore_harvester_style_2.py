import sys

def setup(core, object):
	object.setAttachment('radial_filename', 'structure/harvester')
	object.setHarvester_type(0)
	object.setPowerCost(60); 
	object.setMaintenanceCost(60);
	return