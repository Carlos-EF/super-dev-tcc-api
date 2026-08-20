import os
from uuid import UUID

from supabase import create_client, Client

class SupabaseStorage:

    def __init__(self):
        self.url = os.getenv('SUPABASE_URL')
        self.key = os.getenv('SUPABASE_SERVICE_KEY')
        self.bucket = os.getenv(
            'SUPABASE_BUCKET',
            'imoveis'
        )

        self.client: Client = create_client(
            self.url,
            self.key
        )