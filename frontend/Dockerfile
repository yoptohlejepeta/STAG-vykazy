# Use the official Bun image as the base
FROM oven/bun:latest

# Set the working directory
WORKDIR /app

# Copy package.json and bun.lockb files
COPY package.json bun.lockb ./

# Install dependencies using Bun
RUN bun install

# Copy the rest of your application code
COPY . .

# Expose the port Vite uses (default is 5173)
EXPOSE 5173

# Command to run the frontend development server
CMD ["bun", "dev", "--host"]