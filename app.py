from flask_migrate import Migrate
from src import create_app, db
from dotenv import load_dotenv

load_dotenv()


app = create_app("dev")
migrate = Migrate(app, db)

