from pathlib import Path 
from sqlalchemy import text 
from tcc.infrastructure.connection import engine 

BROKER_SEED_FILE = Path(__file__).parent / 'seeds' / 'clients.sql' 

def seed_clients(): 
    sql = BROKER_SEED_FILE.read_text(encoding='utf-8') 
    with engine.begin() as conn: 
        count = conn.execute( 
            text('SELECT COUNT(*) FROM clientes')
              ).scalar_one() 
        
        if count > 0: 
            return print('Seed de clientes já executada.')

        conn.execute(text(sql))
        print('Clientes inseridos com sucesso!') 

if __name__ == '__main__': seed_clients()