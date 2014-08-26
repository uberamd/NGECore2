import sys

def setup(core, actor, buff):
	return

def add(core, actor, buff):
	core.skillModService.addSkillMod(actor, 'stealth_divisor', 35)
	core.skillModService.addSkillMod(actor, 'expertise_damage_line_vulnerability_of_buff_def', 7)
	core.skillModService.addSkillMod(actor, 'expertise_damage_line_vulnerability_of_dm', 7)
	return
	
def remove(core, actor, buff):
	core.skillModService.deductSkillMod(actor, 'stealth_divisor', 35)
	core.skillModService.deductSkillMod(actor, 'expertise_damage_line_vulnerability_of_buff_def', 7)
	core.skillModService.deductSkillMod(actor, 'expertise_damage_line_vulnerability_of_dm', 7)
	return
	