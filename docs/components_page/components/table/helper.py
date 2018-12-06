import dash_bootstrap_components as dbc
import pandas as pd

df = pd.DataFrame(
    {
        "First Name": ["Arthur", "Ford", "Zaphod", "Trillian"],
        "Last Name": ["Dent", "Prefect", "Beeblebrox", "Astra"],
    }
)

table = dbc.generate_table_from_df(df, striped=True, bordered=True, hover=True)
