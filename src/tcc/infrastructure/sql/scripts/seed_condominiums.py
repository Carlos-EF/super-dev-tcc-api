from pathlib import Path
from sqlalchemy import text
from tcc.infrastructure.connection import engine


COND_SEED_FILE = Path(__file__).parent / 'seeds' /'condominiums.sql'


def seed_condominiums():
    sql = COND_SEED_FILE.read_text(encoding='utf-8')
    
    with engine.begin() as conn:
        count = conn.execute(
            text('SELECT COUNT(*) FROM condominios')
        ).scalar_one()
        
        if count > 0:
            return print('Seed já executada || dados testes no banco.')
        
        conn.execute(text(sql))
        print('Condominios inseridos com sucesso!')



if __name__ == '__main__':
    seed_condominiums()