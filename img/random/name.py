import os
import base64
import random

count = 1
# for a in os.listdir('.'):
# 	if not a.endswith('py'):
# 		os.rename(a,base64.b64encode(str(random.randint(0,100**10))))

for a in os.listdir('.'):
	if not a.endswith('py'):
		name = 'material-'+str(count)+'.png';
		if os.path.exists(name):
			count+=1;
			print('skip ',name)
			continue
		os.rename(a,'material-'+str(count)+'.png');
		count+=1;
