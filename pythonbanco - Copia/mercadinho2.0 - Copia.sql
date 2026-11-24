CREATE TABLE IF NOT EXISTS cliente (
    id_cliente SERIAL PRIMARY KEY,
    nome VARCHAR(255)not null,
    telefone VARCHAR(11) UNIQUE,
    email VARCHAR(255) UNIQUE NOT null,
    password VARCHAR(200) not null 
);

CREATE TABLE IF NOT EXISTS funcionarios (
    id_funcionario SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    cargo VARCHAR(150) NOT null,
    cpf varchar(14) unique not null,
    email varchar(255) unique,
    password varchar(255) not null
);

CREATE TABLE IF NOT EXISTS produto (
    id_produto SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    quantidade_estoque INTEGER
);

CREATE TABLE IF NOT EXISTS fornecedor (
    id_fornecedor SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    telefone VARCHAR(11) UNIQUE NOT NULL,
    id_produto INTEGER REFERENCES produto(id_produto)
);

CREATE TABLE IF NOT EXISTS venda (
    id_venda SERIAL PRIMARY KEY,
    data TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    valor_total NUMERIC(10,2) NOT NULL,
    id_cliente INTEGER REFERENCES cliente(id_cliente),
    id_funcionario INTEGER REFERENCES funcionarios(id_funcionario)
);

CREATE TABLE IF NOT EXISTS item_venda (
    id_item SERIAL PRIMARY KEY,
    quantidade INTEGER NOT NULL,
    preco_unitario NUMERIC(10,2),
    id_venda INTEGER REFERENCES venda(id_venda) ON DELETE CASCADE,
    id_produto INTEGER REFERENCES produto(id_produto)
);



