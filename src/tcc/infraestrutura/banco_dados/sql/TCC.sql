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

    alterado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
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

    alterado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_interessado_cliente
        FOREIGN KEY (id_cliente)
        REFERENCES clientes(id)
        ON DELETE CASCADE
);


CREATE TABLE proprietarios (
    id UUID PRIMARY KEY NOT NULL,

    id_cliente UUID NOT NULL UNIQUE,

    imovel_associado UUID,

	criado_em TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    alterado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_proprietario_cliente
        FOREIGN KEY (id_cliente)
        REFERENCES clientes(id)
        ON DELETE CASCADE,

    CONSTRAINT fk_proprietario_imovel
        FOREIGN KEY (imovel_associado)
        REFERENCES imoveis(id)
        ON DELETE CASCADE
);


CREATE TABLE locatarios (
    id UUID PRIMARY KEY NOT NULL,

    id_cliente UUID NOT NULL UNIQUE,

    imovel_associado UUID,

	criado_em TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    alterado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_locatario_cliente
        FOREIGN KEY (id_cliente)
        REFERENCES clientes(id)
        ON DELETE CASCADE,

    CONSTRAINT fk_locatario_imovel
        FOREIGN KEY (imovel_associado)
        REFERENCES imoveis(id)
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

    alterado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE condominios (
    id UUID PRIMARY KEY NOT NULL,

    nome VARCHAR(100) NOT NULL,

    cep VARCHAR(9) NOT NULL,

    logradouro VARCHAR(60) NOT NULL,

    numero INTEGER NOT NULL,

    bairro VARCHAR(50) NOT NULL,

    estado VARCHAR(20) NOT NULL,

    cidade VARCHAR(40) NOT NULL,

	criado_em TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE imoveis (
    id UUID PRIMARY KEY NOT NULL,

    codigo VARCHAR(10) NOT NULL,
	
    proprietario UUID NOT NULL,
	
    corretor UUID NOT NULL,

    status VARCHAR(7) NOT NULL,

    tipo VARCHAR(12) NOT NULL,

    finalidade VARCHAR(10) NOT NULL,

    logradouro VARCHAR(100) NOT NULL,

    bairro VARCHAR(50) NOT NULL,

	complemento VARCHAR(50),

    cidade VARCHAR(50) NOT NULL,

    estado VARCHAR(16) NOT NULL,

    cep VARCHAR(9) NOT NULL,

    numero INTEGER NOT NULL,

    em_condominio BOOLEAN NOT NULL,

    condominio UUID,

    valor NUMERIC(10, 2) NOT NULL,

    valor_condominio NUMERIC(10, 2),

    valor_iptu NUMERIC(10, 2),

    quantidade_quartos INTEGER,

    quantidade_suites INTEGER,
    
    quantidade_banheiros INTEGER,

    quantidade_vagas INTEGER,

    quantidade_andares INTEGER,

    quantidade_salas INTEGER,

    eh_mobiliado BOOLEAN NOT NULL,

    criado_em TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    alterado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_condominio_imoveis
        FOREIGN KEY (condominio)
        REFERENCES condominios(id)
        ON DELETE CASCADE,
		
    CONSTRAINT fk_proprietario_imoveis
        FOREIGN KEY (proprietario)
        REFERENCES clientes(id)
        ON DELETE CASCADE,
		
    CONSTRAINT fk_corretor_imoveis
        FOREIGN KEY (corretor)
        REFERENCES corretores(id)
        ON DELETE CASCADE
)