@echo off
echo ==================================
echo Installing Python dependencies...
echo ==================================

python -m pip install --upgrade pip

echo.
echo Installing required Kerfur packages...
python -m pip install pygame-ce
python -m pip install pywin32

echo.
echo ==================================
echo Installation complete!
echo ==================================
pause
