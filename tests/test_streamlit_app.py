import pandas as pd
import pandas.testing as pdt
from src.streamlit_app import filter_passengers


def make_df():
    return pd.DataFrame({
        "Survived": [1, 0, 1, 0, 1],
        "Sex":      ["male", "female", "male", "female", "male"],
        "Age":      [25, 35, 45, 55, 65],
        "Embarked": ["S", "S", "C", "C", "Q"]
    })


def norm(df: pd.DataFrame) -> pd.DataFrame:
    return df.sort_values("Embarked").reset_index(drop=True)


def test_survived_only():
    df = make_df()
    got = filter_passengers(df, survived=1)
    expected = (
        df[(df["Survived"] == 1) & (df["Age"].between(30, 60))]
        .groupby("Embarked").size()
        .reset_index(name="Количество пассажиров (30–60 лет)")
    )
    pdt.assert_frame_equal(norm(got), norm(expected))


def test_male_only():
    df = make_df()
    got = filter_passengers(df, sex="male")
    expected = (
        df[(df["Sex"] == "male") & (df["Age"].between(30, 60))]
        .groupby("Embarked").size()
        .reset_index(name="Количество пассажиров (30–60 лет)")
    )
    pdt.assert_frame_equal(norm(got), norm(expected))


def test_male_and_survived():
    df = make_df()
    got = filter_passengers(df, survived=1, sex="male")
    expected = (
        df[(df["Survived"] == 1) & (df["Sex"] == "male") & (df["Age"].between(30, 60))]
        .groupby("Embarked").size()
        .reset_index(name="Количество пассажиров (30–60 лет)")
    )
    pdt.assert_frame_equal(norm(got), norm(expected))
