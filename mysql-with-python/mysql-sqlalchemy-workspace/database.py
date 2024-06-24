from sqlalchemy import Column, String, Integer, create_engine, ForeignKey
from sqlalchemy.orm import registry, relationship
import os

mysq_root_password = os.getenv("PASSWORD")

engine = create_engine(f'mysql+mysqlconnector://root:{mysq_root_password}@localhost:3306/projects', echo=True)

mapper_registry = registry()

Base = mapper_registry.generate_base()

class Project(Base):
    __tablename__ = 'projects'
    project_id = Column(Integer, primary_key=True)
    title = Column(String(length=50))
    description = Column(String(length=50))

    def __repr__(self):
        return "<Project(title'{0}, description='{1}')>".format(self.title, self.description)

class Task(Base):
    __tablename__ = 'tasks'
    task_id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey('projects.project_id'))
    description = Column(String(length=50))

    project = relationship("Project")

    def __repr__(self):
        return "<Task(description='{0}')>".format(self.description)


Base.metadata.create_all(engine)
