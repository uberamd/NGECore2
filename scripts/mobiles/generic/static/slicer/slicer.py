import sys
from services.spawn import MobileTemplate
from services.spawn import WeaponTemplate
from resources.datatables import WeaponType
from resources.datatables import Difficulty
from resources.datatables import Options
from java.util import Vector


def addTemplate(core):
	mobileTemplate = MobileTemplate()
	
	mobileTemplate.setCreatureName('slicer')
	mobileTemplate.setLevel(1)
	mobileTemplate.setDifficulty(Difficulty.NORMAL)
	mobileTemplate.setSocialGroup("thug")
	mobileTemplate.setOptionsBitmask(Options.INVULNERABLE)
		
	templates = Vector()
	templates.add('object/mobile/shared_dressed_criminal_slicer_human_male_01.iff')
	mobileTemplate.setTemplates(templates)
		
	weaponTemplates = Vector()
	weapontemplate = WeaponTemplate('object/weapon/melee/unarmed/shared_unarmed_default.iff', WeaponType.UNARMED, 1.0, 6, 'kinetic')
	
	weaponTemplates.add(weapontemplate)
	mobileTemplate.setWeaponTemplateVector(weaponTemplates)
	
	attacks = Vector()
	mobileTemplate.setDefaultAttack('rangedShot')
	mobileTemplate.setAttacks(attacks)
	
	core.spawnService.addMobileTemplate('slicer', mobileTemplate)
	return