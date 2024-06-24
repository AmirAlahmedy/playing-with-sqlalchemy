import sqlalchemy
import os

mysq_root_password = os.getenv("PASSWORD")

engine = sqlalchemy.create_engine(f'mysql+mysqlconnector://root:{mysq_root_password}@localhost:3306/projects', echo=True)