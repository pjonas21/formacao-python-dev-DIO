from sqlalchemy import create_engine
from sqlalchemy import text
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey

engine = create_engine("sqlite:///:memory")

metadata_obj = MetaData(schema='teste')

user = Table(
    'user',
    metadata_obj,
    Column('user_id', Integer, primary_key=True),
    Column('user_name', String(40), nullable=False),
    Column('email_address', String(120)),
    Column('nickname', String(50), nullable=False),
)

user_prefs = Table(
    "user_prefs", metadata_obj,
    Column('pref_id', Integer, primary_key=True),
    Column('user_id', Integer, ForeignKey('user.user_id'), nullable=False),
    Column('pref_name', String(40), nullable=False),
    Column('pref_value', String(100)),
)

for table in metadata_obj.sorted_tables:
    print(table)


metadata_db_obj = MetaData(schema='bank')
financial_info = Table(
    'financial_info', metadata_db_obj,
    Column('id', Integer, primary_key=True),
    Column('valoue', String(100), nullable=False),
)

sql_insert = text('insert into user values(1,"jonas","jonas@email.com","jonas89")')
engine.execute(sql_insert)

print('\nInformacoes da tabela user_prefs')
print(user_prefs.primary_key)
print(user_prefs.constraints)

print('\nInformacoes da tabela financial_info')
print(financial_info.primary_key)
print(financial_info.constraints)

print('\nConsultas com SQL')

sql = text('select * from user')
result = engine.execute(sql)
for row in result:
    print(row)






