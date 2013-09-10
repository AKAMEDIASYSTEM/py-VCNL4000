# VCNL4000 test script

import VCNL4000 as vcnl
import time

v = vcnl.VCNL4000()
v.continuousConversionOn()

while True:
	print 'prox is ', v.readProximity()
	print 'ambient light is ', v.readAmbient()
	time.sleep(0.5)
