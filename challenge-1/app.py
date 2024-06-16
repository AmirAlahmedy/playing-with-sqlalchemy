from sqlalchemy import create_engine, MetaData, Table, Column, BigInteger, String, insert

engine = create_engine('sqlite:///users.db', echo=True)

metadata = MetaData()

users_table = Table("Users", metadata, 
                     Column("User_Id", BigInteger),
                     Column("First Name", String),
                     Column("Last Name", String),
                     Column("Email Address", String))

metadata.create_all(engine)

with engine.connect() as conn:
    stmt = (
        insert(users_table)
            .values({
                "User_Id": 29810298800072,
                "First Name": "Amir",
                "Last Name": "Alahmedy",
                "Email Address": "ameer.alahmedy@gmail.com" 
            })
            )
    
    conn.execute(stmt)
    conn.commit()