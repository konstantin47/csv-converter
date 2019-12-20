from app import app
import sys


if len(sys.argv) != 2:
    print('\nPass env as parameter (prod or dev)\n')
else:
    if sys.argv[1] == 'prod':
        app.run(debug=False)
    elif sys.argv[1] == 'dev':
        app.run(debug=True)
    else:
        print('\nNo such environment!\n')
