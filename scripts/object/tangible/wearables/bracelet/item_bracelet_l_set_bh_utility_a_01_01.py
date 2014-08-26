import sys

def setup(core, object):
	object.setStfFilename('static_item_n')
	object.setStfName('item_bracelet_l_set_bh_utility_a_01_01')
	object.setDetailFilename('static_item_d')
	object.setDetailName('item_bracelet_l_set_bh_utility_a_01_01')
	object.setStringAttribute('class_required', 'Bounty Hunter')
	object.setIntAttribute('required_combat_level', 85)
	object.setIntAttribute('cat_stat_mod_bonus.@stat_n:precision_modified', 50)
	object.setIntAttribute('cat_stat_mod_bonus.@stat_n:luck_modified', 30)
	object.setStringAttribute('@set_bonus:piece_bonus_count_3', '@set_bonus:set_bonus_bh_utility_a_1')
	object.setStringAttribute('@set_bonus:piece_bonus_count_4', '@set_bonus:set_bonus_bh_utility_a_2')
	object.setStringAttribute('@set_bonus:piece_bonus_count_5', '@set_bonus:set_bonus_bh_utility_a_3')
	object.setAttachment('setBonus', 'set_bonus_bh_utility_a')
	return