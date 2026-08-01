from pathlib import Path 
from sqlalchemy import text 
from tcc.infrastructure.connection import engine 

BROKER_SEED_FILE = Path(__file__).parent / 'seeds' / 'brokers.sql' 

def seed_brokers(): 
    sql = BROKER_SEED_FILE.read_text(encoding='utf-8') 
    with engine.begin() as conn: 
        count = conn.execute( 
            text('SELECT COUNT(*) FROM corretores')
              ).scalar_one() 
        
        if count > 0: 
            return print('Seed de corretores já executada.')

        conn.execute(text(sql))
        print('Corretores inseridos com sucesso!') 

if __name__ == '__main__': seed_brokers()