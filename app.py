from flask import *
from apps import create_app
create_app()




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=77, debug=True)