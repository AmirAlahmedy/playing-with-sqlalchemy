from sqlalchemy import create_engine, MetaData, Table, Column, BigInteger, String, insert, select
import json

# Create the database and connect to it
engine = create_engine('sqlite:///users.db', echo=True)

metadata = MetaData()

# Create the 'Users' table
users_table = Table("Users", metadata,
                    Column("User_Id", BigInteger, unique=True),
                    Column("First Name", String),
                    Column("Last Name", String),
                    Column("Email Address", String))

metadata.create_all(engine)

# Read the data from a file
f = open('rows.json')
rows = json.load(f)

# Insert the rows into the table
with engine.connect() as conn:
    for row in rows:
        stmt = (
            insert(users_table)
            .values(row)
        )
        conn.execute(stmt)
        conn.commit()

    result = conn.execute(select(users_table))
    for row in result:
        print(row)
