
FROM node:18

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

RUN npx tsc


EXPOSE 5000

# Start the server
CMD ["node", "dist/server.js"]
