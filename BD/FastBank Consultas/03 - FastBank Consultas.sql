/* Estrutura da instrtução select

	select (seleção) -> Atributos (colunas) que serão apresentadas
    from (origem) -> Tabela de referencia para bsuca dos dados
    where (filtros) -> Registro (linhas) que serao apresentadas
    order by ()
*/











use fastbank;


select * 
from cliente; 

select nome_razaosocial,usuario
from cliente;


select nome_razaosocial as nome, -- apelidando as colunas
usuario as Usuário
from cliente;

select * 
from endereco
where cidade = 'São Paulo';

select * from endereco
-- <> esse sinal é o sinal de diferente
where cidade <> 'São Paulo'; -- filtrando todos os logradoruos que não é da cidade de são paulo

select * from endereco 
where logradouro like 'Avenida%'; -- Procurando na tabela endereco no registro logradouro se tem um resgistro com Aveinida no início

select * 
from endereco
where cidade like '%Paulo'; -- aqui é ao contrarío,Procurando na tabela endereco,na parte de cidade um registro que possui Paulo no final

select * from endereco
where bairro like '%dim %'; -- Procurando na tabela endereco na ´parte do bairro um registro que contém no meio da palavra - dim

select agencia as Agência,
numero as Número,
if (ativa = 0, 'Inativa','Ativa') as Status -- usando if para visualizar as contas inativas e ativas
from conta;

select  valor_solicitado as 'Valor Solicitado', -- para dar apelidos para campos que são nomeados com mais de duas palavras precisa colocar as aspas
		numero_parcelas as 'Numero de Parcelas',
        data_solicitacao as 'Data de Solicitação'
from emprestimo
where data_solicitacao > '2022-12-01';

select  valor_solicitado as 'Valor Solicitado', -- para dar apelidos para campos que são nomeados com mais de duas palavras precisa colocar as aspas
		numero_parcelas as 'Numero de Parcelas',
        data_solicitacao as 'Data de Solicitação'
from emprestimo
where data_solicitacao > '2022-12-01' and data_solicitacao < '2022-12-11'; -- pesquisando com critério

select  valor_solicitado as 'Valor Solicitado', -- para dar apelidos para campos que são nomeados com mais de duas palavras precisa colocar as aspas
		numero_parcelas as 'Numero de Parcelas',
        data_solicitacao as 'Data de Solicitação'
from emprestimo
where data_solicitacao between '2022-12-01' and  '2022-12-11'; -- usando between que é entre 2 duas datas


select codigo_operacao as 'Código de Operação',
	valor
from movimentacao
where valor between 1000 and 3000;


select codigo_operacao as 'Código de Operação',
	   valor
from movimentacao
where valor between 1000 and 3000
order by valor; -- ordenando a coluna para ordem crescente

select codigo_operacao as 'Código de Operação',
	valor
from movimentacao
where valor between 1000 and 3000
order by valor desc; -- ordenando a coluna para ordem decrescente

select codigo_operacao as 'Código de Operação',
	valor
from movimentacao
where valor between 1000 and 3000
order by codigo_operacao, valor desc; -- ordenando a duas colunas e fazendo quebras de valores para decresente


select codigo_operacao as 'Código de Operação',
	valor
from movimentacao
where valor between 1000 and 3000
order by valor  -- ordenando valor pela ordem cresente
limit 3; -- trazendo as 3 menores e so funciiona com o order by



select codigo_operacao as 'Código de Operação',
	valor
from movimentacao
where valor between 1000 and 3000
order by valor desc -- ordenando a coluna valor para ordem decresente
limit 3; -- trazendo as 3 maiores e so funciiona com o order by


select distinct codigo_bandeira as 'Codigo da Bandeira', -- traz um resgistro de cada código,ele elimina as redundanças
		situacao as 'Situação'
from cartao
order by codigo_bandeira;

-- Funções de agregação 

select max(valor) as 'Menor movimentação',
		min(valor) as 'Maior movimentação',
        sum(valor) as 'Total de movimentações',
        avg(valor) as 'Médias de movimentações',
        count(valor) as 'Quantidade de movimentações'
from movimentacao; -- Trouxe o valor máximo da tabela valor 

-- Agrupamentos (group by)
select codigo_cartao as 'Código do cartão',
		codigo_operacao as 'Código da operação',
		sum(valor) as 'Total de movimentações por cartão'
from movimentacao
group by codigo_cartao, codigo_operacao
order by codigo_cartao;


select max(valor) as 'Menor movimentação',
		min(valor) as 'Maior movimentação',
        sum(valor) as 'Total de movimentações',
        avg(valor) as 'Médias de movimentações',
        count(valor) as 'Quantidade de movimentações'
from movimentacao -- Trouxe o valor máximo da tabela valor 
group by codigo_operacao;

-- Formatações

-- Moeda 
select format(valor_solicitado, '2', 'pt_BR' ) as 'Português Brazil',
		format(valor_solicitado, '2', 'de_DE') as 'German',
        format(valor_solicitado, '2', 'en_US') as 'US Engilsh'
from emprestimo;
-- Porcentagem
select juros as 'Como fração',
	format(juros * 100, '2') as 'Como inteiro',
    concat(format(juros * 100, '2'), '%') as 'Como porcentagem'
from emprestimo;

-- Data
select date_format(data_solicitacao, '%d/%m/%y') as 'Data abrevidada',
		date_format(data_solicitacao, '%d/%m/%Y') as 'Data abrevida(com 4 digitos)',
        date_format(data_solicitacao, '%d de %M de %Y') as 'Data por extenso',
        date_format(data_solicitacao, '%W, %d de %M de %Y') as 'Data por exetenso (dia da semana)'
from emprestimo;


-- Hora

select time_format(data_hora, '%h:%i:%s') as 'Horário da movimentação',
		time_format(data_hora, '%h:%i:%s (%p)') as 'Horário da movimentação',
        time_format(data_hora, '%H:%i:%s') as 'Horário da movimentação',
		time_format(data_hora, '%r') as 'Horário da movimentação'
from movimentacao;

-- Retorna a data do servidor
select curdate() as 'Data',
	   curtime() as 'Hora';

select current_date() as 'Data',
	   current_time() as 'Hora',
       current_timestamp() as 'Data e Hora';
       
select date_format(data_solicitacao, '%d/%m/%y') as 'Data de solicitação',
	   day(data_solicitacao) as 'Dia',
       month(data_solicitacao) as 'Mês',
       year(data_solicitacao) as 'Ano'
from emprestimo;

-- Calcular diferença entre datas
select datediff('2025-04-28', '2025-01-01');

select datediff(current_date(), '2025-01-01');

-- Calcular diferença entre horas
select timestampdiff(day, '2025-01-01', now()),
	   timestampdiff(month, '2025-01-01', now()),
       timestampdiff(year, '2025-01-01', now());
       
select datediff(current_date(), data_solicitacao) as 'Dias a partir da solicitação'
from emprestimo;

-- Manipulação de textos

select nome_razaosocial
from cliente
where codigo = 10;

update cliente
set nome_razaosocial = ''
where codigo = 10;

-- trim (desconsidera espaços em brancos antes e depois do texto)
select nome_razaosocial
from cliente
where trim(nome_razaosocial) = '';

-- char_lenght (retorna a quantidade de caracteres de um texto)
select nome_razaosocial,
	   char_length(nome_razaosocial) as 'Qtde caracteres'
from cliente
where codigo = 9;

-- left (retona caraterees a esquerda)
select nome_razaosocial,
	   left(nome_razaosocial, 10) as 'caracteres a esquerda'
from cliente
where codigo = 9;


-- pesquisa se um (ou main) caracter exoiste no texto
select nome_razaosocial,
	   position('de' in nome_razaosocial)
from cliente where codigo = 6;

-- substring (retorna uma parte do texto)
select nome_razaosocial,
	   substring(nome_razaosocial, position('' in nome_razaosocial), 10)
from cliente
where codigo = 5;


-- letras minusculas
select nome_razaosocial,
	   lower(nome_razaosocia)
from cliente
where codigo = 4;

-- letras maiusculas
select nome_razaosocial,
	   upper(nome_razaosocia)
from cliente
where codigo = 4;

-- Concatenaçoes
select concat(nome_razaosocial,': ', usuario, '(',  senha, ')')
from cliente







	




