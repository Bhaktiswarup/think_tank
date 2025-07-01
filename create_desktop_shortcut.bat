@echo off
title Create Desktop Shortcut - UltimateThinktank

echo.
echo ========================================
echo  Creating Desktop Shortcut for UltimateThinktank
echo ========================================
echo.

:: Get the current directory (project root)
set "PROJECT_DIR=%CD%"
set "DESKTOP_DIR=%USERPROFILE%\Desktop"
set "SHORTCUT_NAME=UltimateThinktank.bat"

echo Project directory: %PROJECT_DIR%
echo Desktop directory: %DESKTOP_DIR%
echo.

:: Create the shortcut file
echo Creating shortcut...

:: Create a VBS script to make the shortcut
echo Set oWS = WScript.CreateObject("WScript.Shell") > "%TEMP%\CreateShortcut.vbs"
echo sLinkFile = "%DESKTOP_DIR%\%SHORTCUT_NAME%" >> "%TEMP%\CreateShortcut.vbs"
echo Set oLink = oWS.CreateShortcut(sLinkFile) >> "%TEMP%\CreateShortcut.vbs"
echo oLink.TargetPath = "%PROJECT_DIR%\run_thinktank.bat" >> "%TEMP%\CreateShortcut.vbs"
echo oLink.WorkingDirectory = "%PROJECT_DIR%" >> "%TEMP%\CreateShortcut.vbs"
echo oLink.Description = "UltimateThinktank - AI Think Tank" >> "%TEMP%\CreateShortcut.vbs"
echo oLink.IconLocation = "%PROJECT_DIR%\run_thinktank.bat,0" >> "%TEMP%\CreateShortcut.vbs"
echo oLink.Save >> "%TEMP%\CreateShortcut.vbs"

:: Run the VBS script
cscript //nologo "%TEMP%\CreateShortcut.vbs"

:: Clean up
del "%TEMP%\CreateShortcut.vbs"

if exist "%DESKTOP_DIR%\%SHORTCUT_NAME%" (
    echo.
    echo ✅ Desktop shortcut created successfully!
    echo.
    echo Shortcut location: %DESKTOP_DIR%\%SHORTCUT_NAME%
    echo.
    echo You can now double-click the shortcut on your desktop to run the think tank.
    echo.
) else (
    echo.
    echo ❌ Failed to create desktop shortcut.
    echo.
    echo You can still run the think tank by double-clicking:
    echo %PROJECT_DIR%\run_thinktank.bat
    echo.
)

pause 