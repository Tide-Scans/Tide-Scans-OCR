@echo off
REM Create a virtual environment if it doesn't exist
if not exist myenv (
    python -m venv myenv
)

REM Activate the virtual environment
call myenv\Scripts\activate

REM Install the required packages
pip install -r requirements.txt

REM Run the application
python app.py

REM Deactivate the virtual environment
deactivate