import pandas as pd
import plotly.express as px

def main():
    df = pd.read_csv('purchasingpower.csv')
    print(df['Año'])




if __name__ == "__main__":
    main()
