from sanic import Sanic
from sanic_jinja2 import SanicJinja2

app = Sanic(__name__)
jinja = SanicJinja2(app)
app.config['WTF_CSRF_SECRET_KEY'] = 'top secret!'

session = {}
@app.middleware('request')
async def add_session(request):
    request['session'] = session


