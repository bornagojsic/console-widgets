@echo off

if not exist test goto nematestdirektorija
if not exist radni goto nemaradnidirektorija
if not exist test\stimer.exe goto nematimer
if not exist test\etimer.exe goto nematimer
if not exist test\diff.exe goto nemadiff
if "%1" == "" goto falizadatak

if not exist %1.py goto faliexe
if "%2" == "" goto svi

:jedan
rem --- Testiranje jednog primjera

if not exist test\%1 goto krivizadatak
if not exist test\%1\%1.in.%2 goto kriviin
if not exist test\%1\%1.out.%2 goto kriviout

echo.
echo Zadatak %1, test podatak %2:
echo ===== Sluzbeno rjesenje =====
type test\%1\%1.out.%2
echo == Natjecateljevo rjesenje ==
set STARTTIME=%TIME% 
python %1.py < test\%1\%1.in.%2 > radni\%1.out.%2 2> radni\%1.stderr.%2
set ENDTIME=%TIME%
type radni\%1.out.%2
type radni\%1.stderr.%2
echo =============================
rem --- convert STARTTIME and ENDTIME to hours, mins
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
echo Vrijeme: %totalsecs%.%ms%s
fc /b test\%1\%1.out.%2 radni\%1.out.%2 >nul&&goto ispravno||goto krivo

if errorlevel 1 goto krivo
goto ispravno

:krivo
echo Rjesenje NIJE ispravno
goto kraj

:ispravno
echo Rjesenje je ispravno
goto kraj


:svi
rem --- Testira sve primjere u nekom zadatku

if not exist test\%1 goto krivizadatak

for %%i in (1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20) do (
   if not exist test\%1\%1.in.%%i goto dalje
	call p3.bat %1 %%i
	rem --- pause >nul

:dalje
   echo >nul
)

goto kraj


:nematestdirektorija
rem --- Ne postoji direktorij test
echo Ne postoji direktorij test (sa test podacima)!
goto kraj

:nemaradnidirektorija
rem --- Ne postoji direktorij radni
echo Ne postoji direktorij radni (gdje se spremaju izlazi natjecatelja)!
goto kraj

:nematimer
rem --- Nema stimer.exe ili etimer.exe
echo U direktoriju test ne postoji stoperica!
goto kraj

:nemadiff
rem --- Nema diff.exe
echo U direktoriju test ne postoji diff program za usporedjivanje datoteka!
goto kraj

:krivizadatak
rem --- Zadatak ne postoji
echo U direktoriju test ne postoji zadatak %1!
goto kraj


:falizadatak
rem --- Nije zadan zadatak
echo Nije zadan zadatak (vidi upute).
echo Pravilno koristenje: t zadatak [broj_tp]
goto kraj


:kriviin
rem --- Zadan nepostojeci test podatak
echo Ne postoji test podatak %2 (datoteka test\%1\%1.in.%2)!
goto kraj


:kriviout
rem --- Zadan nepostojeci test podatak
echo Ne postoji test podatak %2 (datoteka test\%1\%1.out.%2)!
goto kraj

:faliexe
rem --- Zadan nepostojeci test podatak
echo Ne postoji natjecateljsko rjesenje (datoteka %1.py)!
goto kraj


rem ---
:kraj

echo.

