import express, { Request, Response } from 'express';
import cors from 'cors';
import yahooFinance from 'yahoo-finance2';
import dotenv from 'dotenv';

dotenv.config();

const app = express();
app.use(cors());

app.get('/api/stocks/:ticker', async (req: Request, res: Response) => {
    try {
        const { ticker } = req.params;
        const data = await yahooFinance.quote(ticker);

        res.json({
            ticker: data.symbol,
            price: data.regularMarketPrice,
            change: data.regularMarketChangePercent,
        });
    } catch (error) {
        console.error('Error fetching stock data:', error);
        res.status(500).json({ error: 'Failed to fetch stock data' });
    }
});

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
