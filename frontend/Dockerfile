FROM oven/bun:latest

WORKDIR /app

COPY package.json bun.lockb ./

RUN bun install

COPY . .

RUN bun tailwind

COPY /dist .

EXPOSE 5173

CMD ["bun", "dev", "--host"]