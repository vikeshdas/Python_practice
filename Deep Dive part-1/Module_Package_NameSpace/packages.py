"""
-package is a module that contains other modules and packages,modules are files.
-a directory with __init__.py file and modules are called packages.
-__init.py tells a directory is a package.
-package is basically a folder and it contains python files(modueles),as a folder can contains onother folder ,a package can contains onother packages
-importing packages: import package_1.module_1

-It can be like below ,below is structure of a package.
app/
  package1/
    __init__.py
    module1.py
    module.py

"""

"""
package can also contains package 

app/
  package1/
    __init__.py
    module1.py
    module.py
    package2/
        __init__.py
        module3.py
        module4.py
"""


"""

app/
  module.py           
  package1/
    __init__.py
    module1.py
    module.py
    package2/
        __init__.py
        module3.py
        module4.py


-if we print module.__file__ :-ouput will be ...app/module.py(absolute path)
-module.__path__ :-not set (becuase it is not a package its module )
-module.package: it will print empty string because its not a package

-if we print package1.__file__ :-ouput will be ...app/module.py(absolute path)
-package1.__path__ :.../app/package1
-module.package: package1

-if we print module1.__file__   :- ...app/package/module1(absolute path)
-moduel1.__path__ :-not set (becuase module1 is not a package its module )
-module1.package: package1 (module1 is in package1)

"""

"""
import package1.package2.module4

-after improting above line 
-package1 will be imported and added sys.modules
-package2 will be imported and added sys.modules
-module1 will be imported and added sys.modules
"""

"""
app/
  module.py           
  package1/
    __init__.py
    module1.py
    module.py
    package2/
        __init__.py
        module3.py
        module4.py

import package1.package2

-when we import above package it does not load modules and package inside that package

-it only load package1,package2 in gloabal namesapace and sys.module

-module1,module2,module3,module3 will be loaded

import package1.package2.module3
-now module3 will be loaded

-If we want to load modules as well with package we need to go to __init__.py file of that package and import module in __init__.py file 
 -lets we want to load module1 and module2 when importing package1
  step1:- got to __init__.py file of package1 
  step2:- import module1,module2 in that file with full path 
        import package1.module1
        import package1.module1
-Now when you will import package 1 above both module will be loaded
"""