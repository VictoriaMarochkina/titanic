import streamlit as st
import pandas as pd


def filter_passengers(df, survived=None, sex=None):

    if survived == 1:
        df = df[df["Survived"] == 1]
    elif survived == 0:
        df = df[df["Survived"] == 0]

    if sex == "male":
        df = df[df["Sex"] == "male"]
    elif sex == "female":
        df = df[df["Sex"] == "female"]

    tx_df = df[(df["Age"] >= 30) & (df["Age"] <= 60)]
    result = tx_df.groupby("Embarked").size().reset_index(name="Количество пассажиров (30–60 лет)")

    return result


def load_data():
    return pd.read_csv("data.csv")


def main():

    st.image("titanic.jpeg")
    st.title("Данные пассажиров Титаника")
    st.write("""
    Для просмотра данных только по спасённым или погибшим, выберите соответствующий пункт из списка.
    """)

    df = load_data()

    s_o = st.selectbox(
        "Значение поля Survived:",
        options=["Любое", "Выжившие (1)", "Погибшие (0)"]
    )

    s_s = st.selectbox(
        "Значение поля Sex:",
        options=["Любой", "Мужской", "Женский"]
    )

    survived_param = None
    if s_o == "Выжившие (1)":
        survived_param = 1
    elif s_o == "Погибшие (0)":
        survived_param = 0

    sex_param = None
    if s_s == "Мужской":
        sex_param = "male"
    elif s_s == "Женский":
        sex_param = "female"

    result = filter_passengers(df, survived=survived_param, sex=sex_param)

    st.dataframe(result)


if __name__ == "__main__":
    main()
