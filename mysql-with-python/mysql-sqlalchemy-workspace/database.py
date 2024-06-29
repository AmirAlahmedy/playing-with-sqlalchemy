from sqlalchemy import Column, String, Integer, create_engine, ForeignKey
from sqlalchemy.orm import registry, relationship, Session
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

with Session(engine) as session:
    organize_closet_project = Project(title='Organize closet',
                                      description='Organize closet by color ans style')

    session.add(organize_closet_project)

    session.flush()  # flush the session to initialize the primary key

    tasks = [
        Task(project_id=organize_closet_project.project_id, description='Decide what clothes to donate'),
        Task(project_id=organize_closet_project.project_id, description='Organize summer clothes'),
        Task(project_id=organize_closet_project.project_id, description='Organize winter clothes')
    ]

    session.bulk_save_objects(tasks)

    session.commit()

