from app.server import app

# Web Server Gate Interface (WSGI) untuk deploy ke heroku
if __name__ == '__main__':
    app.run()
