CREATE EXTENSION IF NOT EXISTS pgcrypto;

CREATE TABLE
    condominios (
        id UUID PRIMARY KEY NOT NULL,
        nome VARCHAR(60) NOT NULL,
        cep VARCHAR(9) NOT NULL,
        logradouro VARCHAR(60) NOT NULL,
        numero INTEGER NOT NULL,
        bairro VARCHAR(50) NOT NULL,
        uf VARCHAR(2) NOT NULL,
        cidade VARCHAR(50) NOT NULL,
        criado_em TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        alterado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );

CREATE TABLE
    corretores (
        id UUID PRIMARY KEY NOT NULL,
        nome VARCHAR(60) NOT NULL,
        codigo VARCHAR(4) NOT NULL,
        creci VARCHAR(7) NOT NULL,
        numero VARCHAR(15) NOT NULL,
        email VARCHAR(60) NOT NULL,
        data_nascimento VARCHAR(10),
        rg VARCHAR(9),
        cpf VARCHAR(14),
        criado_em TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        alterado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );