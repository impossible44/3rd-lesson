from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Boolean, Float, select

engine = create_engine("sqlite:///:memory:", echo=True)
metadata = MetaData()

students_table = Table(
    "students",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String),
    Column("is_active", Boolean),
    Column("gpa", Float)
)

metadata.create_all(engine)

with engine.connect() as connection:
    connection.execute(
        students_table.insert(),
        [
            {"name": "Леха", "is_active": True, "gpa": 4.8},
            {"name": "Серый", "is_active": False, "gpa": 3.9},
            {"name": "Бахрудин", "is_active": True, "gpa": 4.5}
        ]
    )
    connection.commit() 

with engine.connect() as connection:
    statement=select(students_table)
    result=connection.execute(statement)
    
    for row in result:
        print(row.id, row.name, row.is_active)
        
    statement2=select(students_table.c.name, students_table.c.gpa)
    result2=connection.execute(statement2)
    for row in result2:
        print(row.name, row.gpa)
    
