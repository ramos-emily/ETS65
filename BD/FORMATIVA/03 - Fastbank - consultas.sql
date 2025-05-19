/*---------------------------------------------
Banco: FastBank
--------------------------------------------*/
/* 
	select (Seleção) -> Atributos (colunas) que serão apresentados
	from (Origem) -> Tabela de referência para busca dos dados
	join (Junções) -> associações com outra(s) tabela(s) acrescentando dados para a consulta
	where (Filtros) -> Registros (linhas) que serão apresentados
	order by (Ordenações) e group by (Agrupamentos) -> Registros apresentados

	Cláusulas/ Argumentos:
	as - Apelidos (ALIas) para colunas
	if() - Substituição de valores em colunas
	like - Varredura em textos
	between - Faixa de valores/período
	limit() - Primeiros registros
	distinct - Registros sem repetição

	Funções de agregação (extração de informações únicas ou agrupadas de colunas)
	min()
	max()
	sum()
	avg()
	count()

	formatações de Data e hora
	Funções de cadeia de caracteres (textos)

*/


-- Conexão com o Banco
use Fastbank;


-- Consultas gerais
select * from cliente;
select * from clientePF;
select * from clientePJ;
select * from endereco;
select * from contato;
select * from cliente_conta;
select * from conta;
select * from cartao;
select * from movimentacao;
select * from emprestimo;
select * from emprestimo_parcela;
select * from investimento;


-- Todas as colunas e todas as linhas
select *
from Endereco;


-- Colunas selecionadas e todas as linhas
select logradouro,
       cidade
from Endereco;


-- Todas as colunas com filtros de registros
select *
from Endereco
where cidade = 'São Paulo';


-- Todas as colunas com filtros de registros
select *
from Endereco
where cidade <> 'São Paulo' and logradouro like 'Avenida%';


-- Alterar visualização de dados de uma coluna por meio de lógica
select agencia,
       numero,
	   if(ativa = 0, 'Inativa', 'Ativa')
from Conta;



-- Apelido (alias) para o titulo da coluna
select agencia as 'Agência',
       numero as 'Número',
	   if(ativa = 0, 'Inativa', 'Ativa') as 'Situação'
from Conta;


-- Filtrando registros por período
select valor_solicitado as "Valor solicitado",
       numero_parcelas as "Número de parcelas",
       data_solicitacao as "Data de solicitação"
from emprestimo
where data_solicitacao between "2022-12-01" and "2022-12-31";


-- Ordenação
select codigo_operacao,
	   data_hora,
       valor
from movimentacao
order by codigo_operacao, valor;



-- Filtro e Ordenação
select codigo_operacao as 'Código da operação',
       valor as 'Valor',
	   data_hora as 'Data e Hora'
from movimentacao
where valor between 1000 and 3000
order by codigo_operacao, valor desc;



-- Define quantos registros serão exibidos (os primeiros de acordo com a ordenação)
select codigo_operacao,
       valor
from movimentacao
order by valor desc
limit 3;



-- Elimina repetições
select distinct codigo_bandeira,
                situacao
from cartao;


select distinct codigo_bandeira
from cartao;


-- Funções de agregação
select min(valor) as 'Menor movimentação',
	   max(valor) as 'Maior movimentação',
	   sum(valor) as 'Soma total',
	   avg(valor) as 'Média aritmética',
	   count(valor) as 'Quantidade de movimentações'	
from movimentacao;


-- Agrupamentos (group by)
select codigo_cartao
from movimentacao
group by codigo_cartao;
        

select codigo_operacao
from movimentacao
group by codigo_operacao;


select codigo_cartao,
       codigo_operacao
from movimentacao
group by codigo_cartao, codigo_operacao;


-- Agrupamento e Agregação
select codigo_cartao,
       codigo_operacao,
	   count(*) as 'Quantidade de movimentações'
from movimentacao
group by codigo_cartao, codigo_operacao;


select codigo_operacao,
       min(valor) as 'Menor movimentação',
	   max(valor) as 'Maior movimentação',
	   sum(valor) as 'Soma total',
	   avg(valor) as 'Média aritmética',
	   count(valor) as 'Quantidade de movimentações'	
from movimentacao
group by codigo_operacao;


select codigo_cartao,
       min(valor) as 'Menor movimentação',
	   max(valor) as 'Maior movimentação',
	   sum(valor) as 'Soma total',
	   avg(valor) as 'Média aritmética',
	   count(valor) as 'Quantidade de movimentações'	
from movimentacao
group by codigo_cartao;


-- formatações

-- Data
select date_format(data_solicitacao, '%d/%m/%y') as 'Data de solicitação',
       date_format(data_solicitacao, '%d/%m/%Y') as 'Data de solicitação',
       date_format(data_solicitacao, '%d de %M de %Y') as 'Data de solicitação',
       date_format(data_solicitacao, '%W, %d de %M de %Y') as 'Data de solicitação'       
from emprestimo;

-- Hora
select time_format(data_hora, '%h:%i:%s') as 'Hora da movimentação',
       time_format(data_hora, '%h:%i:%s (%p)') as 'Hora da movimentação',
       time_format(data_hora, '%H:%i:%s') as 'Hora da movimentação',
       time_format(data_hora, '%r') as 'Hora da movimentação'       
from movimentacao;


-- Moeda
select format(valor_solicitado, '2', 'pt_BR') as 'Português Brasil',
       format(valor_solicitado, '2', 'de_DE') as 'German',
       format(valor_solicitado, '2', 'en_US') as 'US English'
from emprestimo;

select concat('R$ ', format(valor_solicitado, '2', 'pt_BR')) as 'Português Brasil'
from emprestimo;


-- Porcentagem
select juros as 'Como fração',
	   format(juros * 100, 2) as 'Como porcentagem',
       concat(format(juros * 100, 2), '%') as 'Como porcentagem'
from emprestimo;



-- Data e Hora

-- Retorna a data do servidor
select curdate() as 'Date',
	   curtime() as 'Time';

select current_date() as 'Date',
	   current_time() as 'Time',
       current_timestamp() as 'Timestamp';



select date_format(data_solicitacao, '%d/%m/%y') as 'Data de solicitação',
	   day(data_solicitacao) as 'Dia',	
	   month(data_solicitacao) as 'Mês',
	   year(data_solicitacao) as 'Ano'
from emprestimo;



-- Calcular diferença entre data
select datediff('2023-03-01','2023-03-27');


select timestampdiff(day,'2020-01-01',now()) as dias,
       timestampdiff(month,'2020-01-01',now()) as meses,
       timestampdiff(year,'2020-01-01',now()) as anos;



-- Manipulação de textos

-- Espaços em branco são considerados
update Cliente
set nome_razaoSocial = '   Jaime Câmara Valério'
where codigo = 10;


select * 
from Cliente
where nome_razaoSocial = 'Jaime Câmara Valério';


-- Retirar espaços em branco ante e depois de um texto
select * 
from Cliente
where trim(nome_razaoSocial) = 'Jaime Câmara Valério';


-- Retorna a quantidade de caracteres de um texto
select char_length(nome_razaoSocial)
from Cliente
where codigo = 10;


-- Combinações de funções (começa a execução de dentro pra fora)
select char_length( trim(nome_razaoSocial) )
from Cliente
where codigo = 10;


-- Retorna um quantidade pré-definida de caracteres a esquerda
select left(nome_razaoSocial, 10)
from Cliente
where codigo = 10;


-- Retorna um quantidade pré-definida de caracteres a direita
select right(nome_razaoSocial, 10)
from Cliente
where codigo = 10;


-- Pesquisa se um (ou mais) caracteres existem em um texto

update Cliente
set nome_razaoSocial = 'Jaime de Câmara Valério'
where codigo = 10;


select position('de' in nome_razaoSocial)
from Cliente
where codigo = 10;


select position(' ' in nome_razaoSocial)
from Cliente;


-- Retorna uma parte do texto
select substring(nome_razaoSocial, 10, 6)
from cliente
where codigo = 10;


select substring(nome_razaoSocial, 1, position(' ' in nome_razaoSocial))
from Cliente;

-- Todas as letras minusculas
select lower(nome_razaoSocial)
from cliente;


-- Todas as letras maiúsculas
select upper(nome_razaoSocial)
from cliente;


-- Concatenações
select concat(nome_razaoSocial,': ', trim(usuario), ' - ', senha)
from cliente;



/*------------------------------------------------------------------------------------------
Consultas em várias tabelas (exemplos com where para testes e compreensão do relacionamento)
------------------------------------------------------------------------------------------*/

-- Relacionamento 1:1
-- Envolvendo duas tabelas
--------------------------

-- ClientePF (todos os atributos)
select cli.nome_razaoSocial as 'Nome',
	   if(cli.nomesocial_fantasia IS NULL, 'Não informado', cli.nomesocial_fantasia) as 'Nome social',
	   cli.foto_logo as 'Foto',
	   date_format(cli.datanascimento_abertura, '%d/%m/%Y') as 'Data de nascimento',
	   cli.usuario,
	   cli.senha,
	   cli.codigo as 'PK de Cliente',
	   pf.codigo_cliente as 'PK e FK de ClientePF',
	   pf.rg as 'RG',
	   pf.cpf as 'CPF'
from cliente as cli, cliente_pf as pf
where cli.codigo = pf.codigo_cliente;


-- ClientePF (atributos selecionados)
select cli.nome_razaoSocial as 'Nome',
	   if(Cli.nomeSocial_fantasia IS NULL, 'Não informado', Cli.nomeSocial_fantasia) as 'Nome social',
	   Cli.foto_logo as 'Foto',
	   date_format(Cli.dataNascimento_abertura, '%d/%m/%Y') as 'Data de nascimento',
	   PF.rg as 'RG',
	   PF.cpf as 'CPF'
from cliente as cli, cliente_pf as pf
where cli.codigo = pf.codigo_cliente;



-- ClientePJ (todos os atributos)
select Cli.nome_razaosocial as 'Razao social',
	   Cli.nomesocial_fantasia as 'Nome fantasia',
	   Cli.foto_logo as 'Logo',
	   date_format(Cli.dataNascimento_abertura, '%d/%m/%Y') as 'Data de abertura',
	   Cli.usuario,
	   Cli.senha,
	   Cli.codigo as 'PK de Cliente',
	   PJ.codigo_cliente as 'PK e FK de ClientePJ',
	   PJ.cnpj as 'CNPJ',
	   PJ.inscricao_municipal as 'IM',
	   PJ.inscricao_estadual as 'IE'
from Cliente as cli, cliente_pj as pj
where Cli.codigo = pj.codigo_cliente;


-- ClientePJ (atributos selecionados)
select cli.nome_razaosocial as 'Razao social',
	   if(cli.nomesocial_fantasia is null, 'Não informado', Cli.nomeSocial_fantasia) as 'Nome fantasia',
	   cli.foto_logo as 'Logo',
	   date_format(cli.dataNascimento_abertura, '%d/%m/%Y') as 'Data de abertura',
	   PJ.cnpj as 'CNPJ',
	   PJ.inscricao_municipal as 'IM',
	   if(PJ.inscricao_estadual IS NULL, '', pj.inscricao_estadual) as 'IE'
from cliente as Cli, cliente_pj as pj
where cli.codigo = pj.codigo_cliente;



-- Relacionamento 1:n
-- Envolvendo três tabelas
--------------------------

-- todos os atributos
select Cli.nome_razaosocial as 'Nome',
	   if(Cli.nomesocial_fantasia IS NULL, 'Não informado', Cli.nomeSocial_fantasia)as 'Nome social',
	   Cli.foto_logo as 'Foto',
	   date_format(Cli.dataNascimento_abertura, '%d/%m/%Y') as 'Data de nascimento',
	   Cli.usuario,
	   Cli.senha,
	   Cli.codigo as 'PK de Cliente',
	   PF.codigo_cliente as 'PK e FK de ClientePF',
	   PF.rg as 'RG',
	   PF.cpf as 'CPF',
	   Cli.codigo_endereco as 'FK em Cliente',
	   E.codigo as 'PK de Endereco',
	   E.logradouro,
	   E.bairro,
	   E.cidade,
	   E.uf,
	   E.cep
from Cliente as cli, 
     Cliente_pf as pf,
	 Endereco as e
where Cli.codigo = PF.codigo_cliente
  and Cli.codigo_endereco = e.codigo;


-- Atributos selecionados
select Cli.nome_razaoSocial as 'Nome',
	   if(Cli.nomeSocial_fantasia IS NULL, 'Não informado', Cli.nomeSocial_fantasia) as 'Nome social',
	   Cli.foto_logo as 'Foto',
	   date_format(Cli.dataNascimento_abertura, '%d/%m/%Y') as 'Data de nascimento',
	   PF.rg as 'RG',
	   PF.cpf as 'CPF',
	   E.logradouro as 'Rua',
	   E.bairro,
	   E.cidade,
	   E.uf
from Cliente as Cli, 
     Cliente_pf as PF,
	 Endereco as e
where Cli.codigo = PF.codigo_cliente
  and Cli.codigo_endereco = e.codigo
order by Cli.codigo;


/*-------------------------------------------
Inserção de registros em tabelas dependentes
--------------------------------------------*/

-- select * from Endereco
-- select * from Cliente
-- select * from ClientePF

-- Primeiro a inserção na tabela que será referenciada
INSERT INTO Cliente
VALUES (2, 'Fernanda Ribeiro Souza', 'Fernanda Ribeiro', '\foto\123.jpg','1989-03-30','fernanda', 654);

-- Obtenção do codigo gerado
select max(codigo) from Cliente;

-- Inserção do complemento dos dado do ClientePF
INSERT INTO Cliente_PF
VALUES (10, '48996867900', '264125892');


-- Envolvendo quatro tabelas
----------------------------

-- Todos os atributos
select Cli.nome_razaoSocial as 'Nome',
	   if(Cli.nomeSocial_fantasia IS NULL, 'Não informado', Cli.nomeSocial_fantasia) as 'Nome social',
	   Cli.foto_logo as 'Foto',
	   date_format(Cli.dataNascimento_abertura, '%d/%m/%Y') as 'Data de nascimento',
	   Cli.usuario,
	   Cli.senha,
	   Cli.codigo as 'PK de Cliente',
	   PF.codigo_cliente as 'PK e FK de ClientePF',
	   PF.rg as 'RG',
	   PF.cpf as 'CPF',
	   Cli.codigo_endereco as 'FK em Cliente',
	   E.codigo as 'PK de Endereco',
	   E.logradouro,
	   E.bairro,
	   E.cidade,
	   E.uf,
	   E.cep,
	   Cli.codigo as 'PK de Cliente',
	   Con.codigo_cliente as 'FK em Contato',
	   Con.numero,
	   Con.ramal,
	   Con.email,
	   Con.observacao
from Cliente as Cli, 
     Cliente_pf as pf,
	 Endereco as E,
	 Contato as Con
where Cli.codigo = PF.codigo_cliente
  and Cli.codigo_endereco = E.codigo
  and Cli.codigo = Con.codigo_cliente;


-- Atributos selecionados
select Cli.nome_razaoSocial as 'Nome',
	   if(Cli.nomeSocial_fantasia IS NULL, 'Não informado', Cli.nomeSocial_fantasia) as 'Nome social',
	   Cli.foto_logo as 'Foto',
	   date_format(Cli.dataNascimento_abertura, '%d/%m/%Y') as 'Data de nascimento',
	   PF.rg as 'RG',
	   PF.cpf as 'CPF',
	   E.logradouro,
	   E.bairro,
	   E.cidade,
	   E.uf,
	   Con.numero,
	   if(Con.ramal IS NULL, '', Con.ramal),
	   if(Con.email IS NULL, '', Con.email)
from Cliente as Cli, 
     Cliente_pf as pf,
	 Endereco as E,
	 Contato as Con
where Cli.codigo = PF.codigo_cliente
  and Cli.codigo_endereco = E.codigo
  and Cli.codigo = Con.codigo_cliente
order by Nome;


---------------------------------------------------------------------------------
-- JOINs (Junções)

-- ClientePJ (todos os atributos)
select Cli.nome_razaoSocial as 'Razao social',
	   Cli.nomeSocial_fantasia as 'Nome fantasia',
	   Cli.foto_logo as 'Logo',
	   date_format(Cli.dataNascimento_abertura, '%d/%m/%Y') as 'Data de abertura',
	   Cli.usuario,
	   Cli.senha,
	   Cli.codigo as 'PK de Cliente',
	   PJ.codigo_cliente as 'PK e FK de ClientePJ',
	   PJ.cnpj as 'CNPJ',
	   PJ.inscricao_municipal as 'IM',
	   PJ.inscricao_estadual as 'IE'
from Cliente as Cli 
inner join Cliente_pj as pj ON Cli.codigo = PJ.codigo_cliente;


-- ClientePJ (atributos selecionados)
select Cli.nome_razaoSocial as 'Razao social',
	   if(Cli.nomeSocial_fantasia IS NULL, 'Não informado', Cli.nomeSocial_fantasia) as 'Nome fantasia',
	   Cli.foto_logo as 'Logo',
	   date_format(Cli.dataNascimento_abertura, '%d/%m/%Y') as 'Data de abertura',
	   PJ.cnpj as 'CNPJ',
	   PJ.inscricao_municipal as 'IM',
	   if(PJ.inscricao_estadual IS NULL, '', PJ.inscricao_estadual) as 'IE'
from Cliente as Cli 
INNER JOIN Cliente_pj as PJ ON Cli.codigo = PJ.codigo_cliente
where PJ.inscricao_estadual IS NOT NULL
order by Cli.nome_razaoSocial;



-- ClientePF (todos os atributos)
select Cli.nome_razaoSocial as 'Nome',
	   if(Cli.nomeSocial_fantasia IS NULL, 'Não informado', Cli.nomeSocial_fantasia)as 'Nome social',
	   Cli.foto_logo as 'Foto',
	   date_format(Cli.dataNascimento_abertura, '%d/%m/%Y') as 'Data de nascimento',
	   Cli.usuario,
	   Cli.senha,
	   Cli.codigo as 'PK de Cliente',
	   PF.codigo_cliente as 'PK e FK de ClientePF',
	   PF.rg as 'RG',
	   PF.cpf as 'CPF'
from Cliente as Cli 
inner join Cliente_pf as PF ON Cli.codigo = PF.codigo_cliente;



-- ClientePF (atributos selecionados)
select Cli.nome_razaoSocial as 'Nome',
	   if(Cli.nomeSocial_fantasia IS NULL, 'Não informado', Cli.nomeSocial_fantasia) as 'Nome social',
	   Cli.foto_logo as 'Foto',
	   date_format(Cli.dataNascimento_abertura, '%d/%m/%Y') as 'Data de nascimento',
	   PF.rg as 'RG',
	   PF.cpf as 'CPF'
from Cliente as Cli
inner join Cliente_PF as PF ON Cli.codigo = PF.codigo_Cliente
where dataNascimento_abertura between '1990-01-01' and '1999-12-31'
order by Cli.dataNascimento_abertura;

