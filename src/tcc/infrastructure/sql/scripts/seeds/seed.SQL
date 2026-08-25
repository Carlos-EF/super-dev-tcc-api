CREATE EXTENSION IF NOT EXISTS pgcrypto;


-- ============================================================
-- TABELAS TEMPORÁRIAS
-- ============================================================

CREATE TEMP TABLE seed_condominios (
    seq INTEGER PRIMARY KEY,
    id UUID NOT NULL,
    nome VARCHAR(60) NOT NULL
) ON COMMIT DROP;


CREATE TEMP TABLE seed_corretores (
    seq INTEGER PRIMARY KEY,
    id UUID NOT NULL
) ON COMMIT DROP;


CREATE TEMP TABLE seed_clientes (
    seq INTEGER PRIMARY KEY,
    id UUID NOT NULL,
    tipo VARCHAR(12) NOT NULL
) ON COMMIT DROP;


CREATE TEMP TABLE seed_imoveis (
    seq INTEGER PRIMARY KEY,
    id UUID NOT NULL,
    tipo VARCHAR(15) NOT NULL
) ON COMMIT DROP;


-- ============================================================
-- 20 CONDOMÍNIOS
-- ============================================================

INSERT INTO seed_condominios (
    seq,
    id,
    nome
)
SELECT
    gs,
    gen_random_uuid(),
    CASE gs
        WHEN 1 THEN 'Residencial Jardim das Flores'
        WHEN 2 THEN 'Residencial Vila Nova'
        WHEN 3 THEN 'Condomínio Parque Azul'
        WHEN 4 THEN 'Residencial Bela Vista'
        WHEN 5 THEN 'Condomínio Morada do Sol'
        WHEN 6 THEN 'Residencial Bosque Verde'
        WHEN 7 THEN 'Condomínio Alameda'
        WHEN 8 THEN 'Residencial Vale Dourado'
        WHEN 9 THEN 'Condomínio Porto Seguro'
        WHEN 10 THEN 'Residencial Primavera'
        WHEN 11 THEN 'Condomínio Horizonte'
        WHEN 12 THEN 'Residencial das Palmeiras'
        WHEN 13 THEN 'Condomínio Villa Real'
        WHEN 14 THEN 'Residencial Monte Verde'
        WHEN 15 THEN 'Condomínio Estrela'
        WHEN 16 THEN 'Residencial São Miguel'
        WHEN 17 THEN 'Condomínio Jardim Europa'
        WHEN 18 THEN 'Residencial Santa Clara'
        WHEN 19 THEN 'Condomínio Golden Park'
        WHEN 20 THEN 'Residencial Colinas'
    END
FROM generate_series(1, 20) AS gs;


INSERT INTO condominios (
    id,
    nome,
    cep,
    logradouro,
    numero,
    bairro,
    uf,
    cidade,
    criado_em,
    alterado_em
)
SELECT
    id,
    nome,

    '89010-' || LPAD(seq::TEXT, 3, '0'),

    CASE
        WHEN seq % 4 = 0 THEN 'Rua XV de Novembro'
        WHEN seq % 4 = 1 THEN 'Rua das Acácias'
        WHEN seq % 4 = 2 THEN 'Rua das Palmeiras'
        ELSE 'Rua General Osório'
    END,

    100 + seq,

    CASE
        WHEN seq % 4 = 0 THEN 'Centro'
        WHEN seq % 4 = 1 THEN 'Velha'
        WHEN seq % 4 = 2 THEN 'Victor Konder'
        ELSE 'Itoupava Norte'
    END,

    'SC',
    'Blumenau',
    CURRENT_TIMESTAMP,
    CURRENT_TIMESTAMP

FROM seed_condominios;


-- ============================================================
-- 20 CORRETORES
-- ============================================================

INSERT INTO seed_corretores (
    seq,
    id
)
SELECT
    gs,
    gen_random_uuid()
FROM generate_series(1, 20) AS gs;


INSERT INTO corretores (
    id,
    nome,
    codigo,
    creci,
    numero,
    email,
    data_nascimento,
    rg,
    cpf,
    criado_em,
    alterado_em
)
SELECT
    id,

    CASE seq
        WHEN 1 THEN 'Carlos Almeida'
        WHEN 2 THEN 'Mariana Souza'
        WHEN 3 THEN 'Rafael Martins'
        WHEN 4 THEN 'Juliana Costa'
        WHEN 5 THEN 'Fernando Oliveira'
        WHEN 6 THEN 'Camila Rocha'
        WHEN 7 THEN 'Lucas Pereira'
        WHEN 8 THEN 'Beatriz Lima'
        WHEN 9 THEN 'Gabriel Santos'
        WHEN 10 THEN 'Amanda Ribeiro'
        WHEN 11 THEN 'Bruno Carvalho'
        WHEN 12 THEN 'Larissa Mendes'
        WHEN 13 THEN 'Diego Fernandes'
        WHEN 14 THEN 'Patrícia Gomes'
        WHEN 15 THEN 'Thiago Barbosa'
        WHEN 16 THEN 'Renata Alves'
        WHEN 17 THEN 'Marcelo Castro'
        WHEN 18 THEN 'Isabela Nunes'
        WHEN 19 THEN 'André Moreira'
        WHEN 20 THEN 'Carolina Freitas'
    END,

    LPAD(seq::TEXT, 4, '0'),

    LPAD((10 + seq)::TEXT, 2, '0')
    || '.'
    || LPAD((100 + seq)::TEXT, 3, '0')
    || 'F',

    -- 15 caracteres
    '(47) 99999-' || LPAD(seq::TEXT, 4, '0'),

    'corretor' || seq || '@email.com',

    '19'
    || LPAD((70 + (seq % 20))::TEXT, 2, '0')
    || '-01-01',

    LPAD((100000000 + seq)::TEXT, 9, '0'),

    LPAD((10000000000000 + seq)::TEXT, 14, '0'),

    CURRENT_TIMESTAMP,
    CURRENT_TIMESTAMP

FROM seed_corretores;


-- ============================================================
-- 30 CLIENTES
--
-- 1-10   Proprietário
-- 11-20  Locatário
-- 21-30  Interessado
-- ============================================================

INSERT INTO seed_clientes (
    seq,
    id,
    tipo
)
SELECT
    gs,
    gen_random_uuid(),

    CASE
        WHEN gs <= 10 THEN 'Proprietário'
        WHEN gs <= 20 THEN 'Locatário'
        ELSE 'Interessado'
    END

FROM generate_series(1, 30) AS gs;


INSERT INTO clientes (
    id,
    nome,
    codigo,
    numero,
    email,
    tipo,
    como_encontrou,
    criado_em,
    alterado_em
)
SELECT
    id,

    CASE seq
        WHEN 1 THEN 'João da Silva'
        WHEN 2 THEN 'Maria Oliveira'
        WHEN 3 THEN 'Pedro Souza'
        WHEN 4 THEN 'Ana Costa'
        WHEN 5 THEN 'Roberto Santos'
        WHEN 6 THEN 'Fernanda Lima'
        WHEN 7 THEN 'Ricardo Alves'
        WHEN 8 THEN 'Juliana Martins'
        WHEN 9 THEN 'Eduardo Rocha'
        WHEN 10 THEN 'Patrícia Gomes'

        WHEN 11 THEN 'Lucas Ferreira'
        WHEN 12 THEN 'Camila Mendes'
        WHEN 13 THEN 'Bruno Castro'
        WHEN 14 THEN 'Larissa Nunes'
        WHEN 15 THEN 'Diego Ramos'
        WHEN 16 THEN 'Amanda Barbosa'
        WHEN 17 THEN 'Thiago Freitas'
        WHEN 18 THEN 'Renata Carvalho'
        WHEN 19 THEN 'Marcelo Dias'
        WHEN 20 THEN 'Carolina Duarte'

        WHEN 21 THEN 'Gabriel Teixeira'
        WHEN 22 THEN 'Isabela Moura'
        WHEN 23 THEN 'André Lopes'
        WHEN 24 THEN 'Beatriz Cardoso'
        WHEN 25 THEN 'Felipe Martins'
        WHEN 26 THEN 'Marina Vieira'
        WHEN 27 THEN 'Gustavo Mendes'
        WHEN 28 THEN 'Cláudia Ribeiro'
        WHEN 29 THEN 'Henrique Souza'
        WHEN 30 THEN 'Vanessa Rocha'
    END,

    LPAD(seq::TEXT, 4, '0'),

    -- 15 caracteres
    '(47) 98888-' || LPAD(seq::TEXT, 4, '0'),

    'cliente' || seq || '@email.com',

    tipo,

    CASE
        WHEN seq % 5 = 0 THEN 'WhatsApp'
        WHEN seq % 5 = 1 THEN 'Indicação'
        WHEN seq % 5 = 2 THEN 'Instagram'
        WHEN seq % 5 = 3 THEN 'Portal imobiliário'
        ELSE 'Placa no imóvel'
    END,

    CURRENT_TIMESTAMP,
    CURRENT_TIMESTAMP

FROM seed_clientes;


-- ============================================================
-- 10 INTERESSADOS
-- ============================================================

INSERT INTO interessados (
    id,
    cliente_id,
    procura,
    finalidade,
    preferencia,
    criado_em,
    alterado_em
)
SELECT
    gen_random_uuid(),

    id,

    CASE
        WHEN seq % 3 = 0 THEN 'Casa'
        WHEN seq % 3 = 1 THEN 'Apartamento'
        ELSE 'Terreno'
    END,

    CASE
        WHEN seq % 2 = 0 THEN 'Comprar'
        ELSE 'Alugar'
    END,

    CASE
        WHEN seq % 2 = 0
            THEN 'Região Central'
        ELSE
            'Próximo ao bairro Velha'
    END,

    CURRENT_TIMESTAMP,
    CURRENT_TIMESTAMP

FROM seed_clientes
WHERE seq BETWEEN 21 AND 30;


-- ============================================================
-- 15 IMÓVEIS
--
-- 1-5   Casa
-- 6-10  Apartamento
-- 11-15 Terreno
-- ============================================================

INSERT INTO seed_imoveis (
    seq,
    id,
    tipo
)
SELECT
    gs,
    gen_random_uuid(),

    CASE
        WHEN gs <= 5 THEN 'Casa'
        WHEN gs <= 10 THEN 'Apartamento'
        ELSE 'Terreno'
    END

FROM generate_series(1, 15) AS gs;


INSERT INTO imoveis (
    id,
    proprietario_id,
    corretor_id,
    codigo,
    finalidade,
    tipo,
    em_condominio,
    condominio,
    cep,
    logradouro,
    numero,
    bairro,
    uf,
    cidade,
    complemento,
    valor,
    valor_iptu,
    valor_condominio,
    criado_em,
    alterado_em
)
SELECT
    p.id,

    (
        SELECT c.id
        FROM seed_clientes c
        WHERE c.seq = ((p.seq - 1) % 10) + 1
    ),

    (
        SELECT c.id
        FROM seed_corretores c
        WHERE c.seq = ((p.seq - 1) % 20) + 1
    ),

    LPAD((1000 + p.seq)::TEXT, 4, '0'),

    CASE
        WHEN p.seq IN (
            2, 4,
            7, 9,
            12, 14
        )
        THEN 'Locação'
        ELSE 'Venda'
    END,

    p.tipo,

    CASE
        WHEN p.tipo = 'Apartamento' THEN TRUE
        WHEN p.seq IN (2, 4) THEN TRUE
        ELSE FALSE
    END,

    CASE
        WHEN p.tipo = 'Apartamento'
            THEN (
                SELECT c.id
                FROM seed_condominios c
                WHERE c.seq = p.seq
            )

        WHEN p.seq IN (2, 4)
            THEN (
                SELECT c.id
                FROM seed_condominios c
                WHERE c.seq = p.seq
            )

        ELSE NULL
    END,

    CASE
        WHEN p.tipo = 'Casa'
            THEN '89010-' || LPAD(p.seq::TEXT, 3, '0')

        WHEN p.tipo = 'Apartamento'
            THEN '89020-' || LPAD(p.seq::TEXT, 3, '0')

        ELSE
            '89030-' || LPAD((p.seq - 10)::TEXT, 3, '0')
    END,

    CASE
        WHEN p.tipo = 'Casa'
            THEN 'Rua das Acácias'

        WHEN p.tipo = 'Apartamento'
            THEN 'Rua das Palmeiras'

        ELSE
            'Rua dos Lotes'
    END,

    100 + p.seq,

    CASE
        WHEN p.tipo = 'Casa' THEN
            CASE
                WHEN p.seq % 2 = 0 THEN 'Velha'
                ELSE 'Fortaleza'
            END

        WHEN p.tipo = 'Apartamento' THEN
            CASE
                WHEN p.seq % 2 = 0 THEN 'Centro'
                ELSE 'Victor Konder'
            END

        ELSE
            CASE
                WHEN p.seq % 2 = 0 THEN 'Itoupava Norte'
                ELSE 'Itoupava Central'
            END
    END,

    'SC',

    'Blumenau',

    CASE
        WHEN p.tipo = 'Casa'
            THEN 'Próximo a comércio e escolas'

        WHEN p.tipo = 'Apartamento'
            THEN 'Próximo ao centro'

        ELSE NULL
    END,

    CASE
        WHEN p.seq = 1 THEN 450000.00
        WHEN p.seq = 2 THEN 2800.00
        WHEN p.seq = 3 THEN 620000.00
        WHEN p.seq = 4 THEN 3200.00
        WHEN p.seq = 5 THEN 790000.00

        WHEN p.seq = 6 THEN 350000.00
        WHEN p.seq = 7 THEN 2200.00
        WHEN p.seq = 8 THEN 420000.00
        WHEN p.seq = 9 THEN 2800.00
        WHEN p.seq = 10 THEN 580000.00

        WHEN p.seq = 11 THEN 280000.00
        WHEN p.seq = 12 THEN 1800.00
        WHEN p.seq = 13 THEN 350000.00
        WHEN p.seq = 14 THEN 2200.00
        WHEN p.seq = 15 THEN 420000.00
    END,

    CASE
        WHEN p.tipo = 'Apartamento' THEN 1200.00
        WHEN p.tipo = 'Casa' THEN 900.00
        ELSE 600.00
    END,

    CASE
        WHEN p.tipo = 'Apartamento'
            THEN 450.00

        WHEN p.seq IN (2, 4)
            THEN 350.00

        ELSE NULL
    END,

    CURRENT_TIMESTAMP,
    CURRENT_TIMESTAMP

FROM seed_imoveis p;

INSERT INTO imagens_imoveis (
    id,
    imovel_id,
    caminho,
    url,
    principal,
    criado_em,
    alterado_em
)
SELECT
    gen_random_uuid(),
    p.id,
    NULL,
    NULL,
    FALSE,
    CURRENT_DATE,
    NULL
FROM seed_imoveis p;


INSERT INTO casas (
    id,
    imovel_id,
    metragem,
    quartos,
    suites,
    banheiros,
    garagens,
    andares,
    salas,
    esta_mobiliado,
    mobilia,
    criado_em,
    alterado_em
)
SELECT
    gen_random_uuid(),
    p.id,

    100 + (p.seq * 12),

    2 + (p.seq % 3),

    CASE
        WHEN p.seq % 2 = 0 THEN 1
        ELSE 2
    END,

    2 + (p.seq % 2),

    1 + (p.seq % 3),

    CASE
        WHEN p.seq % 2 = 0 THEN 2
        ELSE 1
    END,

    2 + (p.seq % 2),

    CASE
        WHEN p.seq % 2 = 0
            THEN 'Semimobiliado'
        ELSE
            'Não'
    END,

    CASE
        WHEN p.seq % 2 = 0
            THEN ARRAY[
                'Cozinha planejada',
                'Armários nos quartos'
            ]::TEXT[]

        ELSE
            '{}'::TEXT[]
    END,

    CURRENT_TIMESTAMP,
    CURRENT_TIMESTAMP

FROM seed_imoveis p
WHERE p.tipo = 'Casa';


INSERT INTO apartamentos (
    id,
    imovel_id,
    metragem,
    quartos,
    suites,
    banheiros,
    garagens,
    andares,
    salas,
    esta_mobiliado,
    mobilia,
    criado_em,
    alterado_em
)
SELECT
    gen_random_uuid(),
    p.id,

    55 + (p.seq * 8),

    2 + (p.seq % 2),

    CASE
        WHEN p.seq % 2 = 0 THEN 1
        ELSE 0
    END,

    1 + (p.seq % 2),

    1 + (p.seq % 2),

    1,

    1 + (p.seq % 2),

    CASE
        WHEN p.seq % 2 = 0
            THEN 'Semimobiliado'
        ELSE
            'Não'
    END,

    CASE
        WHEN p.seq % 2 = 0
            THEN ARRAY[
                'Cozinha planejada',
                'Armários nos quartos'
            ]::TEXT[]

        ELSE
            '{}'::TEXT[]
    END,

    CURRENT_TIMESTAMP,
    CURRENT_TIMESTAMP

FROM seed_imoveis p
WHERE p.tipo = 'Apartamento';

INSERT INTO terrenos (
    id,
    imovel_id,
    area_total,
    medida_esquerda,
    medida_direita,
    medida_frente,
    medida_fundo,
    zoneamento,
    coeficiente,
    criado_em,
    alterado_em
)
SELECT
    gen_random_uuid(),
    p.id,

    300 + (p.seq * 25),

    25 + p.seq,

    25 + p.seq,

    12 + p.seq,

    12 + p.seq,

    CASE
        WHEN p.seq % 5 = 0 THEN 'Industrial'
        WHEN p.seq % 2 = 0 THEN 'Residencial'
        ELSE 'Comercial'
    END,

    1.5 + (p.seq * 0.1),

    CURRENT_TIMESTAMP,
    CURRENT_TIMESTAMP

FROM seed_imoveis p
WHERE p.tipo = 'Terreno';

