from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session

from database import get_db
from models.company import Company
from schemas.company import CompanyCreate, CompanyUpdate, CompanyResponse

router = APIRouter(
    prefix="/company",
    tags=["company"]
)


# Create Company
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=CompanyResponse)
def create_company(company: CompanyCreate, db: Session = Depends(get_db)):
    db_company = Company(**company.dict())

    db.add(db_company)
    db.commit()
    db.refresh(db_company)

    return db_company


# Get All Companies
@router.get("/", status_code=status.HTTP_200_OK, response_model=list[CompanyResponse])
def get_all_company(db: Session = Depends(get_db)):
    companies = db.query(Company).all()
    return companies


# Get Company By ID
@router.get("/{company_id}", status_code=status.HTTP_200_OK, response_model=CompanyResponse)
def get_company(company_id: int, db: Session = Depends(get_db)):
    company = db.query(Company).filter(Company.id == company_id).first()

    if company is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Company not found"
        )

    return company


# Update Company
@router.put("/{company_id}", status_code=status.HTTP_200_OK, response_model=CompanyResponse)
def update_company(company_id: int, company: CompanyUpdate, db: Session = Depends(get_db)):
    db_company = db.query(Company).filter(Company.id == company_id).first()

    if db_company is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Company not found"
        )

    update_data = company.dict(exclude_unset=True)

    for key, value in update_data.items():
        setattr(db_company, key, value)

    db.commit()
    db.refresh(db_company)

    return db_company


# Delete Company
@router.delete("/{company_id}", status_code=status.HTTP_200_OK)
def delete_company(company_id: int, db: Session = Depends(get_db)):
    db_company = db.query(Company).filter(Company.id == company_id).first()

    if db_company is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Company not found"
        )

    db.delete(db_company)
    db.commit()

    return {"message": "Company deleted successfully"}