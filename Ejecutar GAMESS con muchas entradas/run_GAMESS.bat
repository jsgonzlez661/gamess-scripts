@ECHO off
REM Script de GAMESS
ECHO.
ECHO ----------------------------------------------------------
ECHO  ######      ###    ##     ## ########  ######   ######  
ECHO ##    ##    ## ##   ###   ### ##       ##    ## ##    ## 
ECHO ##         ##   ##  #### #### ##       ##       ##       
ECHO ##   #### ##     ## ## ### ## ######    ######   ######  
ECHO ##    ##  ######### ##     ## ##             ##       ## 
ECHO ##    ##  ##     ## ##     ## ##       ##    ## ##    ## 
ECHO  ######   ##     ## ##     ## ########  ######   ######  
ECHO ----------------------------------------------------------
ECHO -------------------- Script  1.21v -----------------------
ECHO.
ECHO Ejecutando
ECHO.

:reader
FOR /f "tokens=*" %%A IN (job.txt) DO (
	CALL rungms.bat %%A > %%A.log
REM	call rungms.bat %%A.inp 11-32 1 0 %%A.log
ECHO ----------------------------------------------------------
ECHO ** // %%A Listo // **
ECHO ----------------------------------------------------------
ECHO.
)

PAUSE
EXIT




