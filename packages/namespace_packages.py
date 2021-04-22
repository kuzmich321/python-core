# What are implicit Namespace Packages?

# PEP 420

# Namespace packages are package-like
# directories
#   may contain modules
#   may contain nested regular packages
#   may contain nested namespace packages
#   but cannot contain __init__.py

# These directories are implicitly made into these special types of packages

# Mechanics
"""
utils/                  ==> does not contain __init__.py            ==> namespace package
	validators/         ==> does not contain __init__.py            ==> namespace package
		boolean.py      ==> boolean.py is a file with.py extension  ==> module
		date.py
		json/           ==> contains __init__.py                    ==> regular package
			__init__.py
			serializers                                             ==> module
			validators
"""

# Regular vs Namespace Packages
"""
Regular Package                                     Namespace Package
type = module                                       type = module
__init__.py = YES                                   __init__.py = NO
__file__ = package __init__                         __file__ = not set

paths = breaks if parent                            path = dynamic path computation
directories change and absolute                     so OK if parent directories change
import are used                                     (your imports will still need to be modified)

single package lives in single                      single package can live in multiple (non-nested)
directory                                           directories
													in fact, parts of the namespace may even be in a zip file
"""

# Example
"""
app/
	utils/
		validators/
			boolean.py
	common/
		__init__.py
		validators/
			boolean.py
"""

"""
	utils                                               common
type = module                                       type = module
__name__ = utils                                    __name__ = utils
__repr__() = <module utils (namespace)>             __repr__() = <module common from '.../app/common'>
__path__ = _Namespace(['.../app/utils'])            __path__ = ['.../app/utils']
__file__ = not set                                  __file__ = ...app/common/__init__.py
__package__ = utils                                 __package__ = common
"""
