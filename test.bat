@echo off

rem --- Creates empty tests.txt file
if not exist tests\tests.results copy /y NUL tests\tests.results >NUL

if not "%1" == "" goto onetest
goto alltests


:alltests
copy /y NUL tests\tests.results >NUL
for %%i in (tests/*.py) do call test.bat %%i
echo ========= Overall results =========
type tests\tests.results
echo ===================================
del tests\tests.results
goto end


:onetest
set test=%1
set test=%test:~0,-3%
rem --- echo %test%
rem --- pause >nul

if not exist tests\expected\%test%.txt goto noexpected
if not exist tests\results mkdir tests\results
rem --- Testing only one example

echo.
echo Testing %test%.py
echo ===== Expected result =====
type tests\expected\%test%.txt
echo ========= Results =========
set STARTTIME=%TIME%
python tests\%test%.py > tests\results\%test%.txt 2> tests\results\%test%.stderr
set ENDTIME=%TIME%
type tests\expected\%test%.txt
type tests\results\%test%.stderr
echo =============================

rem --- convert STARTTIME and ENDTIME to hours, mins, secs and milisecs
set options="tokens=1-4 delims=:.,"
for /f %options% %%a in ("%STARTTIME%") do set start_h=%%a&set /a start_m=100%%b %% 100&set /a start_s=100%%c %% 100&set /a start_ms=100%%d %% 100
for /f %options% %%a in ("%ENDTIME%") do set end_h=%%a&set /a end_m=100%%b %% 100&set /a end_s=100%%c %% 100&set /a end_ms=100%%d %% 100
set /a hours=%end_h%-%start_h%
set /a mins=%end_m%-%start_m%
set /a secs=%end_s%-%start_s%
set /a ms=%end_ms%-%start_ms%
if %ms% lss 0 set /a secs = %secs% - 1 & set /a ms = 100%ms%
if %secs% lss 0 set /a mins = %mins% - 1 & set /a secs = 60%secs%
if %mins% lss 0 set /a hours = %hours% - 1 & set /a mins = 60%mins%
if %hours% lss 0 set /a hours = 24%hours%
if 1%ms% lss 100 set ms=0%ms%
set /a totalsecs = %hours%*3600 + %mins%*60 + %secs%

echo.
echo Total time: %totalsecs%.%ms%s
echo.
fc tests\expected\%test%.txt tests\results\%test%.txt >nul&&goto passed||goto failed


:passed
echo Test %test% passed!
echo Test %test% passed! >> tests\tests.results
goto end


:failed
echo Test %test% FAILED!
echo Test %test% FAILED! >> tests\tests.results
goto end


:noexpected
echo The file with the expected result (%test%.txt) doesn't exist!
goto end


:end
echo.