"""
functional programming in python:
- list comprehension
- partial
- reduce
- map, filter (list comprehension is more pythonic)

TODO ...

Examples here:
- List comprehension
- List slicing
- Iterate over strings
- izip (zip iterator)
"""


"""
1. Basic example

transform parent / child association
"""

from itertools import izip

import pymel.core as pm

# 1. PyMEL + list comprehension
transforms = ['joint1', 'joint2', 'joint3', 'joint4']
# convert strings to PyNodes
transforms = [pm.PyNode(transform) for transform in transforms]
# create list of parents
parents = [transform.getParent() for transform in transforms]
for parent, child in izip(parents, transforms):
    print('%s > %s' % (parent, child))
# None > joint1
# joint1 > joint2
# joint2 > joint3
# joint3 > joint4


# 2. Strings + list slicing
transforms = ['joint1', 'joint2', 'joint3', 'joint4']
for parent, child in izip(transforms[:-1], transforms[1:]):
    print('%s > %s' % (parent, child))
    # joint1 > joint2
    # joint2 > joint3
    # joint3 > joint4


"""
2. Bad example (Thanks to Viktoras Makauskas for pointing it out)

Essential attribute connections for 
transform driver, driven relationship.
"""

import pymel.core as pm

driver, driven = pm.ls(selection=True, type='transform')

# 1. list comprehension
for attribute in [at + ax for at in 'trs' for ax in 'xyz'] + ['ro']:
    driver.attr(attribute) >> driven.attr(attribute)

# 2. constant is better here, because it is:
#    - more readable
#    - almost same character count
transform_attributes = ['tx', 'ty', 'tz',
                        'rx', 'ry', 'rz',
                        'sx', 'sy', 'sz',
                        'ro']
for attribute in transform_attributes:
    driver.attr(attribute) >> driven.attr(attribute)

# 3. using parent attr
transform_attributes = ['t', 'r', 's', 'ro']
for attribute in transform_attributes:
    driver.attr(attribute) >> driven.attr(attribute)