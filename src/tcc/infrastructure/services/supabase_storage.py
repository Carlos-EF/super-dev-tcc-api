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

    def upload(
            self,
            file_bytes: bytes,
            path: str,
            content_type: str
    ) -> str:
        self.client.storage \
        .from_(self.bucket) \
        .upload(
            path=path,
            file=file_bytes,
            file_options={
                'content_type': content_type,
                'upsert': False
            }
        )

        return self.get_public_url(path)


    def get_public_url(
            self,
            path: str
    ) -> str:

        return self.client.storage \
        .from_(self.bucket) \
        .get_public_url(path=path)