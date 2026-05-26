dados_missao = [
    [25, 91, 87, 95, 89],
    [28, 79, 70, 93, 84],
    [30, 67, 56, 90, 71],
    [35, 44, 36, 86, 57],
    [38, 29, 21, 77, 34],
    [33, 53, 31, 81, 49],
    [26, 88, 74, 92, 83],
    [37, 41, 27, 85, 52]
]
areas_monitoradas = [
    "Temperatura interna",
    "Comunicação com a base",
    "Sistema de energia",
    "Suporte de oxigênio",
    "Estabilidade operacional"
]
def analisar_temperatura(temp):
    if temp<18:
        return 'atenção'
    elif temp>=18 and temp<=30:
        return 'normal'
    elif temp>30 and temp<= 35:
        return 'atenção'
    else:
        return 'critico'    
def analisar_comunicacao(com):
    if com<30:
        return 'critico'
    elif com>=30 and com<=59:
        return 'atenção'
    else:
        return 'normal' 
def analisar_bateria(bat):
    if bat<20:
        return 'critico'
    elif bat>=20 and bat<=49:
        return 'atenção'
    else:
        return 'normal'
def analisar_oxigenio(ox):
    if ox<80:
        return 'critico'
    elif ox>=80 and ox<=89:
        return 'atenção'
    else:
        return 'normal'
def analisar_estabilidade(est):
    if est<40:
        return 'critico'
    elif est>=40 and est<=69:
        return 'atenção'
    else:
        return 'normal'
def classificar_ciclo(pont):
    if pont<=2:
        return 'missão estavel'
    elif pont>=3 and pont<=5:
        return 'missão em atenção'
    elif pont>=6 and pont<=10:
        return 'missão critica'
def pontuar(status):
    if status=="normal":
        return 0
    elif status=="atenção":
        return 1
    else:
        return 2       
def gerar_recomendacao(pont):
    if pont<=2:
        return "Manter operação normal e continuar monitoramento."
    elif pont<=5:
        return "Monitorar sistemas em atenção e preparar plano de contingência."
    else:
        return "Ativar modo de segurança e priorizar sistemas críticos."    
def mostrar(area, mensagem):
    if area == 'Temperatura interna':
        if mensagem == 'critico':
            return 'temperatura muito instavel'
        elif mensagem == 'atenção':
            return 'temperatura instavel'
        else:
            return 'temperatura adequada'
    elif area == 'Comunicação com a base':
        if mensagem == 'critico':
            return 'comunicação critica'
        elif mensagem == 'atenção':
            return 'rever a comunicação'
        else:
            return 'comunicação estavel'
    elif area == 'Sistema de energia':
        if mensagem == 'critico':
            return 'energia em nivel critico'
        elif mensagem == 'atenção':
            return 'energia abaixo do ideal'
        else:
            return 'energia estavel'
    elif area == 'Suporte de oxigênio':
        if mensagem == 'critico':
            return 'oxigenio em nivel critico'
        elif mensagem == 'atenção':
            return 'oxigenio abaixo do ideal'
        else:
            return 'oxigenio adequado'
    elif area == 'Estabilidade operacional':
        if mensagem == 'critico':
            return 'estabilidade operacional critica'
        elif mensagem == 'atenção':
            return 'estabilidade reduzida'
        else:
            return 'estabilidade adequada'
riscos=[]
risco_areas=[0, 0, 0, 0, 0]
cont=1  
print('======================================')
print('MISSION CONTROL AI')
print('======================================')
print('Missão: Orion Test Alpha')
print('Equipe: Equipe Apollo')
print(f'Quantidade de ciclos analisados: {len(dados_missao)}')
print('======================================')
for ciclo in dados_missao:
    pontuacoes=[]
    pont=0
    print('======================================')
    print(f'CICLO {cont}')
    print('======================================')
    cont+=1
    temperatura=analisar_temperatura(ciclo[0])
    comunicacao=analisar_comunicacao(ciclo[1])
    bateria=analisar_bateria(ciclo[2])
    oxigenio=analisar_oxigenio(ciclo[3])
    estabilidade=analisar_estabilidade(ciclo[4])
    status=[temperatura, comunicacao, bateria, oxigenio, estabilidade]
    for i in status:
        pontos=pontuar(i)
        pont+=pontos
        pontuacoes.append(pontos)
    ciclos=classificar_ciclo(pont)
    recomendacao=gerar_recomendacao(pont)
    riscos.append(pont)
    for i in range(len(risco_areas)):
        risco_areas[i]+=pontuacoes[i]
    print(f"Temperatura: {ciclo[0]}°C | {temperatura} | {mostrar(areas_monitoradas[0],temperatura)}")
    print(f"Comunicação: {ciclo[1]}% | {comunicacao} | {mostrar(areas_monitoradas[1],comunicacao)}")
    print(f"Bateria: {ciclo[2]}% | {bateria} | {mostrar(areas_monitoradas[2],bateria)}")
    print(f"Oxigênio: {ciclo[3]}% | {oxigenio} | {mostrar(areas_monitoradas[3],oxigenio)}")
    print(f"Estabilidade: {ciclo[4]}% | {estabilidade} | {mostrar(areas_monitoradas[4],estabilidade)}")
    print(f"Pontuação de risco do ciclo: {pont}")
    print(f"Classificação do ciclo: {ciclos}")
    print(f"Recomendação: {recomendacao}")
soma_temp=0
soma_com=0
soma_bat=0
soma_ox=0
soma_est=0
for linha in dados_missao:
    soma_temp+=linha[0]
    soma_com+=linha[1]
    soma_bat+=linha[2]
    soma_ox+=linha[3]
    soma_est+=linha[4]
media_temp=soma_temp/len(dados_missao)
media_com=soma_com/len(dados_missao)
media_bat=soma_bat/len(dados_missao)
media_ox=soma_ox/len(dados_missao)
media_est=soma_est/len(dados_missao)
maior_risco=0
ciclo_mais_critico=0
for i in range(len(riscos)):
    if riscos[i]>maior_risco:
        maior_risco=riscos[i]
        ciclo_mais_critico=i+1
soma_riscos=0
qtd_criticos=0
for risco in riscos:
    soma_riscos+=risco
    if risco>=6:
        qtd_criticos+=1
risco_medio=soma_riscos/len(riscos)
if riscos[-1]>riscos[0]:
    tendencia="A missão apresentou tendência de piora."
elif riscos[-1]<riscos[0]:
    tendencia="A missão apresentou tendência de melhora."
else:
    tendencia="A missão permaneceu estável."
maior_area=0
pos_area=0
for i in range(len(risco_areas)):
    if risco_areas[i]>maior_area:
        maior_area=risco_areas[i]
        pos_area=i
print()
print('======================================')
print('RELATÓRIO FINAL DA MISSÃO')
print('======================================')
print(f'Média de temperatura: {media_temp:.2f} °C')
print(f'Média de comunicação: {media_com:.2f}%')
print(f'Média de bateria: {media_bat:.2f}%')
print(f'Média de oxigênio: {media_ox:.2f}%')
print(f'Média de estabilidade: {media_est:.2f}%')
print(f'Ciclo mais crítico: Ciclo {ciclo_mais_critico}')
print(f'Maior pontuação de risco: {maior_risco}')
print(f'Risco médio da missão: {risco_medio:.2f}')
print(f'Quantidade de ciclos críticos: {qtd_criticos}')
print(f'Tendência da missão: {tendencia}')
print()
print('pontuação acumulada por area:')
for i in range(len(areas_monitoradas)):
    print(f'{areas_monitoradas[i]}: {risco_areas[i]} pontos')
print()
print(f'Área mais afetada: {areas_monitoradas[pos_area]}')
print(f'Classificação final da missão: {classificar_ciclo(risco_medio)}')