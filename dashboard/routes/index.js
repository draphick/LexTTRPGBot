const express = require('express');
const fs = require('fs');
const path = require('path');
const router = express.Router();

const characterDir = process.env.CHARACTER_DIR || path.join(__dirname, '../../bot/characters');

router.get('/', (req, res) => {
  fs.readdir(characterDir, (err, files) => {
    if (err) return res.status(500).send("Couldn't read character directory.");
    const characters = files.filter(f => f.endsWith('.json')).map(f => path.basename(f, '.json'));
    res.render('index', { characters });
  });
});

module.exports = router;
