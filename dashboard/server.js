const express = require('express');
const app = express();
const path = require('path');
const indexRouter = require('./routes/index');
const characterRouter = require('./routes/character');

app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));

app.use(express.static(path.join(__dirname, 'public')));
app.use('/', indexRouter);
app.use('/character', characterRouter);

const PORT = 3000;
app.listen(PORT, () => console.log(`Dashboard running on http://localhost:${PORT}`));
