from flask_migrate import Migrate
from src import create_app, db
from dotenv import load_dotenv

load_dotenv()


app = create_app("dev")
migrate = Migrate(app, db)

with app.app_context():
    from src.seed import seed_data  # Importa a função seed_data do seu script seed.py
    seed_data()