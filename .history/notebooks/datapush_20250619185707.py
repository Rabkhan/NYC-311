from sqlalchemy import create_engine

engine = create_engine("postgresql+psycopg2://postgres:9890@localhost:5432/nyc_data")


#from sqlalchemy import create_engine

# engine = create_engine("postgresql+psycopg2://postgres:9890@localhost:5432/nyc_data")