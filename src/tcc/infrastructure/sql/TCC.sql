CREATE TABLE condominios {
    id UUID PRIMARY KEY NOT NULL,

    nome VARCHAR(60) NOT NULL,

    cep VARCHAR(9) NOT NULL,

    logradouro VARCHAR(60) NOT NULL,

    numero INTEGER NOT NULL,

    bairro VARCHAR(50) NOT NULL,

    uf VARCHAR(2) NOT NULL,

    cidade VARCHAR(50) NOT NULL,

    criado_em TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
}