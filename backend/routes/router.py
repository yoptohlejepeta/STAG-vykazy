from pathlib import Path

import polars as pl
from fastapi import APIRouter

router = APIRouter(prefix="/data")


data_path = Path.joinpath(Path(__file__).parent, "../data/uchazeci_transformed.csv")
data = pl.read_csv(data_path)


@router.get("/okruhy")
def endpoint_okruhy() -> list[dict]:
    """Vrátí pivot table uchažecích podle okruhů."""
    okruhy_df = data.filter(pl.col("OKRUH1").is_not_null()).select(["OKRUH1", "OKRUH2"]).group_by(["OKRUH1", "OKRUH2"]).count().sort("OKRUH1")

    return okruhy_df.to_dicts()
