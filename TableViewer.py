import pandas as pd


class TableView:
    """
    class for viewing your db objects as pandas DataFrames.
    """

    def __init__(self, table):
        self.table = table

    def view_table(self):
        """
        Takes django.db.models.Model.objects.all().values() as argument, returns pandas DataFrame
        """
        return pd.DataFrame(list(self.table))
