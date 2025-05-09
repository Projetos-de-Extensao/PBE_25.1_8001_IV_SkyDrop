---
id: brainstorm
title: Brainstorm
weight: -200
---

## Introdução
<p align="justify">
O brainstorm é uma técnica de elicitação de requisitos que consiste em reunir a equipe e discutir sobre diversos tópicos gerais do projeto apresentados no documento problema de negócio. No brainstorm o diálogo é incentivado e críticas são evitadas para permitir que todos colaborem com suas próprias ideias.
</p>

## Metodologia
<p align="justify">
A equipe se reuniu para debater ideias gerais sobre o projeto via reunião remota, começou às 14h e terminou às 15h30, no dia 01/04/2025. João Carvalho foi o moderador, direcionando a equipe com questões pré-elaboradas, e transcrevendo as respostas para o documento.
</p>

## Brainstorm

## Versão 1.0
---

### 1. Qual o objetivo principal da aplicação?

<p align="justify"><b>Pedro Henrique</b> - Permitir que moradores da Ilha Primeira possam receber pedidos via iFood, superando a limitação de acesso por terra.</p>
<p align="justify"><b>Nicholas Borges</b> - Integrar a estrutura logística existente na ilha com a plataforma iFood, otimizando a experiência do usuário.</p>
<p align="justify"><b>Alex Euzébio</b> - Criar um fluxo de entrega híbrido, envolvendo entregadores no continente e na ilha, além de tecnologias emergentes como drones.</p>

---

### 2. Quais desafios logísticos precisam ser superados?

<p align="justify"><b>Gabriel Mendonça</b> - O único acesso à ilha é via embarcações, tornando a logística dependente das condições climáticas.</p>
<p align="justify"><b>Gabriel Maia</b> - A sincronização entre os entregadores do continente e da ilha exige planejamento e comunicação eficientes.</p>
<p align="justify"><b>Pedro Henrique</b> - Garantir segurança e rastreabilidade no ponto de transbordo (píer) é fundamental para evitar perdas.</p>

---

### 3. Como será o processo para cadastrar um novo cliente e adicionar produtos?

<p align="justify"><b>Nicholas Borges</b> - Para novos moradores ou visitantes, o cadastro como "cliente da ilha" poderia ser feito no app local, habilitando a entrega personalizada na ilha.</p>
<p align="justify"><b>Alex Euzébio</b> - A plataforma deve permitir o cadastro de novos moradores (clientes) com endereço específico da ilha.</p>
<p align="justify"><b>Gabriel Mendonça</b> - Produtos disponíveis para entrega na ilha podem ser configurados por restaurante com base em tempo de conservação e transporte.</p>
<p align="justify"><b>Gabriel Maia</b> - O sistema pode ter uma área específica para que os estabelecimentos cadastrem produtos "aprovados para envio à ilha", garantindo compatibilidade com a logística.</p>
<p align="justify"><b>Pedro Henrique</b> - O cadastro de produtos deve considerar restrições como tempo de viagem, embalagem e temperatura, para garantir a qualidade na entrega.</p>

---

### 4. Quais soluções podem ser implementadas para viabilizar as entregas?

<p align="justify"><b>Nicholas Borges</b> - Implementar um sistema de dois entregadores: um que leve os pedidos até o píer e outro que faça a entrega dentro da ilha.</p>
<p align="justify"><b>Alex Euzébio</b> - Utilizar drones para entregas diretas em regiões mais afastadas da ilha.</p>
<p align="justify"><b>Gabriel Mendonça</b> - Estabelecer parceria com o serviço "Ilha Delivery", que já opera na região, aproveitando sua estrutura.</p>

---

### 5. Quais tecnologias podem auxiliar no processo?

<p align="justify"><b>Gabriel Maia</b> - Sistema de geolocalização para mapeamento detalhado das residências da ilha.</p>
<p align="justify"><b>Pedro Henrique</b> - Aplicativo para rastreamento das entregas e comunicação entre os entregadores.</p>
<p align="justify"><b>Nicholas Borges</b> - Integração entre a API do iFood e a do parceiro logístico local.</p>

---

### 6. Quais são os próximos passos para a implementação?

<p align="justify"><b>Alex Euzébio</b> - Realizar mapeamento técnico da ilha e levantamento das rotas viáveis.</p>
<p align="justify"><b>Gabriel Mendonça</b> - Entrar em contato com representantes do "Ilha Delivery" e iniciar tratativas com o iFood.</p>
<p align="justify"><b>Gabriel Maia</b> - Desenvolver um MVP e testar o fluxo com entregas simuladas ou reais em pequena escala.</p>

---

### 7. Quais informações seriam interessantes para o cliente?

<p align="justify"><b>Pedro Henrique</b> - Informações sobre o tempo estimado de chegada do pedido, considerando a logística com transbordo e clima.</p>
<p align="justify"><b>Nicholas Borges</b> - A localização atual do pedido (rastreamento em tempo real ou por etapas: restaurante → píer → entrega).</p>
<p align="justify"><b>Alex Euzébio</b> - Nome do entregador responsável pela etapa na ilha, para facilitar o contato em caso de dúvidas.</p>
<p align="justify"><b>Gabriel Mendonça</b> - Notificações sobre atrasos por conta de maré, chuva ou ventos, com base em dados climáticos.</p>
<p align="justify"><b>Gabriel Maia</b> - Confirmação de entrega visual (foto do pacote entregue ou assinatura digital).</p>

---

### Requisitos elicitados

|ID|Descrição|
|----|-------------|
|BS01| A aplicação deve permitir a divisão de entrega em duas etapas com pontos de transbordo definidos.|
|BS02| A aplicação deve integrar entregadores locais ao fluxo de entregas iFood.|
|BS03| A aplicação deve ser capaz de rastrear o status da entrega mesmo em ambientes com conectividade limitada.|
|BS04| A solução logística deve considerar a viabilidade de uso de drones.|
|BS05| O sistema deve possibilitar integração com serviços logísticos parceiros como o Ilha Delivery.|
|BS06| O sistema deve permitir o cadastro de clientes com endereço insular.|
|BS07| Os produtos oferecidos devem respeitar restrições de transporte (conservação, embalagem, tempo).|

## Conclusão
<p align="justify">
Através da aplicação da técnica, foi possível elicitar alguns dos primeiros requisitos do projeto "Ilha Primeira", oferecendo uma base sólida para a próxima etapa de planejamento e desenvolvimento.
</p>

## Referências Bibliográficas

> iFood Developer Documentation. https://developer.ifood.com.br/  
> ANAC – Regras para uso de drones. https://www.gov.br/anac/

## Autor(es)

| Data | Versão | Descrição | Autor(es) |
| -- | -- | -- | -- |
| 01/04/2025 | 1.0 | Criação do documento | Pedro Henrique, Nicholas Borges, Alex Euzébio, Gabriel Mendonça, Gabriel Maia |
