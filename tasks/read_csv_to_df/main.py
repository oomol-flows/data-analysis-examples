from oocana import Context
import pandas as pd

def main(inputs: dict, context: Context):
  # input.get("in") -> help you get node input value
  file = inputs.get("csv")
  df = pd.read_csv(file)
  context.preview(df)

  return { "df": df }