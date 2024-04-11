FROM imbios/bun-node:18-slim AS deps

WORKDIR /app

COPY package.json bun.lockb ./

RUN bun install --frozen-lockfile

COPY . .

RUN bun run --env-file .env.local build 

EXPOSE 3000

CMD ["bun", "run", "--env-file", ".env.local", "start"]
