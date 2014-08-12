import sys
from services.spawn import MobileTemplate
from services.spawn import WeaponTemplate
from resources.datatables import WeaponType
from resources.datatables import Difficulty
from resources.datatables import Options
from java.util import Vector


def addTemplate(core):
	mobileTemplate = MobileTemplate()
	
	mobileTemplate.setCreatureName('gurnaset_hatchling')
	mobileTemplate.setLevel(49)
	mobileTemplate.setDifficulty(Difficulty.NORMAL)
	mobileTemplate.setMinSpawnDistance(4)
	mobileTemplate.setMaxSpawnDistance(8)
	mobileTemplate.setDeathblow(False)
	mobileTemplate.setScale(1)
	mobileTemplate.setMeatType("Herbivore Meat")
	mobileTemplate.setMeatAmount(351)
	mobileTemplate.setHideType("Leathery Hide")
	mobileTemplate.setHideAmount(278)
	mobileTemplate.setBoneType("Mammal Bone")
	mobileTemplate.setBoneAmount(7)
	mobileTemplate.setSocialGroup("gurnaset")
	mobileTemplate.setAssistRange(303)
	mobileTemplate.setStalker(False)
	mobileTemplate.setOptionsBitmask(Options.ATTACKABLE)
	
	
	templates = Vector()
	templates.add('object/mobile/shared_gurnaset.iff')
	mobileTemplate.setTemplates(templates)
	
	
	weaponTemplates = Vector()
	weapontemplate = WeaponTemplate('object/weapon/melee/unarmed/shared_unarmed_default.iff', WeaponType.UNARMED, 1.0, 6, 'kinetic')
	weaponTemplates.add(weapontemplate)
	mobileTemplate.setWeaponTemplateVector(weaponTemplates)

	
	attacks = Vector()
	attacks.add('bm_bite_3')
	attacks.add('bm_kick_3')
	attacks.add('bm_spit_3')
	
	mobileTemplate.setDefaultAttack('creatureMeleeAttack')
	mobileTemplate.setAttacks(attacks)
	
		
	core.spawnService.addMobileTemplate('gurnaset_hatchling', mobileTemplate)
	return