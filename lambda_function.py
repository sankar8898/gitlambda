import pandas as pd
def lambda_handler(event, context):
    """
    AWS Lambda function handler.
    
    :param event: The event data passed to the function.
    :param context: The context object providing runtime information.
    :return: A response indicating the function executed successfully.
    """
    d = {'col1': [1,2], 'col2': [3,4]}
    df = pd.DataFrame(data=d)
    print(df)
    print('Done x1')
    # print("Event received:", event)
    # print("Context received:", context)
    
    # Your processing logic here
    return {
        'statusCode': 200,
        'body': 'Hello from Lambda!'
    }