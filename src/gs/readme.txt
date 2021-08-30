Minimal GS - a boilerplate for GS authors

Minimal GS author: Zuu
Forum thread: http://www.tt-forums.net/viewtopic.php?f=65&t=62163


** SuperLib **
The boilerplate imports SuperLib and makes use of a few helpers
from the library. However, none of these are truly mandatory. Log
can easily be replaced with GSLog and drop the info.nut log level
parameter. The other helpers used are mostly for making it easy
to both support old (1.2, 1.3) OpenTTD versions and yet make use
of new functionality in trunk.

If you keep SuperLib, please update the import statement to the
last available version ( http://bananas.openttd.org/en/gslibrary/ ),
and set SuperLib as dependency when you upload your script to
bananas. When you make updates, this needs to be repeated because
the dependency in bananas can (when this was written) only be set
to the last version of a library.

By following this dependency recommendation, you make it much
easier for users to download your script and automatically get
all dependencies without any extra work for them.
