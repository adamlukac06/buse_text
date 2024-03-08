const express = require('express');
const { exec } = require('child_process');
const app = express();
const port = 3000;

app.use(express.json()); // Middleware to parse JSON bodies
app.use(express.static('public')); // Serve static files from 'public' directory

app.post('/submit-text', (req, res) => {
    const { text } = req.body;
    console.log(`Received text: ${text}`);
    
    // Use the full path for Python executable and the script
    const pythonPath = "C:/Users/adaml/AppData/Local/Programs/Python/Python312/python.exe";
    const scriptPath = "c:/Users/adaml/Desktop/Cursor_projects/buse_text/automate_input.py";
    
    exec(`"${pythonPath}" "${scriptPath}" "${text.replace(/"/g, '\\"')}"`, (error, stdout, stderr) => {
        if (error) {
            console.error(`exec error: ${error}`);
            return res.status(500).send({message: 'Failed to submit text', error: stderr});
        }
        console.log(`stdout: ${stdout}`);
        res.send({ message: 'Text submitted successfully', output: stdout });
    });
});

app.listen(port, () => {
    console.log(`Server listening at http://localhost:${port}`);
});
