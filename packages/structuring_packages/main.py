import common.validators as validators
import common

validators.is_boolean('true')
validators.is_json('{}')
validators.is_date('2021-01-01')
validators.is_numeric(15)

from common.validators import *

print('\n\n****** self ******')

for k in dict(globals()).keys():
	print(k)


print('\n\n****** common ******')
for k in common.__dict__.keys():
	print(k)


print('\n\n****** validators ******')
for k in common.validators.__dict__.keys():
	print(k)


print('\n\n****** numeric ******')
for k in common.validators.numeric.__dict__.keys():
	print(k)
