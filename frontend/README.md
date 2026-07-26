# AcousticSpace - Deepfake Detection Frontend

### Project Structure:

```
frontend/
├── index.html
├── package.json
├── tsconfig.json
├── tsconfig.node.json
├── vite.config.ts
├── .gitignore
├── src/
│   ├── main.tsx
│   ├── App.tsx
│   ├── styles.css
│   └── components/
│       ├── AudioUploader.tsx
│       ├── ResultsPanel.tsx
│       └── WaveformPlayer.tsx
```

## Next Steps:

### 1. Install Node.js
If you don't have Node.js installed, download it from https://nodejs.org/ (LTS version recommended)

### 2. Install Dependencies
```bash
cd frontend
npm install
```

### 3. Start Development Server
```bash
npm run dev
```

The app will run on `http://localhost:3000`

### 4. Build for Production
```bash
npm run build
```

## Features:

- 🎙️ Audio file upload
- 📊 Real-time waveform visualization
- 🔍 Deepfake detection analysis
- 📈 Results dashboard with confidence scores
- 🎨 Modern dark UI with gradient styling

## Backend Connection:

The frontend connects to the backend API at `http://localhost:8000/analyze`

Make sure your backend service is running on port 8000 for the analysis feature to work.
