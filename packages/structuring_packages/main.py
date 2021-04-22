from common import validators
from common import models
from common import helpers
import common

validators.is_boolean('true')
validators.is_json('{}')
validators.is_date('2021-01-01')
validators.is_numeric(15)

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


print('\n\n****** models ******')
for k in common.models.__dict__.keys():
	print(k)


print('\n\n****** posts ******')
for k in common.models.posts.__dict__.keys():
	print(k)


print('\n\n****** users ******')
for k in common.models.users.__dict__.keys():
	print(k)


print('\n\n****** helpers ******')
for k in helpers.__dict__.keys():
	print(k)


print('-----------------------')
print(helpers.say_hello('Python'))
print(helpers.factorial(6))
