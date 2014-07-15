# Project SWG:  Mos Eisley gunrunners:  Static Spawns
# (C)2014 ProjectSWG

import sys
from resources.datatables import Options
from resources.datatables import State
from java.util import Vector
from engine.resources.scene import Point3D

def addPlanetSpawns(core, planet):

	stcSvc = core.staticService
	objSvc = core.objectService
	aiSvc = core.aiService

	# gunrunners
	gunrunner = stcSvc.spawnObject('gunrunner', 'tatooine', long(0), float(2835), float(8), float(-4276), float(0), float(0), float(0), float(0), 45)
	gunrunner1 = stcSvc.spawnObject('gunrunner', 'tatooine', long(0), float(2818), float(7), float(-4265), float(0), float(0), float(0), float(0), 45)
	gunrunner2 = stcSvc.spawnObject('gunrunner', 'tatooine', long(0), float(2823), float(7), float(-4284), float(0), float(0), float(0), float(0), 45)
	gunrunner3 = stcSvc.spawnObject('gunrunner', 'tatooine', long(0), float(2806), float(7), float(-4253), float(0), float(0), float(0), float(0), 45)
	gunrunner4 = stcSvc.spawnObject('gunrunner', 'tatooine', long(0), float(2798), float(7), float(-4292), float(0), float(0), float(0), float(0), 45)
	gunrunner5 = stcSvc.spawnObject('gunrunner', 'tatooine', long(0), float(2848), float(7), float(-4316), float(0), float(0), float(0), float(0), 45)
	gunrunner6 = stcSvc.spawnObject('gunrunner', 'tatooine', long(0), float(2862), float(7), float(-4289), float(0), float(0), float(0), float(0), 45)
	gunrunner7 = stcSvc.spawnObject('gunrunner', 'tatooine', long(0), float(2842), float(7), float(-4299), float(0), float(0), float(0), float(0), 45)
	gunrunner8 = stcSvc.spawnObject('gunrunner', 'tatooine', long(0), float(2839), float(7), float(-4283), float(0), float(0), float(0), float(0), 45)
	gunrunner9 = stcSvc.spawnObject('gunrunner', 'tatooine', long(0), float(2799), float(6), float(-4277), float(0), float(0), float(0), float(0), 45)
	gunrunner10 = stcSvc.spawnObject('gunrunner', 'tatooine', long(0), float(2744), float(7), float(-4279), float(0), float(0), float(0), float(0), 45)
	gunrunner11 = stcSvc.spawnObject('gunrunner', 'tatooine', long(0), float(2794), float(7), float(-4301), float(0), float(0), float(0), float(0), 45)
	
	# gunrunner sentry
	gunrunner_sentry = stcSvc.spawnObject('gunrunner_sentry', 'tatooine', long(0), float(2830), float(8), float(-4270), float(0), float(0), float(0), float(0), 45)
	gunrunner_sentry1 = stcSvc.spawnObject('gunrunner_sentry', 'tatooine', long(0), float(2851), float(10), float(-4261), float(0), float(0), float(0), float(0), 45)
	gunrunner_sentry2 = stcSvc.spawnObject('gunrunner_sentry', 'tatooine', long(0), float(2824), float(6), float(-4297), float(0), float(0), float(0), float(0), 45)
	gunrunner_sentry3 = stcSvc.spawnObject('gunrunner_sentry', 'tatooine', long(0), float(2833), float(10), float(-4252), float(0), float(0), float(0), float(0), 45)
	gunrunner_sentry4 = stcSvc.spawnObject('gunrunner_sentry', 'tatooine', long(0), float(2830), float(6), float(-4308), float(0), float(0), float(0), float(0), 45)
	
	aiSvc.setLoiter(gunrunner, float(1), float(8))
	aiSvc.setLoiter(gunrunner1, float(1), float(8)) 
	aiSvc.setLoiter(gunrunner2, float(1), float(8)) 
	aiSvc.setLoiter(gunrunner3, float(1), float(8)) 
	aiSvc.setLoiter(gunrunner4, float(1), float(8)) 
	aiSvc.setLoiter(gunrunner5, float(1), float(8))  
	aiSvc.setLoiter(gunrunner6, float(1), float(8))
	aiSvc.setLoiter(gunrunner7, float(1), float(8)) 
	aiSvc.setLoiter(gunrunner8, float(1), float(8)) 
	aiSvc.setLoiter(gunrunner9, float(1), float(8)) 
	aiSvc.setLoiter(gunrunner10, float(1), float(8)) 
	aiSvc.setLoiter(gunrunner11, float(1), float(8))
	
	aiSvc.setLoiter(gunrunner_sentry, float(1), float(8))
	aiSvc.setLoiter(gunrunner_sentry1, float(1), float(8)) 
	aiSvc.setLoiter(gunrunner_sentry2, float(1), float(8)) 
	aiSvc.setLoiter(gunrunner_sentry3, float(1), float(8)) 
	aiSvc.setLoiter(gunrunner_sentry4, float(1), float(8)) 
	
	return	
