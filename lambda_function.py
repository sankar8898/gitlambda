import pandas as pd
def lambda_handler(event, context):

    d = {'col1': [1,2], 'col2': [3,4]}
    df = pd.DataFrame(data=d)
    print(df)
    print('Donee 123789')
    # print("Event received:", event)
    # print("Context received:", context)