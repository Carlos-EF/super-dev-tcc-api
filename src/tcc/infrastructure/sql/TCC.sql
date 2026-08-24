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

CREATE TABLE
    clientes (
        id UUID PRIMARY KEY NOT NULL,
        nome VARCHAR(60) NOT NULL,
        codigo VARCHAR(4) NOT NULL,
        numero VARCHAR(15) NOT NULL,
        email VARCHAR(60) NOT NULL,
        tipo VARCHAR(12) NOT NULL,
        como_encontrou VARCHAR(18),
        criado_em TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        alterado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );

CREATE TABLE
    interessados (
        id UUID PRIMARY KEY NOT NULL,
        cliente_id UUID NOT NULL,
        procura VARCHAR(11),
        finalidade VARCHAR(7),
        preferencia VARCHAR(50),
        criado_em TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        alterado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (cliente_id) REFERENCES clientes (id) ON DELETE CASCADE
    );

CREATE TABLE
    imoveis (
        id UUID PRIMARY KEY NOT NULL,
        proprietario_id UUID,
        corretor_id UUID,
        codigo VARCHAR(4) NOT NULL,
        finalidade VARCHAR(7) NOT NULL,
        tipo VARCHAR(15) NOT NULL,
        em_condominio BOOLEAN NOT NULL DEFAULT FALSE,
        condominio UUID,
        cep VARCHAR(9) NOT NULL,
        logradouro VARCHAR(60) NOT NULL,
        numero INTEGER NOT NULL,
        bairro VARCHAR(50) NOT NULL,
        uf VARCHAR(2) NOT NULL,
        cidade VARCHAR(50) NOT NULL,
        complemento VARCHAR(60),
        valor NUMERIC(12, 2),
        valor_iptu NUMERIC(12, 2),
        valor_condominio NUMERIC(12, 2),
        criado_em TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        alterado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

        CONSTRAINT fk_imovel_proprietario FOREIGN KEY (proprietario_id) REFERENCES clientes (id) ON DELETE SET NULL,
        CONSTRAINT fk_imovel_corretor FOREIGN KEY (corretor_id) REFERENCES corretores (id) ON DELETE SET NULL,
        CONSTRAINT fk_imovel_condominio FOREIGN KEY (condominio) REFERENCES condominios (id) ON DELETE SET NULL
    );

CREATE TABLE
    casas (
        id UUID PRIMARY KEY NOT NULL,
        imovel_id UUID NOT NULL,
        metragem NUMERIC(10, 2),
        quartos INTEGER,
        suites INTEGER,
        banheiros INTEGER,
        garagens INTEGER,
        andares INTEGER,
        salas INTEGER,
        esta_mobiliado VARCHAR(15),
        mobilia TEXT[] DEFAULT '{}',
        criado_em TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        alterado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

        CONSTRAINT fk_casa_imovel FOREIGN KEY (imovel_id) REFERENCES imoveis (id) ON DELETE CASCADE,
        CONSTRAINT uq_casa_imovel UNIQUE (imovel_id)
    );

CREATE TABLE
    apartamentos (
        id UUID PRIMARY KEY NOT NULL,
        imovel_id UUID NOT NULL,
        metragem NUMERIC(10, 2),
        quartos INTEGER,
        suites INTEGER,
        banheiros INTEGER,
        garagens INTEGER,
        andares INTEGER,
        salas INTEGER,
        esta_mobiliado VARCHAR(15),
        mobilia TEXT[] DEFAULT '{}',
        criado_em TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        alterado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

        CONSTRAINT fk_apartamento_imovel FOREIGN KEY (imovel_id) REFERENCES imoveis (id) ON DELETE CASCADE,
        CONSTRAINT uq_apartamento_imovel UNIQUE (imovel_id)
    );

CREATE TABLE
    terrenos (
        id UUID PRIMARY KEY NOT NULL,
        imovel_id UUID NOT NULL,
        area_total NUMERIC(12, 2),
        medida_esquerda NUMERIC(10, 2),
        medida_direita NUMERIC(10, 2),
        medida_frente NUMERIC(10, 2),
        medida_fundo NUMERIC(10, 2),
        zoneamento VARCHAR(50),
        coeficiente NUMERIC(10, 2),
        criado_em TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        alterado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

        CONSTRAINT fk_terreno_imovel FOREIGN KEY (imovel_id) REFERENCES imoveis (id) ON DELETE CASCADE,
        CONSTRAINT uq_terreno_imovel UNIQUE (imovel_id)
    );


CREATE TABLE 
    imagens_imoveis (
        id UUID PRIMARY KEY,
        imovel_id UUID NOT NULL,
        caminho VARCHAR(500) NOT NULL,
        url VARCHAR(1000) NOT NULL,
        principal BOOLEAN NOT NULL DEFAULT FALSE,
        criado_em DATE NOT NULL,
        alterado_em DATE,

        CONSTRAINT fk_imagens_imoveis_imovel
        FOREIGN KEY (imovel_id)
        REFERENCES imoveis(id)
        ON DELETE CASCADE
    );

CREATE TABLE
    usuarios (
        id UUID PRIMARY KEY NOT NULL,
        nome VARCHAR(60) NOT NULL,
        email VARCHAR(60) NOT NULL,
        senha_hash VARCHAR(255) NOT NULL,
        ativo BOOLEAN NOT NULL DEFAULT TRUE,
        criado_em TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        alterado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

        CONSTRAINT uq_usuario_email
            UNIQUE (email)
    );