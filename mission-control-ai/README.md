No inicio do programa, é criado uma matriz 8X5, em que representa os dados da missão. As linhas representam os ciclos, nesse caso são 8
e as colunas representam os dados de cada ciclo, contendo a temperatura, comunicacao, bateria, oxigenio, estabilidade respectivamente.

Depois foi criado uma lista que contem as areas monitoradas, sendo elas a Temperatura interna, a Comunicação com a base, o Sistema de energia,
o Suporte de oxigênio, a Estabilidade operacional, respectivamente.

Após isso foram criadas as funções essenciais para o programa. A função analisar_temperatura() é responsável por analisar a temperatura de cada ciclo da missão, retornando se a situação está em estado normal, atenção ou crítico de acordo com os limites definidos no sistema.

A função analisar_comunicacao() foi desenvolvida para verificar a qualidade da comunicação com a base terrestre, classificando o sinal conforme os níveis de risco estabelecidos.

A função analisar_bateria() analisa o nível de bateria disponível na missão, identificando situações de estabilidade, atenção ou risco crítico de energia.

A função analisar_oxigenio() é responsável por verificar o suporte de oxigênio da missão, analisando se os níveis estão adequados para a operação segura do sistema espacial.

A função analisar_estabilidade() verifica a estabilidade operacional geral da missão, permitindo identificar possíveis riscos relacionados ao funcionamento dos sistemas da nave.

Também foi criada a função pontuar(), utilizada para transformar cada classificação em uma pontuação de risco, sendo normal igual a 0 pontos, atenção igual a 1 ponto e crítico igual a 2 pontos.

A função classificar_ciclo() foi desenvolvida para classificar cada ciclo da missão como missão estável, missão em atenção ou missão crítica, de acordo com a pontuação total obtida durante a análise.

Por fim, a função gerar_recomendacao() gera automaticamente recomendações para a equipe da missão, orientando ações de monitoramento, prevenção ou segurança conforme o nível de risco identificado em cada ciclo analisado.

Após a criação das funções, o programa inicializa duas listas importantes: riscos, utilizada para armazenar a pontuação total de risco de cada ciclo analisado, e risco_areas, responsável por armazenar a pontuação acumulada de cada área monitorada ao longo da missão. Também é criada a variável cont, utilizada para numerar os ciclos exibidos no terminal.

Em seguida, o programa apresenta no terminal as informações iniciais da missão, como o nome da missão, o nome da equipe e a quantidade total de ciclos analisados. Depois disso, é iniciado um laço de repetição for, responsável por percorrer cada ciclo armazenado dentro da matriz dados_missao.

Durante a execução do laço, o sistema analisa individualmente cada informação do ciclo utilizando as funções desenvolvidas anteriormente. A temperatura, comunicação, bateria, oxigênio e estabilidade são classificados como normal, atenção ou crítico. Essas classificações são armazenadas dentro da lista status.

Logo após, outro laço de repetição percorre a lista status para calcular a pontuação total de risco do ciclo. Cada classificação recebe uma quantidade de pontos por meio da função pontuar(). Além disso, a pontuação individual de cada área é armazenada na lista pontuacoes, permitindo calcular posteriormente qual área acumulou maior risco durante toda a missão.

Depois do cálculo dos pontos, o programa utiliza a função classificar_ciclo() para determinar a situação geral do ciclo, podendo classificá-lo como missão estável, missão em atenção ou missão crítica. Em seguida, a função gerar_recomendacao() gera automaticamente uma recomendação de segurança e monitoramento com base no risco identificado.

Após todas as análises do ciclo, o sistema exibe no terminal os valores monitorados, suas classificações, a pontuação total de risco, a classificação geral do ciclo e a recomendação correspondente.

Finalizada a análise de todos os ciclos, o programa inicia a geração do relatório final da missão. Primeiramente, são calculadas as médias de temperatura, comunicação, bateria, oxigênio e estabilidade utilizando estruturas de repetição e variáveis acumuladoras.

Em seguida, o sistema identifica qual foi o ciclo mais crítico da missão, verificando a maior pontuação de risco armazenada na lista riscos. Também é calculado o risco médio da missão e a quantidade de ciclos classificados como críticos.

Depois disso, o programa realiza a análise de tendência da missão, comparando o risco do primeiro ciclo com o risco do último ciclo. Caso o último ciclo possua maior risco, a missão apresenta tendência de piora. Caso o risco seja menor, a missão apresenta tendência de melhora. Se os riscos forem iguais, a missão é considerada estável.

Por fim, o sistema identifica a área mais afetada da missão utilizando a lista risco_areas, verificando qual área acumulou a maior quantidade de pontos de risco durante todos os ciclos monitorados. Todas essas informações são exibidas no relatório final apresentado no terminal, concluindo a análise completa da missão espacial.