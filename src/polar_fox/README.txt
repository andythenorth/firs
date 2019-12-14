This project provides a package of common assets which are used in vehicle newgrfs by andythenorth.

*Examples*

- cargos for inclusion in cargo table
- refits by label for different classes of vehicle
- sprites for cargo graphics
- graphics constants
- pixa graphics processing module

Extend as needed.

*Usage*

There is a single script that will assemble the distributed files and copy them to consumers.  This assumes a specific filesystem layout and is not intended to be portable.

	python bin/distribute.py

*Caveats*

1. Not everything is common.  Assets local to the newgrf are preferred, unless they are 100% identical across multiple newgrfs.
2. Eventually this might grow too big and unwieldy.  If it does, split it. 

------------
Polar Fox License
------------
Copyright (C) andythenorth, and others.

Licensed under GPL(v2)
  http://www.gnu.org/licenses/gpl-2.0.html

----------------
License Exceptions
----------------
All assets within the project required to produce the distributed bundle (program) are GPL(v2) or GPL(v2)-compatible.

Copying, redistribution or modification of these assets must be GPL(v2) compliant.

Some assets which are optional for producing the distributed bundle (program) use free software licenses that are not GPL(v2) compatible.

Copying, redistribution or modification of these assets must be compliant with their respective licenses.

Bootstrap is used to produce HTML documentation and is licensed under the MIT License.
    https://github.com/twbs/bootstrap/blob/master/LICENSE
GPL-compatibility notes for HTML templates:
    https://www.gnu.org/licenses/old-licenses/gpl-2.0-faq.en.html#WMS

Silkscreen font is used for documentation, and is distributed under the Open Font License.
    http://www.kottke.org/plus/type/silkscreen/
GPL-compatibility notes for fonts:
    https://www.fsf.org/blogs/licensing/20050425novalis

