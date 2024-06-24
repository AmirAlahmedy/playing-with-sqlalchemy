import sqlalchemy

engine = sqlalchemy.create_engine('sqlite:///movies.db', echo=True)

# The engine is the starting point for the SQLAlchemy application
# It allows your application to have multiple database connections
# and it manages those connections

with engine.connect() as conn:
    result = conn.execute(sqlalchemy.text("SELECT * FROM Movies"))
    for row in result:
        print(row)


# Using SQL expression languages
metadata = sqlalchemy.MetaData()

movies_table = sqlalchemy.Table("Movies", metadata,
                sqlalchemy.Column("title", sqlalchemy.Text),
                sqlalchemy.Column("director", sqlalchemy.Text),
                sqlalchemy.Column("year",  sqlalchemy.Integer))

metadata.create_all(engine) # To instantiate the table

with engine.connect() as conn:
    result = conn.execute(sqlalchemy.select(movies_table))
    for row in result:
        print(row)
        