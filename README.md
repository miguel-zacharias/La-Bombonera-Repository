# 🚚 La Bombonera Repository  
![Raspberry Pi](https://img.shields.io/badge/Raspberry%20Pi-Project-red?style=for-the-badge&logo=raspberrypi)  
![Status](https://img.shields.io/badge/Status-In%20Development-blue?style=for-the-badge&logo=github)  
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)  

---

## 🌐 Website  
**Página oficial:**  
👉 https://labombo.rf.gd

Explore tudo num visual direto: equipe, tecnologias, protótipo e progresso do sistema.

---

## 📖 Sobre o Projeto  
O projeto utiliza uma **Raspberry Pi Pico 2W** para controlar uma **esteira transportadora** e um **mini caminhão**, simulando um processo logístico automatizado real.

### 🎯 Objetivo Principal  
Criar uma esteira totalmente automatizada com um carrinho finalizador usando **sensor PIR** que interrompe a esteira no momento certo e realiza o **descarregamento automático** dos produtos.

---

## 🔧 Funcionalidades  
- **Detecção automática** (sensor PIR)  
- **Interrupção inteligente** da esteira  
- **Descarregamento autônomo** do caminhão  
- **Integração IoT** com a Raspberry Pi Pico 2W  
- **Monitoramento em tempo real**  

---

## ⚙️ Tech Stack  
- Raspberry Pi Pico 2W  
- MicroPython  
- Sensor PIR HC-SR501  
- Servo SG90  
- Motor DC 6V  
- Ponte H L298N  
- Sistema de esteira customizado  
- WiFi / Bluetooth  

---

## 🧩 Lista de Hardware (Detalhada)  
| Componente | Quantidade | Observações |
|-----------|------------|-------------|
| Raspberry Pi Pico 2W | 1 | Microcontrolador principal |
| Sensor PIR HC-SR501 | 1 | Detecta presença no final da esteira |
| Motor DC 6V | 1 | Movimenta a esteira |
| Ponte H L298N | 1 | Controla o motor |
| Servo SG90 | 1 | Sistema de descarga |
| Mini Caminhão | 1 | Carrinho finalizador |
| Fonte 5V externa | 1 | Alimentação dos atuadores |
| Jumpers / Protoboard | — | Ligações gerais |
| Estrutura da esteira | 1 | Parte física |

---

## 🔌 Pinagem Completa  
| Componente | Pino do Componente | Pino no Pico | Função |
|-----------|--------------------|--------------|--------|
| PIR HC-SR501 | OUT | GP15 | Detecção |
| PIR HC-SR501 | VCC / GND | 5V / GND | Alimentação |
| Motor da Esteira (via L298N) | IN1 / IN2 | GP2 / GP3 | Controle |
| Ponte H L298N | ENA | 5V | Ativação |
| Ponte H L298N | VCC / GND | 12V / GND | Alimentação do motor |
| Servo SG90 | Sinal | GP10 | Movimento |
| Servo SG90 | VCC / GND | 5V / GND | Alimentação |
| Pico 2W | WiFi | — | Comunicação IoT |

---

# 🍯 La Bombonera - Raspberry Pi Pico 2W

Projeto de automação e IoT desenvolvido pelo grupo La Bombonera utilizando Raspberry Pi Pico 2W.

## 🚀 Como Começar

Clone o repositório:

```bash
git clone https://github.com/miguel-zacharias/La-Bombonera-Repository.git
cd La-Bombonera-Repository
```

## 📌 Pré-requisitos

- Raspberry Pi Pico 2W
- Firmware MicroPython instalado
- Motor DC, L298N, Servo SG90, PIR HC-SR501
- Rede WiFi disponível
- Cabo micro-USB
- Fonte 5V externa para atuadores

## 🛠️ Instalação

1. Instale MicroPython na Pico 2W
2. Suba os arquivos do projeto para o microcontrolador
3. Monte todo o hardware seguindo a tabela de pinagem
4. Edite o arquivo `config.py` com suas credenciais WiFi
5. Execute o arquivo principal utilizando Thonny ou outro IDE

## 👥 Membros da Equipe

- **Agnaldo** – Backend
- **Augusto** – UI/UX
- **Italo** – Hardware
- **Miguel Z.** – Full Stack

Mais informações na página da equipe: [labombo.rf.gd](https://labombo.rf.gd)

## 📈 Status do Projeto

- ✅ Estrutura física montada
- ✅ Sensores integrados
- 🔄 Calibração do PIR
- 🔄 Mecanismo de descarga do caminhão
- ⏳ Comunicação WiFi
- ⏳ Interface Web

## 🤝 Contribuindo

1. Faça um fork
2. Crie uma branch (`git checkout -b feature/NovaFeature`)
3. Commit suas mudanças (`git commit -m 'Adiciona XYZ'`)
4. Push na sua branch (`git push origin feature/NovaFeature`)
5. Abra um Pull Request

## 📝 Licença

MIT — veja o arquivo [LICENSE](LICENSE).

## 📞 Contato

Entre em contato através da nossa [página da equipe](https://labombo.rf.gd) ou abra uma issue neste repositório.

---

<div align="center">
  Feito com ❤️ pelo time La Bombonera
</div>

GitHub: https://github.com/miguel-zacharias/La-Bombonera-Repository
