import os
from app import create_app

app = create_app()

# if __name__ == '__main__':
#     flask_app.run(debug=os.environ.get('ENABLE_DEBUG'))

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=8001)
