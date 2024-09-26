from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import alembic.config

Base = declarative_base()
engine = create_engine('sqlite:///company.db')
Session = sessionmaker(bind=engine)
session = Session()

class Company(Base):
    __tablename__ = 'companies'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    location = Column(String, nullable=False)
    industry = Column(String, nullable=False)

def create_company(company: Company):
    session.add(company)
    session.commit()
    print(f"Empresa {company.name} adicionada com sucesso.")

def read_company(company_id: int):
    company = session.query(Company).filter_by(id=company_id).first()
    if company:
        return company
    else:
        print(f"Empresa com ID {company_id} não encontrada.")
        return None

def update_company(company_id: int, kwargs: dict):
    company = session.query(Company).filter_by(id=company_id).first()
    if company:
        for key, value in kwargs.items():
            if hasattr(company, key):
                setattr(company, key, value)
        session.commit()
        print(f"Empresa {company.name} atualizada com sucesso.")
    else:
        print(f"Empresa com ID {company_id} não encontrada.")

def delete_company(company_id: int):
    company = session.query(Company).filter_by(id=company_id).first()
    if company:
        session.delete(company)
        session.commit()
        print(f"Empresa {company.name} removida com sucesso.")
    else:
        print(f"Empresa com ID {company_id} não encontrada.")

def main():
    Base.metadata.create_all(engine)

    company = Company(name="Azimute Racional Tecnologia", location="Portugal", industry="Tecnologia")
    create_company(company)

    company_from_db = read_company(company.id)
    if company_from_db:
        print(f"Empresa encontrada: {company_from_db.name}, {company_from_db.location}, {company_from_db.industry}")

    update_company(company.id, {'location': 'Brasil'})

    updated_company = read_company(company.id)
    if updated_company:
        print(f"Empresa atualizada: {updated_company.name}, {updated_company.location}, {updated_company.industry}")

    delete_company(company.id)

    read_company(company.id)

if __name__ == "__main__":
    main()