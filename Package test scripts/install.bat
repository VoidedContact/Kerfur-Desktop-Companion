@echo off
echo ==================================
echo Installing Python dependencies...
echo ==================================

python -m pip install --upgrade pip

echo.
echo Installing packages from requirements.txt...
python -m pip install -r requirements.txt

echo.
echo ==================================
echo Installation complete!
echo ==================================
pause