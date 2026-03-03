You are a senior Web3 backend engineer and quantitative developer.



Build a production-grade Telegram trading bot called "AshArb".



AshArb must:



1) Connect securely to Polymarket using my API key.

2) Execute automated arbitrage strategies on underpriced 5-minute markets.

3) Detect pricing inefficiencies across complementary outcomes (YES/NO arbitrage).

4) Track top-performing whale wallets in real time.

5) Copy whale trades based on configurable filters:

   - Minimum trade size

   - ROI threshold

   - Profit consistency

   - Market category filters

6) Execute trades automatically using my connected wallet.

7) Implement strict risk management:

   - Max % capital per trade

   - Daily loss cap

   - Slippage protection

   - Position size control

8) Include logging, error handling, retry logic, and API rate-limit protection.

9) Include dry-run / simulation mode.

10) Provide Telegram bot interface for:

   - /status

   - /balance

   - /positions

   - /start

   - /stop

   - /config

   - /whales

   - /arb-opportunities



Tech Requirements:

- Use TypeScript + Node.js

- Clean modular architecture

- Use environment variables (.env) for API keys and private keys

- Include Dockerfile

- Include README.md

- Include example config.json

- Include unit-test structure

- Code must be structured for production deployment

- No hardcoded secrets



Architecture:

- src/

    - api/

    - strategies/

    - whaleTracker/

    - arbitrageEngine/

    - execution/

    - telegram/

    - riskManager/

    - utils/



Output Requirements:

1) Full project folder structure

2) All core source code files

3) Setup instructions

4) Step-by-step GitHub commit guide

5) Step-by-step VPS deployment guide (Ubuntu)

6) Optional: Docker deployment guide



The bot must be secure, scalable, and designed for real capital use.



Do not generate simplified or demo code. Build it like a real trading system.# Crypto-security-checker
