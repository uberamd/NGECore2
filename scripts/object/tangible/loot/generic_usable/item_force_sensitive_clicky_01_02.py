import sys

def setup(core, object):
	object.setAttachment('radial_filename', 'object/usable')
	object.setStfFilename('static_item_n')
	object.setStfName('item_force_sensitive_clicky_01_02')
	object.setDetailFilename('static_item_d')
	object.setDetailName('item_force_sensitive_clicky_01_02')
	object.setIntAttribute('no_trade', 1)
	object.setStringAttribute('class_required', 'Jedi')
	return

def use(core, actor, object):
	core.buffService.addBuffToCreature(actor, 'roadmapFsClicky', actor)
	return
