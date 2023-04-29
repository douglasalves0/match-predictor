# Match Predictor

Um app em python que usa de heurísticas para tentar prever o resultados de jogos do brasileirão, para isso, recebe como entradas a sigla de dois times que participam da primeira divisão do campeonato brasileiro de futebol e retorna como saída o resultado esperado para a partida entre os dois times, usando como base os jogos anteriores do campeonato.

## API

O app usa uma API de onde recebe os dados das partidas, logo, para seu devido funcionamento é necessário que o usuário tenha uma conta [neste site](https://api-futebol.com.br/) e que configure sua chave da API em um arquivo .env na raiz do projeto. A chave da API deve ser configurada com nome de **TOKEN** no arquivo .env.

Fora isso, também é necessário configurar o id da tabela do campeonato brasileiro do ano atual no arquivo .env. O id da tabela deve ser configurada com nome de **TABLE_ID** no arquivo .env. E em 2023 esse id tem valor 10.

É dado um arquivo nomeado .envsample no repositório que serve de template para a configuração das variáveis de ambiente citadas acima.

## Algoritmo

Se uma partida ocorrerá entre os times **A** e **B**, então o número de gols marcados por **A** nessa partida é igual a (x+y)/2, onde:

x = número médio de gols marcados por partida de A;

y = número médio de gols sofridos por partida de A;

E o mesmo serve para B.