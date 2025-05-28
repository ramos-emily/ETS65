/*----------------------------------------------------------------------
Banco: fastbank
Autor: Ralfe
-----------------------------------------------------------------------*/
/*
Documentação:
--> create database 
    (https://dev.mysql.com/doc/refman/8.0/en/creating-database.html)
    --> InnoDB and MyISAM
        (https://dev.mysql.com/doc/refman/8.0/en/index-statistics.html)
--> create table 
    (https://dev.mysql.com/doc/refman/8.0/en/create-table.html)
--> alter table (add, change, drop) 
    (https://dev.mysql.com/doc/refman/8.0/en/alter-table.html)
	Exemplos:
		alter table ClientePJ add regiao varchar(100);
		alter table ClientePJ drop column inscricaoMunicipal;
		alter table ClientePJ change cnpj cnpj varchar(100);
--> drop table
	(https://dev.mysql.com/doc/refman/8.0/en/drop-database.html)
	(https://dev.mysql.com/doc/refman/8.0/en/drop-table.html)
--> Constraints
		primary key (https://dev.mysql.com/doc/refman/8.0/en/primary-key-optimization.html)
		foreign key (https://dev.mysql.com/doc/refman/8.0/en/create-table-foreign-keys.html)
		unique (https://dev.mysql.com/doc/refman/8.0/en/constraint-primary-key.html)
		check (https://dev.mysql.com/doc/refman/8.0/en/create-table-check-constraints.html)
		default (https://dev.mysql.com/doc/refman/8.0/en/data-type-defaults.html)
        enum (https://dev.mysql.com/doc/refman/8.0/en/enum.html)
--> update e delete cascade
	(https://dev.mysql.com/doc/refman/8.0/en/ansi-diff-foreign-keys.html)

*/
-- Criação do banco
create database fastbank;

-- Conecta no banco
use fastbank;

-- Criação de tabelas

-- Entidades fracas
/*
	ContaTipo
	Bandeira
	Operacao
	InvestimentoTipo
	GrauRisco
	TipoImovel
*/

create table conta_tipo(
	codigo int auto_increment,
    descricao varchar(100) not null,
    constraint pk_contatipo primary key (codigo)
);

create table bandeira(
	codigo int auto_increment,
    descricao varchar(100) not null,
    constraint pk_bandeira primary key (codigo)
);

create table operacao(
	codigo int auto_increment,
    descricao varchar(100) not null,
    constraint pk_operacao primary key (codigo)
);

create table investimento_tipo(
	codigo int auto_increment,
    modalidade varchar(50) not null,
    sigla varchar(20) not null,
    descricao varchar(100) not null,
    constraint pk_investimentotipo primary key (codigo)
);

create table investimento_grau_risco(
	codigo int auto_increment,
    sigla varchar(20) not null,
    descricao varchar(100) not null,
    constraint pk_graurisco primary key (codigo)
);

create table imovel_tipo(
	codigo int auto_increment,
    descricao varchar(100) not null,
    constraint pk_imoveltipo primary key (codigo)
);

-- Entidades sem chave estrangeira
/*
	Endereco
    Cobertura
    Servico
*/

create table endereco(
	codigo int auto_increment,
    logradouro varchar(100) not null,
    bairro varchar(75) not null,
    cep char(10) not null,
    cidade varchar(75) not null,
    uf char(2),
    constraint chk_endereco_uf check (uf = 'AC' or
                                      uf = 'AL' or
                                      uf = 'AM' or
                                      uf = 'AP' or
                                      uf = 'BA' or
                                      uf = 'CE' or
                                      uf = 'DF' or
                                      uf = 'ES' or
                                      uf = 'GO' or
                                      uf = 'MA' or
                                      uf = 'MT' or
                                      uf = 'MS' or
                                      uf = 'MG' or
                                      uf = 'PA' or
                                      uf = 'PB' or
                                      uf = 'PR' or
                                      uf = 'PE' or
                                      uf = 'PI' or
                                      uf = 'RJ' or
                                      uf = 'RN' or
                                      uf = 'RS' or
                                      uf = 'RO' or
                                      uf = 'RR' or
                                      uf = 'SC' or
                                      uf = 'SP' or
                                      uf = 'SE' or
                                      uf = 'TO'),
    constraint pk_endereco primary key (codigo)
);

create table cobertura(
	codigo int auto_increment,
    descricao varchar(100) not null,
    constraint pk_cobertura primary key (codigo)
);

create table servico(
	codigo int auto_increment,
    descricao varchar(100) not null,
    constraint pk_servico primary key (codigo)
);

-- Entidades com chave estrangeira
/*
	Cliente
    ClientePF
    ClientePJ
    Contato
    Conta
    Cartao
    Movimentacao
    Investimento
    Emprestimo
    EmprestimoParcela
    Seguro
    SeguroPagamento
    Imovel
    Sinistro
*/

create table cliente(
	codigo int auto_increment,
    codigo_endereco int not null,
    nome_razaosocial varchar(100) not null,
    nomesocial_fantasia varchar(100),
    foto_logo varchar(100) not null,
    datanascimento_abertura date not null,
    usuario char(10) not null,
    senha int not null,
    constraint pk_cliente primary key (codigo),
    constraint uk_cliente unique (usuario),
    constraint chk_cliente_senha check (senha >= 000000 and senha <= 999999),
    constraint fk_cliente_endereco foreign key (codigo_endereco) references endereco (codigo)
);

create table cliente_pf(
	codigo_cliente int,
    rg varchar(20) not null,
    cpf varchar(20) not null,
    constraint pk_clientepf primary key (codigo_cliente),
    constraint uk_clientepf unique (rg, cpf),
    constraint fk_clientepf_cliente foreign key (codigo_cliente) references cliente (codigo)
);

create table cliente_pj(
	codigo_cliente int,
    cnpj varchar(50) not null,
    inscricao_municipal varchar(50) not null,
    inscricao_estadual varchar(50),
    constraint pk_clientepj primary key (codigo_cliente),
    constraint uk_clientepj unique (cnpj, inscricao_municipal, inscricao_estadual),
    constraint fk_clientepj_cliente foreign key (codigo_cliente) references cliente (codigo)
);

create table contato(
	codigo int auto_increment,
    codigo_cliente int not null,
    ddd char(3) not null,
    numero varchar(10) not null,
    ramal varchar(10),
    email varchar(50),
    observacao varchar(50),
    constraint pk_contato primary key (codigo),
    constraint fk_contato_cliente foreign key (codigo_cliente) references cliente (codigo) 
    on update cascade
    on delete cascade
);

create table conta(
	codigo int auto_increment,
    codigo_conta_tipo int not null,
    agencia varchar(10) not null,
    numero varchar(20) not null,
    limite decimal(10,2) not null,
	ativa bool default true,
    constraint pk_conta primary key (codigo),
	constraint fk_conta_contatipo foreign key (codigo_conta_tipo) references conta_tipo (codigo)    
);

create table cartao(
	codigo int auto_increment,
    codigo_conta int not null,
    codigo_bandeira int not null,
    numero varchar(30) not null,
    cvv char(5) not null,
    validade date not null,
    situacao varchar(20) default 'bloqueado',
    constraint pk_cartao primary key (codigo),
    constraint chk_cartao_situacao check (situacao = 'ativo' or situacao = 'bloqueado' or situacao = 'vencido'),
    constraint fk_cartao_conta foreign key (codigo_conta) references conta (codigo),
    constraint fk_cartao_bandeira foreign key (codigo_bandeira) references bandeira (codigo)    
);

create table movimentacao(
	codigo int auto_increment,
    codigo_cartao int not null,
    codigo_operacao int not null,
    codigo_conta_destino int,
    data_hora datetime not null,
    valor decimal(10,2) not null,
    constraint pk_cartao primary key (codigo),
    constraint fk_movimentacao_cartao foreign key (codigo_cartao) references cartao (codigo),
    constraint fk_movimentacao_operacao foreign key (codigo_operacao) references operacao (codigo)
);

create table investimento(
	codigo int auto_increment,
    codigo_conta int not null,
    codigo_investimento_tipo int not null,
    codigo_grau_risco int not null,
    aporte decimal(10,2) not null,
    prazo varchar(20) not null,
    rentabilidade decimal(10,2),
    taxa_administracao float not null,
    finalizado bool default false,
    constraint pk_investimento primary key (codigo),
    constraint chk_investimento_prazo check (prazo = 'curto' or prazo = 'médio' or prazo = 'longo'),
    constraint fk_investimento_conta foreign key (codigo_conta) references conta (codigo),
    constraint fk_investimento_investimentotipo foreign key (codigo_investimento_tipo) references investimento_tipo (codigo),
    constraint fk_investimento_investimentograurisco foreign key (codigo_grau_risco) references investimento_grau_risco (codigo)
);

create table emprestimo(
	codigo int auto_increment,
    codigo_conta int not null,
    valor_solicitado decimal(10,2),
    data_solicitacao date not null,
    aprovado bool not null,
    juros float not null,
    data_aprovacao date,
    numero_parcelas int,
    observacao varchar(200),
    constraint pk_emprestimo primary key (codigo),
    constraint fk_emprestimo_conta foreign key (codigo_conta) references conta (codigo)
);

create table emprestimo_parcela(
	codigo int auto_increment,
    codigo_emprestimo int not null,
    numero int not null,
    valor_parcela decimal(10,2) not null,
    data_vencimento date not null,
    valor_pago decimal(10,2),
    data_pagamento date,
    constraint pk_emprestimoparcela primary key (codigo),
    constraint fk_emprestimoparcela_emprestimo foreign key (codigo_emprestimo) references emprestimo (codigo)
);

create table seguro(
	codigo int auto_increment,
    codigo_conta int not null,
	descricao varchar(50),
    constraint pk_seguro primary key (codigo),
    constraint fk_seguro_conta foreign key (codigo_conta) references conta (codigo)
);

create table seguro_pagamento(
	codigo int auto_increment,
    codigo_seguro int not null,
    quantidade_parcelas int not null,
    numero_parcela int not null,
    valor_total decimal(10,2) not null,
    data_vencimento date not null,
    valor_pago decimal(10,2),
    data_pagamento date,
    constraint pk_seguropagamento primary key (codigo),
    constraint fk_seguropagamento_seguro foreign key (codigo_seguro) references seguro (codigo)
);

create table imovel(
	codigo int auto_increment,
    codigo_seguro int not null,
    codigo_imovel_tipo int not null,
    codigo_endereco int not null,
    valor decimal(10,2) not null,
    constraint pk_imovel primary key (codigo),
    constraint fk_imovel_seguro foreign key (codigo_seguro) references seguro (codigo),
    constraint fk_imovel_imovelTipo foreign key (codigo_imovel_tipo) references imovel_tipo (codigo)
);

create table sinistro(
	codigo int auto_increment,
    codigo_imovel int not null,
    data_abertura date not null,
    descricao varchar(300) not null,
    indenizacao decimal(10,2) not null,
    data_finalizacao date not null,
    constraint pk_sinistro primary key (codigo),
    constraint fk_sinistro_imovel foreign key (codigo_imovel) references imovel (codigo)
);

-- Entidades associativas (tabelas de relacionamento n:n)
/*
	ClienteConta
    SeguroCobertura
    SeguroServico
    SinistroCobertura
    SinistroServico
*/

create table cliente_conta(
	codigo_cliente int,
    codigo_conta int,
    constraint pk_clienteconta primary key (codigo_cliente, codigo_conta),
    constraint fk_clienteconta_cliente foreign key (codigo_cliente) references cliente (codigo),
    constraint fk_clienteconta_conta foreign key (codigo_conta) references conta (codigo)
);

create table seguro_cobertura(
	codigo_seguro int,
    codigo_cobertura int,
    constraint pk_segurocobertura primary key (codigo_seguro, codigo_cobertura),
    constraint fk_segurocobertura_seguro foreign key (codigo_seguro) references seguro (codigo),
    constraint fk_segurocobertura_cobertura foreign key (codigo_cobertura) references cobertura (codigo)
);

create table seguro_servico(
	codigo_seguro int,
    codigo_servico int,
    constraint pk_seguroservico primary key (codigo_seguro, codigo_servico),
    constraint fk_seguroservico_seguro foreign key (codigo_seguro) references seguro (codigo),
    constraint fk_seguroservico_servico foreign key (codigo_servico) references servico (codigo)
);

create table sinistro_cobertura(
	codigo_sinistro int,
    codigo_cobertura int,
    constraint pk_sinistrocobertura primary key (codigo_sinistro, codigo_cobertura),
    constraint fk_sinistrocobertura_sinistro foreign key (codigo_sinistro) references sinistro (codigo),
    constraint fk_sinistrocobertura_cobertura foreign key (codigo_cobertura) references cobertura (codigo)
);

create table sinistro_servico(
	codigo_sinistro int,
    codigo_servico int,
    constraint pk_sinistroservico primary key (codigo_sinistro, codigo_servico),
    constraint fk_sinistroservico_sinistro foreign key (codigo_sinistro) references sinistro (codigo),
    constraint fk_sinistroservico_servico foreign key (codigo_servico) references servico (codigo)
);

-- Inserções iniciais em tabelas/entidade fracas

-- ContaTipo
insert into conta_tipo (descricao)
values ('corrente');

-- Verifica resultado
select * from conta_tipo;


insert into conta_tipo (descricao)
values ('poupanca'),
       ('investimento');
       
-- Verifica resultado
select * from conta_tipo;


-- Bandeira
insert into bandeira (descricao)
values ('Visa'),
       ('Master Card'),
       ('Elo'),
       ('Americam Express');

-- Verifica resultado       
select * from bandeira;


-- Operacao
insert into operacao (descricao)
values ('Crédito'),
       ('Débito'),
       ('Transferência');

-- Verifica resultado       
select * from operacao;


-- InvestimentoTipo
insert into investimento_tipo (modalidade, sigla, descricao)
values ('Renda fixa', 'CDB', 'Certificados de Depósitos bancários'),
	   ('Renda fixa', 'TTD', 'Titulos do Tesouro Direto'),
	   ('Renda fixa', 'LCI', 'Letras de Crédito'),
       ('Renda fixa', 'LCA', 'Letras de Crédito'),
       ('Renda variável', 'Ações', 'Ações empresariais'),
       ('Renda variável', 'Cotas', 'Cotas de Fundos Imobiliários');

-- Verifica resultado       
select * from investimento_tipo;

-- GrauRisco
insert into investimento_grau_risco (sigla, descricao)
values ('AAA', 'Prime'),
       ('AA-', 'Elevado'),
       ('AA', 'Elevado'),
       ('AA+', 'Elevado'),
       ('A-', 'Médio elevado'),
       ('A', 'Médio elevado'),
       ('A+', 'Médio elevado'),
       ('BBB-', 'Médio baixo'),
       ('BBB', 'Médio baixo'),       
       ('BBB+', 'Médio baixo'),       
       ('BB-', 'Especulativo'),       
       ('BB', 'Especulativo'),       
       ('BB+', 'Especulativo'),       
	   ('B-', 'Altamente especulativo'),       
	   ('B', 'Altamente especulativo'),              
	   ('B+', 'Altamente especulativo'),              
	   ('CCC-', 'Risco substancial'),              
	   ('CCC', 'Risco substancial'),              
       ('CCC+', 'Risco substancial');              

-- Verifica resultado
select * from investimento_grau_risco;
		
-- ImovelTipo
insert into imovel_tipo (descricao)
values ('Casa'),
       ('Apartamento'),
       ('Chacara'),
       ('Sitio'),
       ('Sala comercial');

-- Verifica resultado
select * from imovel_tipo;