# my-lambdata-johan-mazorra


Function to check for null values and split dates into multiple columns.

Usage

`from my_lambdata_johan_mazorra.my_mod import check_for_nulls`

`df = pd.DataFrame({'x': [1, 2, 3, 4, 5,np.nan],`
`'y': [np.nan,np.nan , 1, 2, 3, 4 ],`
`'z': [1, 2, 3, 4, 5, 6]})`

`df.check_for_nulls`

`from my_lambdata_johan_mazorra.my_mod import split_dates`

`df['name of column'].split_dates`