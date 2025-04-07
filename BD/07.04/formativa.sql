/*____________________________________
Banco: FastBank
-------------------------------------*/

-- Criação do banco de dados
create database formativa_2;

-- conexão do banco
USE formativa_2;

create table cliente (
	id_cliente int primary key auto_increment,
    rg varchar(15) not null,
    cpf varchar(15) not null,
    nome varchar(100) not null,
    cnh varchar(15) not null,
    data_nascimento date not null,
    logradouro varchar(100) not null,
    bairro varchar(100) not null,
    cidade varchar(100) not null,
    uf enum('AC', 'AL', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'SP'),
    cep varchar(10) not null
);

create table categoria (
	id_categoria int primary key auto_increment, 
    nome_categoria varchar(50) not null,
    preco_diaria decimal(10,2) not null,
    descricao text
);

create table veiculo (
	id_veiculo int primary key auto_increment,
    chassi varchar(50) not null,
    placa varchar(10) not null,
    marca varchar(50) not null,
    modelo varchar(50) not null,
    ano_fabricacao int,
    ano_modelo int,
    cor_predominante varchar(30),
    id_categoria int,
    foreign key (id_categoria) references categoria(id_categoria)
);

create table locacao (
	id_locacao int primary key auto_increment,
    id_veiculo int,
    id_cliente int,
    data_hora_locacao datetime not null,
    data_hora_devolucao datetime,
	foreign key (id_cliente) references cliente(id_cliente),
	foreign key (id_veiculo) references veiculo(id_veiculo)
);

create table manutencao (
	id_manutencao int primary key auto_increment,
    id_veiculo int,
    data_manutencao date not null,
    valor_pago decimal(10,2) not null,
    descricao_servico text,
    nome_oficina varchar(100),
	foreign key (id_veiculo) references veiculo(id_veiculo)
);

insert into cliente
	(rg, cpf, nome, logradouro, bairro, cidade, cep, uf, cnh, data_nascimento)
values
	('123456789', '111.111.111-11', 'Vikitor Souza', 'Rua A, 123', 'itajai', 'Campinas', '13058020', 'AC', 'CNH12345', '2005-07-10'),
	('234567890', '222.222.222-22', 'Gaybriel Bosco', 'Rua B, 456', 'sao bento', 'Hortocity', '13058021', 'CE', 'CNH67890', '2005-07-02'),
	('012345678', '333.333.333-33', 'Paula tejano', 'Rua C, 789',  'Bassoli', 'Campinas', '13058025', 'DF', 'CNH01234', '2006-11-18');
    
    
select * from cliente;    
    
insert into categoria
	(nome_categoria, preco_diaria, descricao)
values
	('Economico', 100.00, 'Carros populares, baixo consumo de combustivel'),
    ('SUV', 300.00, 'Carros desbundado'),
    ('Sedan', 300.00, 'Carro com bunda');
  
select * from categoria;      
  
insert into veiculo
	(chassi, placa, marca, modelo, ano_fabricacao, ano_modelo, cor_predominante, id_categoria)
values
	('9BD111060T5002156', 'ABC1A23', 'BMW', 'M3-Mcompetiton', 2024, 2025, 'black piano', 1),
    ('9BD111060T5002157', 'ABC1A24', 'Honda', 'Civic', 2017, 2018, 'black', 2),
    ('9BD111060T5002158', 'ABC1A25', 'Porsche', 'Macan', 2015, 2023, 'white', 3);
    
select * from veiculo;        
    
insert into locacao
	(id_cliente, id_veiculo, data_hora_locacao, data_hora_devolucao)
values
	(1, 1, '2025-04-01 10:00:00', '2025-04-03 12:00:00'),
    (1, 1, '2025-05-01 12:00:00', '2025-05-03 14:00:00'),
    (1, 1, '2025-06-01 14:00:00', '2025-06-03 16:00:00');

select * from locacao;    

insert into manutencao
	(id_veiculo, data_manutencao, valor_pago, descricao_servico, nome_oficina)
values
	(1, '2025-03-01', 500.00, 'Troca de oleo', 'fueltech'),
    (2, '2025-04-01', 900.00, 'Trocar scape', 'Oficina do tião'),
	(3, '2025-05-01', 690.00, 'Trocar disco de Freio', 'Oficina do Vikitor');
    
select * from manutencao;    
    