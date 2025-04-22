const express = require('express');
const fs = require('fs');
const path = require('path');
const router = express.Router();

const characterDir = process.env.CHARACTER_DIR || path.join(__dirname, '../../bot/characters');

router.get('/:name', (req, res) => {
  const filename = path.join(characterDir, `${req.params.name}.json`);
  fs.readFile(filename, 'utf8', (err, data) => {
    if (err) return res.status(404).send("Character not found.");
    const character = JSON.parse(data);
    res.render('character', { character });
  });
});

module.exports = router;
