from app import app
from flask_bootstrap import Bootstrap
import config

#app.config['SECRET_KEY'] = 'test'  强制写法
app.config.from_object(config)

bootstrap = Bootstrap(app)
if __name__ == '__main__':
    app.run()
# LeoLiu_web_flask
