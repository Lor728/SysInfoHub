@echo off
REM Build the standalone executable and then compile the Inno Setup installer.
REM Update the ISCC_PATH variable if Inno Setup is installed in a custom location.

set PYTHON=%~dp0env\Scripts\python.exe
set ISCC_PATH=ISCC.exe
set ICON=app_icon.ico
set SCRIPT=SysInfoHubInstaller.iss
set EXE_NAME=SysInfoHub

if not exist "%PYTHON%" (
    echo Python executable not found at %PYTHON%
    echo Make sure your virtual environment exists.
    pause
    exit /b 1
)

if not exist "%ICON%" (
    echo Icon file not found: %ICON%
    echo Place your .ico file in the project root and try again.
    pause
    exit /b 1
)

echo Building standalone executable...
"%PYTHON%" -m PyInstaller --onefile --windowed --icon="%ICON%" --name "%EXE_NAME%" main.py
if errorlevel 1 (
    echo PyInstaller build failed.
    pause
    exit /b 1
)

if not exist "dist\%EXE_NAME%.exe" (
    echo Expected executable not found: dist\%EXE_NAME%.exe
    pause
    exit /b 1
)

echo Compiling Inno Setup installer...
"%ISCC_PATH%" "%SCRIPT%"
if errorlevel 1 (
    echo Inno Setup compiler failed.
    echo Make sure ISCC.exe is on your PATH or update ISCC_PATH in this batch file.
    pause
    exit /b 1
)

echo Installer created successfully.
pause
