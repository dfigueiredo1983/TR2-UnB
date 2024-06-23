const express = require('express');
const { CONSTRAINT } = require('sqlite3');
const sqlite3 = require('sqlite3').verbose();

const app = express();
const port = process.env.PORT || 8080;

const db = new sqlite3.Database('.././tr2.db', (err) => {
    if(err){
        console.error(err.message);
    }
    console.log('Conectado ao banco de dados products');
});

app.use(express.json());

// GET all products
app.get('/ultrassom', (req, res) => {
    db.all('SELECT * FROM ultrasonic', (err, rows) => {
        if(err){
            console.error(err.message);
            res.status(500).send('Erro interno no servidor');
        } else {
            res.send(rows);
        }
    });
});

app.listen(port, () => {
    console.log('Servidor escutando na porta ${port}');
});