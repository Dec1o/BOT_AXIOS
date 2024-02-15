# DOCUMENTAÇÃO

O objetivo deste projetoé ser uma soluçãofeita sob medida paragerenciar os chamados dentro do sistema AXIOS ASSYST, logoapós, deve realizar umaligação afim denotificar o profissional responsávelpela solução dos chamados.



# Módulo BOT, 1. Visão Geral

O módulo boté responsável por gerenciar as operações relacionadas à interação com a interface gráfica de usuário, atualizando chamados, clicando em elementos específicos e processando texto copiado.


# 2. Funcionalidades Principais

2.1 Atualização de Chamados: O  bot  atualiza  periodicamente  os  chamados  na  interface,  garantindo  que  as  informações  mais  recentes estejam sempre disponíveis.

2.2 Atualização do Menu: Além dos chamados, o bot também atualiza o menu da aplicação para garantir que todas as opções estejam acessíveis.

2.3 Clique em Chamados: O bot clica em chamados específicos para realizar ações adicionais, como reconhecimento ou tratamento.

2.4 Tratamento de Bugs: O código inclui tratamento para possíveis bugs, como recarregar o site em caso de falhas.
 
2.5 Processamento de Texto Copiado: O bot copia o texto nainterface e processa-o para determinar qual ação tomarcom base nas informações.

2.6 Reinicialização Periódica: O bot reinicia a página da aplicação após um determinado número de iterações para garantir a estabilidade e integridade das operações.


# Bibliotecas utilizadas

• time: Para controlar os intervalos de tempo entre as operações.

• pyautogui: Para interagir com a interface gráfica de usuário.

• pyperclip: Para acessar a área de transferência e copiar texto.



# Módulo funcoes, 1. Visão Geral

O  módulofuncoesé  responsável  por  gerenciar  as  operações  relacionadas  à  realização  de  chamadas telefônicas  por  meio  de  um  serviço  online.  Ele  automatiza  o  navegador  web  para  acessar  o  serviço, autenticar-se, discar números de telefone e enviar mensagens pré-configuradas.


# 2. Funcionalidades Principais

2.1 Acesso ao Serviço de Chamadas: O bot acessa um serviço online específico para realizar chamadas telefônicas.

2.2 Autenticação Automátic: aApós o acesso ao serviço, é realizada uma autenticação automática, fornecendo as credenciais necessárias.

2.3 Discagem de Números de Telefone: O bot discará números de telefone específicos conforme necessário.

2.4 Envio de Mensagens: Além  de  discar  números,  o  bot  também  é  capaz  de  enviar  mensagens  pré-configuradas  de  acordo  com  o horário atual.

2.5 Finalização de Chamadas: Após a conclusão da chamada, o bot finaliza a ligação.


# 3. Bibliotecas utilizadas

• selenium:  Essa  biblioteca  é  utilizada  para  automatizar  o  navegador  web.  Ela  permite  simular  a interação  humana  com  o  navegador,  como  clicar  em  botões,  preencher  formulários  e  navegar  em páginas da web.

• webdriver_manager:  Utilizado  para  gerenciar  automaticamente  a  instalação  do  driver  específico  do navegador, no caso o ChromeDriver.

• ChromeDriverManager:  Especificamente,  essa  biblioteca  automatiza  o  processo  de  instalação  do ChromeDriver, garantindo que a versão correta seja baixada e instalada de acordo com a versão do navegador Chrome instalada no sistema.



Décio Carvalho Faria © 2024. Todos os direitos reservados.



