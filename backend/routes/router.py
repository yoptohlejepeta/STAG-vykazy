from fastapi import APIRouter, Depends

from database import get_db
from models.project import Project
from schemas.project import ProjectBase

router = APIRouter(prefix="/projects")


@router.post("", response_model=ProjectBase)
def create_project(project: ProjectBase, db=Depends(get_db)):
    project = Project(**project.model_dump())
    db.add(project)
    db.commit()
    db.refresh(project)

    return project


@router.get("/{project_id}", response_model=ProjectBase)
def read_project(project_id: int, db=Depends(get_db)):
    project = db.query(Project).filter(Project.id == project_id).first()
    return project


@router.get("", response_model=list[ProjectBase])
def read_projects(db=Depends(get_db)):
    projects = db.query(Project).all()
    return projects
