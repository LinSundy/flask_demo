from app import create_app
import os
env = os.environ.get('FLASK_ENV', 'develop')
app = create_app(env)

if __name__ == '__main__':
    app.run()
