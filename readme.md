# Pasos

0. pip install virtualenv
1. virtualenv venv --python=python3.8
2. source venv/bin/activate
3. pip frees -> no hay nada
4. touch requirements.txt
5. pip install -r requirements.txt


pytest tests\test_math_func.py -v -m strings --disable-warnings

pytest tests\test_math_func.py -v -k "add o strings" --disable-warnings