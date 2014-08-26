import sys
from services.spawn import MobileTemplate
from services.spawn import WeaponTemplate
from resources.datatables import WeaponType
from resources.datatables import Difficulty
from resources.datatables import Options
from java.util import Vector


def addTemplate(core):
	mobileTemplate = MobileTemplate()
	
	mobileTemplate.setCreatureName('kaadu')
	mobileTemplate.setLevel(8)
	mobileTemplate.setMinLevel(8)
	mobileTemplate.setMaxLevel(12)
	mobileTemplate.setDifficulty(Difficulty.NORMAL)

	mobileTemplate.setMinSpawnDistance(4)
	mobileTemplate.setMaxSpawnDistance(8)
	mobileTemplate.setDeathblow(False)
	mobileTemplate.setScale(1)
	mobileTemplate.setMeatType("Avian Meat")
	mobileTemplate.setMeatAmount(120)
	mobileTemplate.setHideType("Leathery Hide")
	mobileTemplate.setHideAmount(85)
	mobileTemplate.setBoneType("Avian Bones")
	mobileTemplate.setBoneAmount(70)
	mobileTemplate.setMilkType('Wild Milk')
	mobileTemplate.setMilkAmount(60)
	mobileTemplate.setSocialGroup("kaadu")
	mobileTemplate.setAssistRange(0)
	mobileTemplate.setStalker(False)
	mobileTemplate.setOptionsBitmask(Options.ATTACKABLE)
	
	templates = Vector()
	templates.add('object/mobile/shared_kaadu_hue.iff')
	mobileTemplate.setTemplates(templates)
	
	weaponTemplates = Vector()
	weapontemplate = WeaponTemplate('object/weapon/melee/unarmed/shared_unarmed_default.iff', WeaponType.UNARMED, 1.0, 6, 'kinetic')
	weaponTemplates.add(weapontemplate)
	mobileTemplate.setWeaponTemplateVector(weaponTemplates)
	
	attacks = Vector()
	attacks.add('bm_bite_1')
	attacks.add('bm_claw_1')
	attacks.add('bm_hamstring_1')
	attacks.add('bm_provoke_1')
	
	mobileTemplate.setDefaultAttack('creatureMeleeAttack')
	mobileTemplate.setAttacks(attacks)
	
	core.spawnService.addMobileTemplate('kaadu', mobileTemplate)
	return