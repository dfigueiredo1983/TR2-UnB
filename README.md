# TR2-UnB
Disciplina de Teleinformática e Redes 2 da Universidade de Brasília

O projeto foi idealizado para ler dados de um sensor ultrassônico em conjunto com
um arduino.
O arduino envia os dados pela porta serial
Um programa em python lê os dados da porta serial e salva em um arquivo txt e em 
um banco de dados sqlite
Foi criada uma API com o NodeJS para disponibilizar os dados para alguma aplicação web

Executar o projeto
Deve inicialmente montar o sensor no arduino com as devidas ligações elétricas
Salvar o sketch no arduino para executar a rotina de leitura dos dados do sensor 
e enviar para a porta serial
Deve iniciar um prgorama em pyhton com o seguinte comando no mesmo diretório do arquivo
python project.py
Para iniciar o servidor NodeJS deve entrar no diretório api
executar o comando "npm install"
Após isso, deve iniciar o servidor Node com o comando "node index.js"
Acessar o endereço pelo navegador: "localhost:8080/ultrassom"
para visualizar os dados enviar pela porta serial