import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey, select, func
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import declarative_base, relationship, Session

Base = declarative_base()


class User(Base):
    __tablename__ = "user_account"

    # atributos
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)

    address = relationship(
        "Address", back_populates="user", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"User(id: {self.id}, name: {self.name}, fullname: {self.fullname})"


class Address(Base):
    __tablename__ = "user_address"

    # atributos
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user_account.id"), nullable=False)
    email_address = Column(String(255), unique=True, nullable=False)

    user = relationship("User", back_populates="address")

    def __repr__(self):
        return f"Address(id: {self.id}, email: {self.email_address})"


print(User.__tablename__)
print(Address.__table__)

# conexao banco de dados
engine = create_engine("sqlite://")

# criando classes como tabelas no banco de dados
Base.metadata.create_all(engine)

# investiga o schema do banco de dados e retorna algumas informacoes
inspector_engine = inspect(engine)
print(inspector_engine.has_table("user_account"))
print(inspector_engine.get_table_names())
print(inspector_engine.default_schema_name)

with Session(engine) as session:
    jonas = User(
        name="jonas",
        fullname="Paulo Jonas",
        address=[Address(email_address="jonas@email.com"),
                 Address(email_address="paulo@email.com")]
    )

    vanessa = User(
        name="vanessa",
        fullname="Vanessa Barros",
        address=[Address(email_address="vanessa@email.com")]
    )

    pedro = User(
        name="pedro",
        fullname="Pedro da Silva"
    )

    # enviando dados para o BD - persistencia de dados
    session.add_all([jonas, vanessa, pedro])

    session.commit()

stmt = select(User).where(User.name.in_(["jonas", "vanessa"]))

for user in session.scalars(stmt):
    print(user)

print('questao')
stmt_address = select(Address).where(Address.user_id.in_([1]))
for address in session.scalars(stmt_address):
    print(address)

stmt_order = select(User).order_by(User.fullname.desc())

#print([user for user in session.scalars(stmt_order)])

for user in session.scalars(stmt_order):
    print(user)

stmt_join = select(User.fullname, Address.email_address).join_from(Address, User)

print(stmt_join)

for result in session.scalars(stmt_join):
    print(result)

connection = engine.connect()

results = connection.execute(stmt_join).fetchall()
print("\nExecutando statement pela connection")

for result in results:
    print(result)

print()
stmt_count = select(func.count('*')).select_from(User)
print("Total de instancias da tabela User: ", end='')
for result in session.scalars(stmt_count):
    print(result)
