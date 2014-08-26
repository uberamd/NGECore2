import sys
from services.spawn import MobileTemplate
from services.spawn import WeaponTemplate
from resources.datatables import WeaponType
from resources.datatables import Difficulty
from resources.datatables import Options
from java.util import Vector


def addTemplate(core):
	mobileTemplate = MobileTemplate()
	
	mobileTemplate.setCreatureName('info_broker')
	mobileTemplate.setLevel(1)
	mobileTemplate.setDifficulty(Difficulty.NORMAL)
	mobileTemplate.setSocialGroup("township")
	mobileTemplate.setOptionsBitmask(Options.INVULNERABLE)
	
		
	templates = Vector()
	templates.add('object/mobile/shared_dressed_criminal_smuggler_human_female_01.iff')
	#templates.add('object/mobile/shared_dressed_commoner_naboo_bothan_male_02.iff')
	#templates.add('object/mobile/shared_dressed_commoner_naboo_bothan_female_01.iff')
	#templates.add('object/mobile/shared_dressed_commoner_naboo_bothan_female_02.iff')
	mobileTemplate.setTemplates(templates)
		
	weaponTemplates = Vector()
	weapontemplate = WeaponTemplate('object/weapon/melee/unarmed/shared_unarmed_default.iff', WeaponType.UNARMED, 1.0, 6, 'kinetic')
	weaponTemplates.add(weapontemplate)
	mobileTemplate.setWeaponTemplateVector(weaponTemplates)
	
	attacks = Vector()
	mobileTemplate.setDefaultAttack('creatureMeleeAttack')
	mobileTemplate.setAttacks(attacks)
	
	core.spawnService.addMobileTemplate('info_broker', mobileTemplate)
	return