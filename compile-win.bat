cd sprites
DEL firs.nfo

cd nfo
COPY header.nfo+textstrings.nfo+cargodefs.nfo firs.nfo

MOVE firs.nfo ../firs.nfo

cd ../../../
renum.exe firs/sprites/firs.nfo
grfcodec.exe -e -p 2 firs.nfo firs/sprites/

MOVE firs.grf firs/firs.grf

PAUSE
exit