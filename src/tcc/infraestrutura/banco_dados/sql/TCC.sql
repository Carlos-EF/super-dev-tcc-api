
CREATE TABLE clientes (
    id UUID PRIMARY KEY NOT NULL,

    nome VARCHAR(100) NOT NULL,

    codigo VARCHAR(10) NOT NULL,

    tipo VARCHAR(12) NOT NULL,

    celular VARCHAR(15) NOT NULL,

    email VARCHAR(40) NOT NULL,

    como_encontrou VARCHAR(14),

    status VARCHAR(7) NOT NULL,

    criado_em TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    alterado_em TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE interessados (
    id UUID PRIMARY KEY NOT NULL,

    id_cliente UUID NOT NULL UNIQUE,

    procurando VARCHAR(11) NOT NULL,

    orcamento INTEGER NOT NULL,

    orcamento_minimo INTEGER,

    orcamento_maximo INTEGER,

    quantidade_quartos INTEGER,

    quantidade_suites INTEGER,

    quantidade_banheiros INTEGER,

    quantidade_vagas INTEGER,

    quantidade_andares INTEGER,

    quantidade_salas INTEGER,

	criado_em TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    alterado_em TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_interessado_cliente
        FOREIGN KEY (id_cliente)
        REFERENCES clientes(id)
        ON DELETE CASCADE
);


CREATE TABLE proprietarios (
    id UUID PRIMARY KEY NOT NULL,

    id_cliente UUID NOT NULL UNIQUE,

    imovel_proprietario TEXT,

	criado_em TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    alterado_em TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_proprietario_cliente
        FOREIGN KEY (id_cliente)
        REFERENCES clientes(id)
        ON DELETE CASCADE
);


CREATE TABLE locatarios (
    id UUID PRIMARY KEY NOT NULL,

    id_cliente UUID NOT NULL UNIQUE,

    imovel_locatario TEXT,

	criado_em TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    alterado_em TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_locatario_cliente
        FOREIGN KEY (id_cliente)
        REFERENCES clientes(id)
        ON DELETE CASCADE
);


CREATE TABLE corretores (
    id UUID PRIMARY KEY NOT NULL,

    status VARCHAR(7) NOT NULL,

    tipo VARCHAR(12) NOT NULL,

    nome_completo VARCHAR(60) NOT NULL,

    codigo INTEGER NOT NULL,

    celular VARCHAR(15) NOT NULL,

    email VARCHAR(50) NOT NULL,

    creci VARCHAR(7) NOT NULL,

    data_nascimento VARCHAR(10),

    rg VARCHAR(9),

    cpf VARCHAR(14),

    criado_em TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    alterado_em TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);