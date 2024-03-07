const express = require('express');
const { exec } = require('child_process');
const app = express();
const port = 3000;

app.use(express.json()); // Middleware to parse JSON bodies

app.post('/submit-text', (req, res) => {
    const { text } = req.body;
    console.log(`Received text: ${text}`);
    // Replace automate_input.py with the path to your actual Python script
    exec(`python automate_input.py "${text.replace(/"/g, '\\"')}"`, (error, stdout, stderr) => {
        if (error) {
            console.error(`exec error: ${error}`);
            return res.status(500).send('Failed to submit text');
        }
        res.send({ message: 'Text submitted successfully' });
    });
});

app.listen(port, () => {
    console.log(`Server listening at http://localhost:${port}`);
});
