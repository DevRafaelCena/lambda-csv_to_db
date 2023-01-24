from chalice import Chalice, Response
import pandas as pd
import json
import boto3

app = Chalice(app_name='myapp')

# Connect to s3
s3 = boto3.client('s3')


def remove_mask(value):
    return value.replace('.', '').replace('-', '').replace('/', '')


@app.route('/upload', methods=['GET'])
def upload():

    bucket = app.current_request.query_params['bucket_name']
    object_key = app.current_request.query_params['object_key']
    try:
        # Acessando o arquivo CSV no S3
        obj = s3.get_object(Bucket=bucket, Key=object_key)
        df = pd.read_csv(obj['Body'])

        df['cpf'] = df['cpf'].apply(remove_mask)
        df['cnpj'] = df['cnpj'].apply(remove_mask)


        df['data'] = pd.to_datetime(df['data'], format='%d/%m/%Y').dt.strftime('%Y-%m-%d')

        # Connect to database
        db = peewee.PostgresqlDatabase(
            'mydb',
            user='myuser',
            password='mypassword',
            host='myhost'
        )

        # Modelo da tabela
        class Data(peewee.Model):
            cpf = peewee.CharField()
            cnpj = peewee.CharField()
            data = peewee.DateField()

            class Meta:
                database = db

        # Criando tabela no banco de dados
        db.connect()
        db.create_tables([Data])

        # Inserindo informações tratadas na tabela
        for index, row in df.iterrows():
            Data.create(cpf=row['cpf'], cnpj=row['cnpj'], data=row['data'])

        return Response(
            body='Salvo com sucesso.',
            status_code=200,
            headers={'Content-Type': 'application/json'}
        )

    except Exception as e:
        return Response(
            body=str(e),
            status_code=500,
            headers={'Content-Type': 'application/json'}
        )
