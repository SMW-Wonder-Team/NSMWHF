@echo off
echo NSMWHF Rom Builder by Souldbminer
echo Converting files... Please wait...
python3 build/script/defineBuilder.py DEFINES.CONFIG build/temp/defines.asm
python3 build/script/ramMapBuilder.py RAM.CONFIG build/temp/ram.asm
echo Done converting files!
echo Building Rom... Please wait...
echo. 2>smw.smc
asar -wno1009 -wno1018 --fix-checksum=off --symbols=nocash --define _VER=!__VER_U nsmwhf.asm YourRomHack.smc
echo Cleaning up... Please wait...
del smw.smc
echo Rom Built! Press ENTER to exit this window.

pause