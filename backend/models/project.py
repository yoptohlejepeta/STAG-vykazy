from sqlalchemy.orm import Mapped, mapped_column

from database import Base


class Project(Base):
    __tablename__ = "projects"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)
    # urls for dev, test, prod
    dev_url: Mapped[str] = mapped_column(unique=True)
    test_url: Mapped[str] = mapped_column(unique=True)
    prod_url: Mapped[str] = mapped_column(unique=True)
