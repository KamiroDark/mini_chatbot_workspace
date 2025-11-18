const express = require('express');
const cors = require('cors');
const path = require('path');
const fs = require('fs');
const archiver = require('archiver');

const app = express();
const PORT = 3000;

app.use(cors());
app.use(express.json());