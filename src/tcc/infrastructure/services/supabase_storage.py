from supabase import create_client, Client


class SupabaseStorage:

    def __init__(
        self,
        url: str,
        key: str,
        bucket: str
    ):
        self.url = url
        self.key = key
        self.bucket = bucket

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

        allowed_content_types = {
            'image/jpeg',
            'image/png',
            'image/webp'
        }

        if content_type not in allowed_content_types:
            raise ValueError(
                f'Tipo de imagem não permitido: {content_type}'
            )

        self.client.storage \
            .from_(self.bucket) \
            .upload(
                path=path,
                file=file_bytes,
                file_options={
                    'content-type': content_type,
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
            .get_public_url(
                path=path
            )

    def delete(
        self,
        path: str
    ) -> None:

        self.client.storage \
            .from_(self.bucket) \
            .remove(
                [path]
            )